class Translation(object):
    START_TEXT = """<b>Hello {},
    
🕹I'm URL X Uploader Bot📌!, Made by @FILMWORLDOFFICIA 

🌀This bot is owned and maintained by @FILMWORofficial

💫This is a public bot so any one can use this

🎲I can Upload URL links as Telegram Files, Documents or audio. 

🍿Send me any Direct Download link.

🎯Send Only One Link at a Time.

😎I can upload to telegram as File or Video or Audio(if supported) format.
Click /help for more details!

Movie channel🎥 - @FILMWORofficial
\n</b>"""
    FORMAT_SELECTION = "<b>✅Select the desired format: <a href='{}'>file size might be approximate.</a> \n🧭If you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\n😎You can use /delthumbnail to delete the auto-generated thumbnail.</b>"
    SET_CUSTOM_USERNAME_PASSWORD = """<b>🤠If you want to download premium videos, provide in the following format:
URL | filename | username | password </b>"""
    DOWNLOAD_START = "⏳"
    UPLOAD_START = "💫"
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "<b>😎Mission Accomplished</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "<b>🍿Downloaded and Uploaded the file.\n🤠Now Enjoy @JikURLBot 😎</b>"
    SAVED_CUSTOM_THUMB_NAIL = "<b>🤠Custom thumbnail saved. This image will be used as Thumbnail.</b>"
    DEL_ETED_CUSTOM_THUMB_NAIL = "<b>✅ Custom Thumbnail cleared Succesfully.</b>"
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    HELP_USER = """<b>🎯It's very simple to use me.\n🎨Just follow the steps.
    
🧁Send url (Link|New Name+Extension).

🧭Send Custom Thumbnail [Optional]

🧰Select the desired Button.

🎰SVideo - Give File as video with Screenshots

🧯DFile - Give File with Screenshots

🎸Video - Give File as video without Screenshots

🛰️File - Give File without Screenshots

🎲If the Bot didn't respond, 

🌀Contact: @FILMWORLDOFFICIA
\n</b>"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
You can use /rename command after receiving file to rename it with custom thumbnail support.
"""
    CANCEL_STR = "<b>❌Process Cancelled❌</b>"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
