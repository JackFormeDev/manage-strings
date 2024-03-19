class ManageStr:
    def __init__(self) -> None:
        self.attribute_error_output = "[{0} : Error] - You need a {1} object"

    def str_to_bytes(self, string: str) -> int:
        """
        This method will convert your string obj in bytes obj.\n
        Parameters:\n
        'string' parameter, the string object that you want to convert in bytes.
        """
        try:
            return string.encode()
        except AttributeError:
            return self.attribute_error_output.format(string, str)

    def bytes_to_str(self, byts: bytes) -> str:
        """
        This method will convert your bytes obj in string obj.\n
        Parameters:\n
        'byts' parameter, the bytes object that you want to convert in string.
        """
        try:
            return byts.decode()
        except AttributeError:
            return self.attribute_error_output.format(byts, bytes)

    def edit_strings(self, string: list, remove_char: list, new_char: list):
        """
        This method allow you to edit your string.\n
        Parameters:\n
        'string' parameter, the current string that you want to modify. A list object.\n
        'remove_char' parameter, it will remove these chars. A list object.\n
        'new_char' parameter, the new chars in place of the removed chars. A list object.\n\n
        -Example 1-\n
        manage_str.edit_strings(string=['hello'], remove_char=['ello'], new_char=['i'])\n

        It will return ['hi']\n
        -Example 2-\n
        manage_str.edit_strings(string=['hello', 'hi', 'cya'], remove_char=['ello', 'i', 'y'], new_char=['i', 'ello', 'i'])\n

        It will return ['hi', 'hello', 'cia']
        """
        try:
            dict_structure = {}
            x = 0
            for _ in string:
                dict_structure[x] = {
                    "string": string[x],
                    "remove_chars": remove_char[x],
                    "new_chars": new_char[x],
                }
                x += 1
            for key_str, values_str in dict_structure.items():
                static_string = values_str.get("string")
                remove_chars = values_str.get("remove_chars")
                new_chars = values_str.get("new_chars")
                new_string = static_string.replace(remove_chars, new_chars)
                dict_structure[key_str] = new_string
            from_dict_to_list = list(dict_structure.values())
            return from_dict_to_list

        except AttributeError:
            return self.attribute_error_output.format(string, list)

    def remove_spaces(self, string: str) -> str:
        """
        This method will remove all spaces in your string.\n
        Parameters:\n
        'string' parameter, the current string that you want to modify.
        """
        try:
            return string.replace(" ", "").strip()
        except AttributeError:
            return self.attribute_error_output.format(string, str)

    def remove_chars(self, string: str, remove_char: str) -> str:
        """
        This method allow you to remove chars from your string.\n
        Parameters:\n
        'string' parameter, the current string that you want to modify.\n
        'remove_char' parameter, it will remove all chars inside that.
        """
        try:
            remove_char_list = [char for char in remove_char]
            acceptable_char_list = [
                char for char in string if not char in remove_char_list
            ]
            return "".join(acceptable_char_list)

        except AttributeError:
            return self.attribute_error_output.format(string, str)

    def match(self, first_string: str, second_string: str) -> bool:
        """
        This method will match two strings.\n
        Parameters:\n
        'first_string' parameter, the first string.\n
        'second_string' parameter, the second string.
        """
        try:
            if first_string == second_string:
                return True
            else:
                return False
        except AttributeError:
            return self.attribute_error_output.format(first_string, str)

    def search(self, string: str, searched_char: str) -> str:
        """
        This method allow you to search chars trough your string.\n
        Parameters:\n
        'string' parameter, the string you parse.\n
        'searched_char' parameter, the char that you are searching.
        """
        try:
            char_in_str = False
            print(searched_char)
            print(string)
            if searched_char in string:
                print("...")
                position_char = string.index(searched_char)
                char_in_str = True
                return f"[Contains '{searched_char}' : {char_in_str} | Position '{searched_char}' : {position_char}]"
            else:
                return f"[Contains '{searched_char}' : {char_in_str}]"

        except:
            return self.attribute_error_output.format(string, str)

    def filter(self, string, filtered_string): ...


manage_str = ManageStr()