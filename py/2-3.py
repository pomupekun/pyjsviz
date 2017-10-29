# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

# A
student_data = [
    {"name": "bob", "id": 0, "scores": [68, 75, 56, 81]},
    {"name": "alice", "id": 1, "scores": [75, 90, 64, 88]},
    {"name": "carol", "id": 2, "scores": [59, 74, 71, 68]}
]


# B
def process_student_data(data, pass_threshold=60, merit_threshold=75):
    """data[scores]の平均を表示"""

    # C
    for sdata in data:
        logger.debug(sdata["name"])
        print("sum", sdata["scores"])
        length = float(len(sdata["scores"]))
        print("len", length)
        av = sum(sdata["scores"]) / float(len(sdata["scores"]))
        sdata["average"] = av
        logger.info("average" + str(av))

        if av > merit_threshold:
            sdata["assessment"] = "passed with merit"
        elif av > pass_threshold:
            sdata["assessment"] = "passed"
        else:
            sdata["assessment"] = "failed"

        # D
        print("%s's (id: %d) final assessment is: %s" %(
            sdata["name"],
            sdata["id"],
            sdata["assessment"].upper())
        )


# E
if __name__ == "__main__":
    process_student_data(student_data)
