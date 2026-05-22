#!/usr/bin/env python3
"""
RS Cinema Villa — Daily Social Media Poster
Posts one photo per day to Instagram, Facebook, X (Twitter), LinkedIn, and YouTube Shorts.
Run via GitHub Actions cron; add photos to the photos/ folder to queue them.
"""

import os
import json
import time
import logging
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).parent.parent
PHOTOS_DIR = REPO_ROOT / "photos"
LOG_FILE = REPO_ROOT / "posted_log.json"

# ---------------------------------------------------------------------------
# Caption content
# ---------------------------------------------------------------------------
REQUIRED_LINE = "Book a villa stay, RS Cinema Villa | Contact: +91 9206845678"

CAPTION_TEMPLATES = [
    (
        "✨ Welcome to RS Cinema Villa — where luxury meets nature.\n\n"
        "🎬 Experience a private cinema right inside your villa.\n"
        "🌿 Surrounded by greenery, perfect for a peaceful retreat.\n\n"
        "{required}\n\n{hashtags}"
    ),
    (
        "🏡 Your dream villa getaway awaits!\n\n"
        "☀️ Mornings here are pure bliss — sip coffee in paradise.\n"
        "🎥 Evenings? Enjoy private cinema screenings under the stars.\n\n"
        "{required}\n\n{hashtags}"
    ),
    (
        "🌟 Escape the ordinary at RS Cinema Villa.\n\n"
        "🛌 Luxurious rooms  🎬 Private cinema  🌿 Lush surroundings\n"
        "The perfect getaway for families, couples & groups.\n\n"
        "{required}\n\n{hashtags}"
    ),
    (
        "🎬 Cinema + Villa = The perfect combination!\n\n"
        "✅ Cozy luxury villa stay\n"
        "✅ Private cinema experience\n"
        "✅ Beautiful natural surroundings\n\n"
        "{required}\n\n{hashtags}"
    ),
    (
        "🌺 Every moment at RS Cinema Villa is worth capturing.\n\n"
        "📸 Beautiful spaces  🎬 Unforgettable experiences\n"
        "💫 Make memories that last a lifetime.\n\n"
        "{required}\n\n{hashtags}"
    ),
    (
        "🏖️ Looking for the perfect weekend getaway?\n\n"
        "RS Cinema Villa offers:\n"
        "🎯 Private villa with cinema\n"
        "🌿 Serene environment\n"
        "👨‍👩‍👧‍👦 Perfect for families & groups\n"
        "💑 Ideal for couples\n\n"
        "{required}\n\n{hashtags}"
    ),
    (
        "🌙 Nights at RS Cinema Villa are absolutely magical ✨\n\n"
        "Imagine watching your favourite movies in a private cinema\n"
        "while staying in a luxurious villa. Make it happen!\n\n"
        "{required}\n\n{hashtags}"
    ),
]

HASHTAGS = (
    "#RSCinemaVilla #CinemaVilla #VillaStay #LuxuryVilla "
    "#VacationRental #VillaLife #LuxuryTravel #IndiaTravel "
    "#VillaRental #StayInStyle #PrivateCinema #WeekendGetaway "
    "#VillaExperience #TravelIndia #RSGlobalTV #HolidayHome "
    "#LuxuryHoliday #VillaHoliday #CinemaExperience #BookNow"
)

# ---------------------------------------------------------------------------
# Credentials (injected via GitHub Secrets)
# ---------------------------------------------------------------------------
FB_ACCESS_TOKEN      = os.environ.get("FB_ACCESS_TOKEN", "")
FB_PAGE_ID           = os.environ.get("FB_PAGE_ID", "")
IG_ACCESS_TOKEN      = os.environ.get("IG_ACCESS_TOKEN", "")
IG_USER_ID           = os.environ.get("IG_USER_ID", "")
TWITTER_API_KEY      = os.environ.get("TWITTER_API_KEY", "")
TWITTER_API_SECRET   = os.environ.get("TWITTER_API_SECRET", "")
TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN", "")
TWITTER_ACCESS_SECRET= os.environ.get("TWITTER_ACCESS_SECRET", "")
LINKEDIN_ACCESS_TOKEN= os.environ.get("LINKEDIN_ACCESS_TOKEN", "")
LINKEDIN_PERSON_ID   = os.environ.get("LINKEDIN_PERSON_ID", "")
YOUTUBE_CLIENT_ID    = os.environ.get("YOUTUBE_CLIENT_ID", "")
YOUTUBE_CLIENT_SECRET= os.environ.get("YOUTUBE_CLIENT_SECRET", "")
YOUTUBE_REFRESH_TOKEN= os.environ.get("YOUTUBE_REFRESH_TOKEN", "")
GITHUB_REPOSITORY    = os.environ.get("GITHUB_REPOSITORY", "rscinemavilla/RSCinemaVilla")
GITHUB_REF_NAME      = os.environ.get("GITHUB_REF_NAME", "main")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_log() -> dict:
    if LOG_FILE.exists():
        with open(LOG_FILE) as f:
            return json.load(f)
    return {"posted": [], "last_posted": None, "history": []}


def save_log(log: dict) -> None:
    with open(LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)


def get_next_photo(log: dict) -> str:
    supported = {".jpg", ".jpeg", ".png", ".webp"}
    photos = sorted(
        p.name
        for p in PHOTOS_DIR.iterdir()
        if p.suffix.lower() in supported
    )
    if not photos:
        raise FileNotFoundError("No photos found in photos/ directory. Please add images.")

    posted = set(log.get("posted", []))
    unposted = [p for p in photos if p not in posted]

    if not unposted:
        logger.info("All photos posted — restarting cycle.")
        log["posted"] = []
        unposted = photos

    return unposted[0]


def generate_caption() -> str:
    day = datetime.now(timezone.utc).timetuple().tm_yday
    template = CAPTION_TEMPLATES[day % len(CAPTION_TEMPLATES)]
    return template.format(required=REQUIRED_LINE, hashtags=HASHTAGS)


def public_image_url(filename: str) -> str:
    return (
        f"https://raw.githubusercontent.com/{GITHUB_REPOSITORY}/"
        f"{GITHUB_REF_NAME}/photos/{filename}"
    )


# ---------------------------------------------------------------------------
# Platform posting functions
# ---------------------------------------------------------------------------

def post_to_facebook(image_path: Path, caption: str) -> dict:
    if not FB_ACCESS_TOKEN or not FB_PAGE_ID:
        logger.warning("Facebook: credentials missing — skipping.")
        return {"status": "skipped"}

    url = f"https://graph.facebook.com/v19.0/{FB_PAGE_ID}/photos"
    with open(image_path, "rb") as f:
        resp = requests.post(
            url,
            data={"caption": caption, "access_token": FB_ACCESS_TOKEN},
            files={"source": f},
        )
    result = resp.json()
    if "error" in result:
        logger.error(f"Facebook error: {result['error']}")
    else:
        logger.info(f"Facebook posted  id={result.get('id')}")
    return result


def post_to_instagram(image_url: str, caption: str) -> dict:
    if not IG_ACCESS_TOKEN or not IG_USER_ID:
        logger.warning("Instagram: credentials missing — skipping.")
        return {"status": "skipped"}

    # 1 — create media container
    resp = requests.post(
        f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media",
        data={
            "image_url": image_url,
            "caption": caption,
            "access_token": IG_ACCESS_TOKEN,
        },
    )
    result = resp.json()
    if "error" in result:
        logger.error(f"Instagram container error: {result['error']}")
        return result

    container_id = result["id"]
    time.sleep(8)  # let Instagram process the image

    # 2 — publish container
    resp = requests.post(
        f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media_publish",
        data={"creation_id": container_id, "access_token": IG_ACCESS_TOKEN},
    )
    result = resp.json()
    if "error" in result:
        logger.error(f"Instagram publish error: {result['error']}")
    else:
        logger.info(f"Instagram posted  id={result.get('id')}")
    return result


def post_to_twitter(image_path: Path, caption: str) -> dict:
    if not all([TWITTER_API_KEY, TWITTER_API_SECRET,
                TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET]):
        logger.warning("Twitter: credentials missing — skipping.")
        return {"status": "skipped"}

    try:
        import tweepy

        auth = tweepy.OAuth1UserHandler(
            TWITTER_API_KEY, TWITTER_API_SECRET,
            TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET,
        )
        api_v1 = tweepy.API(auth)
        media = api_v1.media_upload(filename=str(image_path))

        client = tweepy.Client(
            consumer_key=TWITTER_API_KEY,
            consumer_secret=TWITTER_API_SECRET,
            access_token=TWITTER_ACCESS_TOKEN,
            access_token_secret=TWITTER_ACCESS_SECRET,
        )
        # Twitter hard-limit: 280 chars
        tweet_text = caption[:277] + "..." if len(caption) > 280 else caption
        resp = client.create_tweet(text=tweet_text, media_ids=[media.media_id])
        logger.info(f"Twitter posted  id={resp.data['id']}")
        return {"id": resp.data["id"]}
    except Exception as exc:
        logger.error(f"Twitter error: {exc}")
        return {"error": str(exc)}


def post_to_linkedin(image_path: Path, caption: str) -> dict:
    if not LINKEDIN_ACCESS_TOKEN or not LINKEDIN_PERSON_ID:
        logger.warning("LinkedIn: credentials missing — skipping.")
        return {"status": "skipped"}

    headers = {
        "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
    }

    # 1 — register upload
    resp = requests.post(
        "https://api.linkedin.com/v2/assets?action=registerUpload",
        json={
            "registerUploadRequest": {
                "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"],
                "owner": f"urn:li:person:{LINKEDIN_PERSON_ID}",
                "serviceRelationships": [
                    {"relationshipType": "OWNER",
                     "identifier": "urn:li:userGeneratedContent"}
                ],
            }
        },
        headers=headers,
    )
    upload_data = resp.json()
    if "value" not in upload_data:
        logger.error(f"LinkedIn register error: {upload_data}")
        return upload_data

    upload_url = (
        upload_data["value"]["uploadMechanism"]
        ["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]
        ["uploadUrl"]
    )
    asset = upload_data["value"]["asset"]

    # 2 — upload binary
    with open(image_path, "rb") as f:
        requests.put(
            upload_url,
            data=f,
            headers={"Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}"},
        )

    # 3 — create post
    resp = requests.post(
        "https://api.linkedin.com/v2/ugcPosts",
        json={
            "author": f"urn:li:person:{LINKEDIN_PERSON_ID}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": caption},
                    "shareMediaCategory": "IMAGE",
                    "media": [
                        {
                            "status": "READY",
                            "description": {"text": "RS Cinema Villa"},
                            "media": asset,
                            "title": {"text": "RS Cinema Villa"},
                        }
                    ],
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            },
        },
        headers=headers,
    )
    result = resp.json()
    if "id" in result:
        logger.info(f"LinkedIn posted  id={result['id']}")
    else:
        logger.error(f"LinkedIn error: {result}")
    return result


def _photo_to_short(image_path: Path, output_path: Path, duration: int = 30) -> None:
    """Convert a still image to a 1080×1920 vertical MP4 (YouTube Shorts format)."""
    subprocess.run(
        [
            "ffmpeg", "-y",
            "-loop", "1",
            "-i", str(image_path),
            "-c:v", "libx264",
            "-t", str(duration),
            "-pix_fmt", "yuv420p",
            "-vf",
            "scale=1080:1920:force_original_aspect_ratio=decrease,"
            "pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black",
            "-r", "30",
            str(output_path),
        ],
        check=True,
        capture_output=True,
    )


def post_to_youtube(image_path: Path, title: str, description: str) -> dict:
    if not all([YOUTUBE_CLIENT_ID, YOUTUBE_CLIENT_SECRET, YOUTUBE_REFRESH_TOKEN]):
        logger.warning("YouTube: credentials missing — skipping.")
        return {"status": "skipped"}

    try:
        from google.oauth2.credentials import Credentials
        from googleapiclient.discovery import build
        from googleapiclient.http import MediaFileUpload

        creds = Credentials(
            token=None,
            refresh_token=YOUTUBE_REFRESH_TOKEN,
            client_id=YOUTUBE_CLIENT_ID,
            client_secret=YOUTUBE_CLIENT_SECRET,
            token_uri="https://oauth2.googleapis.com/token",
        )
        youtube = build("youtube", "v3", credentials=creds)

        with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as tmp:
            video_path = Path(tmp.name)

        _photo_to_short(image_path, video_path)

        media = MediaFileUpload(
            str(video_path), chunksize=-1, resumable=True, mimetype="video/mp4"
        )
        request = youtube.videos().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": title[:100],
                    "description": description,
                    "tags": [
                        "RSCinemaVilla", "CinemaVilla", "VillaStay",
                        "LuxuryVilla", "VacationRental", "Shorts",
                    ],
                    "categoryId": "22",
                    "defaultLanguage": "en",
                },
                "status": {
                    "privacyStatus": "public",
                    "selfDeclaredMadeForKids": False,
                },
            },
            media_body=media,
        )

        response = None
        while response is None:
            status, response = request.next_chunk()
            if status:
                logger.info(f"YouTube upload {int(status.progress() * 100)}% complete")

        video_path.unlink(missing_ok=True)
        logger.info(f"YouTube posted  id={response['id']}")
        return {"id": response["id"]}
    except Exception as exc:
        logger.error(f"YouTube error: {exc}")
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    log = load_log()

    try:
        photo_name = get_next_photo(log)
    except FileNotFoundError as exc:
        logger.error(str(exc))
        return

    photo_path = PHOTOS_DIR / photo_name
    image_url  = public_image_url(photo_name)
    caption    = generate_caption()
    yt_title   = "RS Cinema Villa — Luxury Villa Stay with Private Cinema | Book Now"

    logger.info(f"Today's photo : {photo_name}")
    logger.info(f"Public URL    : {image_url}")

    results: dict[str, dict] = {}
    results["facebook"]  = post_to_facebook(photo_path, caption)
    results["instagram"] = post_to_instagram(image_url, caption)
    results["twitter"]   = post_to_twitter(photo_path, caption)
    results["linkedin"]  = post_to_linkedin(photo_path, caption)
    results["youtube"]   = post_to_youtube(photo_path, yt_title, caption)

    # ---- update log ----
    log.setdefault("posted", []).append(photo_name)
    entry = {
        "photo": photo_name,
        "date":  datetime.now(timezone.utc).isoformat(),
        "results": {
            k: str(v.get("id") or v.get("status") or "error")
            for k, v in results.items()
        },
    }
    log["last_posted"] = entry
    log.setdefault("history", []).append(entry)
    save_log(log)

    logger.info("=== Daily post complete ===")
    for platform, result in results.items():
        ok = "id" in result or result.get("status") == "skipped"
        logger.info(f"  {platform:12s}: {'OK' if ok else 'FAILED'}")


if __name__ == "__main__":
    main()
