from .config import verbose

def failed(skk): print("\033[91m[FAILED] \033[00m{}".format(skk))
def passed(skk): print("\033[92m[PASSED] \033[00m{}".format(skk))


def notify(skk):
    if verbose:
        print("\033[96m[NOTIFY] \033[00m{}".format(skk))