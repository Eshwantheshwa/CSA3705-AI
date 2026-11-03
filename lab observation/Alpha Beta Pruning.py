def alpha_beta(depth, index, maximizing, scores,
               alpha, beta, max_depth):

    if depth == max_depth:
        return scores[index]

    if maximizing:
        best = -999

        for child in range(2):
            value = alpha_beta(
                depth + 1, index * 2 + child,
                False, scores, alpha, beta, max_depth
            )

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = 999

        for child in range(2):
            value = alpha_beta(
                depth + 1, index * 2 + child,
                True, scores, alpha, beta, max_depth
            )

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best

scores = [3, 5, 2, 9, 12, 5, 23, 23]

result = alpha_beta(
    0, 0, True, scores, -999, 999, 3
)

print("Best value:", result)
