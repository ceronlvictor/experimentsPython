def calc_bayes(prior_a, prob_b_dado_a, prob_b):
    return (prior_a * prob_b_dado_a) / prob_b

if __name__ == '__main__':
    #estabelcemos las probibilidades de cada una 
    prob_cancer = 1 / 100000
    prob_sintpma_dado_cancer = 1
    prob_sintoma_dado_no_cancer = 10 / 99999
    prob_no_cancer = 1 - prob_cancer

    prob_sintoma = (prob_sintpma_dado_cancer * prob_cancer) + (prob_sintoma_dado_no_cancer * prob_no_cancer)

    prb_cancer_dado_sintoma = calc_bayes(prob_cancer, prob_sintpma_dado_cancer, prob_sintoma)
    print(prb_cancer_dado_sintoma)