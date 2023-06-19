import emoji_converter


def test_emoji_converter():
    # Test case 1: Convert emojis to XML character references
    text = "Hello! 😊"
    converted_text = emoji_converter.convert_emoji_to_xml_text(text)
    expected_result = "Hello! &#128522;"
    assert converted_text == expected_result, f"Expected: {expected_result}, Got: {converted_text}"

    # Test case 2: Convert XML character references to emojis
    xml_text = "Hello! &#128522;"
    converted_text = emoji_converter.convert_xml_to_emoji_text(xml_text)
    expected_result = "Hello! 😊"
    assert converted_text == expected_result, f"Expected: {expected_result}, Got: {converted_text}"

    # Test case 3: Handle None input
    assert emoji_converter.convert_emoji_to_xml_text(None) is None
    assert emoji_converter.convert_xml_to_emoji_text(None) is None

    print("All test cases passed!")


if __name__ == "__main__":
    test_emoji_converter()
