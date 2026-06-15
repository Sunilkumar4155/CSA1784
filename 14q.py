def minimax_alpha_beta(depth, node_idx, is_max, scores, alpha, beta, h):
    if depth == h:
        return scores[node_idx]
    if is_max:
        best = float('-inf')
        for i in range(2):
            val = minimax_alpha_beta(depth+1, node_idx*2+i, False, scores, alpha, beta, h)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax_alpha_beta(depth+1, node_idx*2+i, True, scores, alpha, beta, h)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

scores = [3, 5, 6, 9, 1, 2, 0, -1]
print("Optimal value:", minimax_alpha_beta(0, 0, True, scores, float('-inf'), float('inf'), 3))
