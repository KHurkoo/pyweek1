import sys

import main
MIN_VER = (3, 9)

if sys.version_info[:2] < MIN_VER:
    sys.exit("This game requires Python {}.{}.".format(*MIN_VER))
else:
    main()