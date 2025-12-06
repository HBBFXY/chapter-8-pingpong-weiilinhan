import random
def simulate_game(prob_a):
    """模拟一局比赛，prob_a是选手A每球获胜的概率"""
    score_a, score_b = 0, 0
    while True:
        # 模拟一球胜负
        if random.random() < prob_a:
            score_a += 1
        else:
            score_b += 1
        # 判断是否结束
        if (score_a >= 11 or score_b >= 11) and abs(score_a - score_b) >= 2:
            return 1 if score_a > score_b else 0

def simulate_match(prob_a):
    """模拟一场比赛（7局4胜）"""
    wins_a, wins_b = 0, 0
    while wins_a < 4 and wins_b < 4:
        if simulate_game(prob_a):
            wins_a += 1
        else:
            wins_b += 1
    return 1 if wins_a > wins_b else 0

def analyze_competition(prob_a, n_matches=1000):
    """分析n场比赛的结果"""
    a_wins = sum(simulate_match(prob_a) for _ in range(n_matches))
    print(f"选手A每球胜率{prob_a}时，{n_matches}场比赛获胜{round(a_wins/n_matches*100,2)}%")

analyze_competition(0.55)
