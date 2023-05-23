def keycode_to_key(keycode):
    # Map of special characters
    special_chars = {
        8: "<BACKSPACE>",
        9: "<TAB>",
        13: "<ENTER>",
        16: "<SHIFT>",
        17: "<CTRL>",
        18: "<ALT>",
        20: "<CAPSLOCK>",
        27: "<ESCAPE>",
        32: "<SPACE>",
        46: "<DELETE>",
        190: "<.>"
        # Add any other special characters you're interested in
    }
    return special_chars.get(keycode, chr(keycode))