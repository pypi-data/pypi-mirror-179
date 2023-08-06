# intobot

This tool can turn your script into a VK bot. In every script launched with this tool, `input` and `print` will work with chats instead of the console. A script is ran one time for every user who writes to the bot. First message from a user starts the script execution and cannot be received from the script.

Installation:

    pip install intobot

Use it like this:

    python -m intobot -t [token_file_name.txt] [script_name].py

Everything above that is in brackets needs to be filled by you. (Brackets should be omitted.)

When the script ends, the user is not served anymore, so to serve the user infinitely, add an infinite loop to the script. This was made to allow better flexibility and make it as close to console execution of scripts as possible.

[Predecessor: every_script_is_a_vk_bot](https://github.com/megahomyak/every_script_is_a_vk_bot)
