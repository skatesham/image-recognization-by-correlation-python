import sys

from src.recognizer_application import RecognizerApplication

if __name__ == "__main__":
    print(f"Arguments must be 3, actual count: {len(sys.argv) - 1} ")
    print("Arg(1): target image path")
    print("Arg(2): folder patterns")
    print("Arg(3): pattern format as .png")
    app = RecognizerApplication()
    target_filename_arg = None
    patterns_filename_arg = None
    if len(sys.argv) > 2:
        target_filename_arg = sys.argv[1]
    if len(sys.argv) > 3:
        patterns_filename_arg = sys.argv[2] + "{}" + sys.argv[3]

    if patterns_filename_arg is not None:
        answer = app.recognize(target_filename_arg, patterns_filename_arg)
        print(f"Result= {answer}")
