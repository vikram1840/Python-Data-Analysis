# $language = "python"
# $interface = "1.0"

# Connect to an SSH server using the SSH2 protocol. Specify the
# username and password and hostname on the command line as well as
# some SSH2 protocol specific options.

import datetime
from datetime import date, timedelta




def main():
    host = "187.100.32.94:8022"
    user_name = "f008869"
    password = "Amdocs@123"
    session_name = "f008869@RJBAR-OSWHPP-SRA04"
    cmd = "/SSH2 /L " + session_name + " /PASSWORD " + password + " " + host
    crt.Session.Connect(cmd)
    # crt.Screen.WaitForString("Prompt from dialog that is now in terminal window")
    # crt.Screen.Send("Response")
    # if crt.Session.Connected:
    crt.Screen.Synchronous = True
    row = crt.Screen.CurrentRow
    prompt = crt.Screen.Get(row, 0, row, crt.Screen.CurrentColumn - 1)
    prompt = prompt.strip()
    crt.Screen.Send("cd EM_ITFORUM\n")
    crt.Screen.WaitForString(prompt)
    crt.Screen.Send("./Iub.sh\n")
    crt.Screen.Send("1\n")
    crt.Screen.WaitForString(prompt)
    crt.Screen.Send("cd Iub_output\n")
    crt.Screen.WaitForString(prompt)
    crt.Screen.Send("cat Iub_output.txt\n")
    crt.Screen.WaitForString(prompt)
    # crt.Screen.Send("./emnode.sh\n")
    # crt.Screen.Send("1\n")
    # crt.Screen.WaitForString(prompt)
    # crt.Screen.WaitForString("nkacops@rjoswsra04>")


main()
