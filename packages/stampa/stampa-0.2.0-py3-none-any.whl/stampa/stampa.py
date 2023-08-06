from datetime import datetime


class Stamp:

    """Gets date time as string without spaces"""


    def __init__(self, desired) -> None:

        """Init stamp and stamp dictionary"""

        stamp = (str(datetime.now())
                    .replace(" ", "")
                    .replace(".","").
                    replace(":","")
                    .replace("-","")
                    )


        available = {
            "stamp":stamp,
            "sec":stamp[0:14],
            "min":stamp[0:12],
            "hour":stamp[0:10],
            "day":stamp[0:8],
            "month":stamp[0:6],
            "year":stamp[0:4]
            }

        try:
            self.desired = available[desired]

        except KeyError:
            self.desired = f"Error : {desired} is not available, wrong input"


    def __repr__(self) -> None:

        """Returns text representaion"""

        return f"{self.desired}"
