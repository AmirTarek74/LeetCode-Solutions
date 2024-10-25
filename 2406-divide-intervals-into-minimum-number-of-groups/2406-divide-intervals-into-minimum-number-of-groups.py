class Solution:
    def minGroups(self,intervals):
        """
        Divides intervals into groups with no intersections within a group.

        Args:
          intervals: A list of lists, where each inner list represents an interval [start, end].

        Returns:
          The minimum number of groups required.
        """

        if not intervals:
            return 0

        # Separate start and end points
        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])

        groups = 0
        end_ptr = 0  # Pointer for the 'ends' array

        for start in starts:
            if start <= ends[end_ptr]:
                # Overlap: Need a new group
                groups += 1
            else:
                # No overlap: Reuse a group (move 'end_ptr')
                end_ptr += 1

        return groups