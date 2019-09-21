from armsegment import ArmSegment


MAXTRIES = 1000
SUCCESS_THRESHOLD = 0.1


def segmentatdest(seg, d):
    pos = seg.getPos()
    return d[0] + SUCCESS_THRESHOLD > pos[0] > d[0] - SUCCESS_THRESHOLD and d[1] + SUCCESS_THRESHOLD > pos[1] > d[1] - SUCCESS_THRESHOLD


a0 = ArmSegment(0, 0, 0)
a1 = ArmSegment(90, 15, 1, a0)
a2 = ArmSegment(0, 18, 2, a1)
a3 = ArmSegment(0, 16, 3, a2)

segments = [a0, a1, a2, a3]

dest = (45, 15, 0)

i = 0
seg = len(segments) - 2
while not segmentatdest(a3, dest) and i < MAXTRIES:
    segments[seg].moveto(dest)
    seg -= 1
    if seg == -1:
        seg = len(segments) - 2
    i += 1

print(i)
