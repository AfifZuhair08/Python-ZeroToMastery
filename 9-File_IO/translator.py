from translate import Translator

translator = Translator(to_lang="de")

try:
    with open("my_file.txt", mode="r") as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        # print(translation)
        with open("my_file_german.txt", mode="w") as my_file_translate:
            my_file_translate.write(translation)
except FileNotFoundError as e:
    print("Check your file path")