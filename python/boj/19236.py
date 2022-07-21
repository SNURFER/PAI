import heapq
from typing import List


def solution(input):
    # dictionary for direction vector
    dir_dict = {
        1: [-1, 0],
        2: [-1, -1],
        3: [0, -1],
        4: [1, -1],
        5: [1, 0],
        6: [1, 1],
        7: [0, 1],
        8: [-1, 1]
    }
    max_sum = 0

    def getEatableList(row: int, col: int, dir: int, board: List[List[List[int]]]) -> List[List[int]]:
        if dir == 0:
            print("dir is zero")
        dir_vec = dir_dict[dir]
        row += dir_vec[0]
        col += dir_vec[1]

        ret_val = []
        while 0 <= row < 4 and 0 <= col < 4:
            # over 0 is fish, 0 is blank, -1 is shark.
            if board[row][col][0] > 0:
                ret_val.append([row, col])
            row += dir_vec[0]
            col += dir_vec[1]

        return ret_val

    def moveAllFish(board: List[List[List[int]]], num_queue: List[List[int]], temporal_move: {}):
        q_size = len(num_queue)
        for _ in range(q_size):
            fish_info = num_queue.pop(0)
            loc = fish_info[2: 4]
            dir = fish_info[1]
            val = fish_info[0]

            # if temporal moved history exists, update location
            if temporal_move.get(val):
                loc = temporal_move[val][0: 2]
                temporal_move.pop(val)

            dir_cnt = 0
            target_pos = []
            while dir_cnt < 8:
                # divide by 9 to rotate 360 degree
                target_vec = dir_dict[(dir + dir_cnt - 1) % 8 + 1]
                if 0 <= loc[0] + target_vec[0] < 4 and 0 <= loc[1] + target_vec[1] < 4 and board[loc[0] + target_vec[0]][loc[1] + target_vec[1]][0] > 0:
                    target_pos = [loc[0] + target_vec[0], loc[1] + target_vec[1]]
                    break
                dir_cnt += 1

            # if fish can't move
            if dir_cnt == 8:
                target_pos = loc

            # swap
            board[loc[0]][loc[1]], board[target_pos[0]][target_pos[1]] = \
                board[target_pos[0]][target_pos[1]], board[loc[0]][loc[1]]

            swapped_fish_val = board[loc[0]][loc[1]][0]
            temporal_move[swapped_fish_val] = loc
            num_queue.append([val, dir, target_pos[0], target_pos[1]])

        for fish in num_queue:
            if temporal_move.get(fish[0]):
                fish[2] = temporal_move.get(fish[0])[0]
                fish[3] = temporal_move.get(fish[0])[1]

    def dfs(board: List[List[List[int]]], num_queue: List[List[int]], sum_fish: int, shark_pos: List[int]):
        # step0: delete shark_pos in queue
        for _ in range(len(num_queue)):
            fish_info = num_queue.pop(0)
            if not fish_info[2: 4] == shark_pos:
                num_queue.append(fish_info)

        # step1: move all fish between #1 ~ #16 for once
        moveAllFish(board, num_queue, {})

        # return if there is nothing to eat
        fish_list = getEatableList(shark_pos[0], shark_pos[1], board[shark_pos[0]][shark_pos[1]][1], board)
        nonlocal max_sum
        if len(fish_list) == 0:
            # calculate max
            max_sum = max(sum_fish, max_sum)
            return

        # for loop eatable fish in shark pos
        for fish in fish_list:
            next_shark_pos = fish
            fish_val = board[fish[0]][fish[1]][0]
            sum_fish += fish_val
            board[shark_pos[0]][shark_pos[1]][0] = 0
            board[next_shark_pos[0]][next_shark_pos[1]][0] = -1

            dfs(board, num_queue, sum_fish, next_shark_pos)

            board[shark_pos[0]][shark_pos[1]][0] = -1
            board[next_shark_pos[0]][next_shark_pos[1]][0] = fish_val

    # setting data input
    # data = [list(map(int, input().split())) for _ in range(4)]
    data = input

    # tuning input
    # board[a][b] is pair of [value, direction] of position a, b and we will call fish_info
    # if value is -1, it's shark
    # if value is 0, it's blank
    temp = []
    board: List[List[List[int]]] = [[[0, 0]] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            board[i][j] = [data[i][2 * j], data[i][2 * j + 1]]
            # sort value with number in ascending order
            heapq.heappush(temp, [data[i][2 * j], data[i][2 * j + 1], i, j])

    sum_fish = 0

    # set first step
    next_shark_pos = [0, 0]
    sum_fish += board[next_shark_pos[0]][next_shark_pos[1]][0]
    # set shark
    ate_val = board[next_shark_pos[0]][next_shark_pos[1]][0]
    board[next_shark_pos[0]][next_shark_pos[1]][0] = -1
    # no need to update direction because previous dir equals next shark dir

    # init to queue
    # queue item is [val, dir, i, j]
    num_queue = []
    while temp:
        if ate_val == temp[0][0]:
            heapq.heappop(temp)
            continue
        num_queue.append(heapq.heappop(temp))

    dfs(board, num_queue, sum_fish, next_shark_pos)
    return max_sum


if __name__ == "__main__":
    input = [[7, 6, 2, 3, 15, 6, 9, 8],
             [3, 1, 1, 8, 14, 7, 10, 1],
             [6, 1, 13, 6, 4, 3, 11, 4],
             [16, 1, 8, 7, 5, 2, 12, 2]]
    print(solution(input))
