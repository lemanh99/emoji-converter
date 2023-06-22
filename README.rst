Emoji converter
------
.. image:: https://github.com/lemanh99/emoji-converter/actions/workflows/test.yml/badge.svg
    :target: https://github.com/lemanh99/emoji-converter/actions/workflows/test.yml

A Python package for converting emojis to text and text to emojis.

======================================================

## Example

.. code-block:: python

    import emoji_converter
    
    # Convert emoji to text
    emoji_text = emoji_converter.convert_emoji_to_text("Hello! 😊")
    print(emoji_text)  # Output: Hello! &#128522;
    
    # Convert text to emoji
    text_emoji = emoji_converter.convert_text_to_emoji("Hello! &#128522")
    print(text_emoji)  # Output: Hello! 😊


License
--------
This project is licensed under the MIT License. See the LICENSE file for more information.

