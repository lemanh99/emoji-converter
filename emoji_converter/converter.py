import html
import re

import emoji


def encode_with_xmlcharrefreplace(
        text,
        encoding="ascii"
):
    """
    Encode the input text using the specified encoding and replace any invalid or unencodable characters
    with XML character references.

    Args:
        text (str): The text to encode.
        encoding (str): The encoding to use (default is UTF-8).

    Returns:
        str: The encoded string with XML character references.
    """
    encoded_text = text.encode(encoding, "xmlcharrefreplace")
    return encoded_text.decode()


def convert_emoji_to_xml_text(
        message: str
):
    """
    Converts emoji in the input text to XML character references.

    Args:
        message (str): The text to convert.

    Returns:
        str: The converted text with emojis replaced by their XML character references.

    Description:
        The `convert_emoji_to_xml_text` function takes a text as input and replaces any emojis found in the text with
        their corresponding XML character references. It utilizes the `emoji.replace_emoji` function, passing in the
        input text and a replacement function. The replacement function,
        defined as `lambda chars, _: encode_with_xmlcharrefreplace(chars)`,
        encodes the emoji characters using the `encode_with_xmlcharrefreplace` function,
        which converts the emojis to their XML character reference representation.
        The resulting text is returned, with emojis replaced by their XML character references.

        If the input `text` is None, the function returns None.

    Example:
        message = "Hello! 😊"
        converted_text = convert_emoji_to_xml_text(message)
        print(converted_text)

        Output:
        Hello! &#128522;
    """
    if message is None:
        return None

    return emoji.replace_emoji(
        message,
        replace=lambda chars, _: encode_with_xmlcharrefreplace(chars)
    )


def convert_xml_to_emoji_text(
        xml_text: str
):
    """
    Converts XML character references in the input text to emojis.

    Args:
        xml_text (str): The text with XML character references to convert.

    Returns:
        str: The converted text with XML character references replaced by emojis.

    Description:
        The `convert_xml_to_emoji_text` function takes a text as input and replaces any XML character references
        found in the text with their corresponding emojis. It utilizes regular expressions to identify XML character
        references in the text. The `html.unescape` function is then used to decode the XML character references
        into their corresponding Unicode characters. Finally, the resulting text with emojis is returned.

        If the input `xml_text` is None, the function returns None.

    Example:
        xml_text = "Hello! &#128522;"
        converted_text = convert_xml_to_emoji_text(xml_text)
        print(converted_text)

        Output:
        Hello! 😊
    """
    if xml_text is None:
        return None

    emoji_pattern = re.compile(r"&#(\d+);")
    converted_text = emoji_pattern.sub(lambda m: chr(int(m.group(1))), xml_text)
    return html.unescape(converted_text)
