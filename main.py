import sys
from filtre import noirblanc, dilatation, floue

arg = sys.argv
premier_arg = arg[1]


if premier_arg == "dilatation":
    dilatation.en_dilatation()
elif premier_arg == "noir et blance":
    noirblanc.n_b()
elif premier_arg == "floue":
    floue.en_floue()
