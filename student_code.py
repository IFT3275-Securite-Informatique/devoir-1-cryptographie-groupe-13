# Équipe 13
# Nikolas Lévesque (20276665) et Abdelmouhcine Messaad (2151011)

import random
from collections import Counter
import math

def decrypt(C):
    M = ""
    # fréquences des lettres
    frequences_lettres = {
        'e': 14.7155, 'a': 7.6364, 'i': 7.5290, 's': 7.9488, 't': 7.2443,
        'n': 7.0955, 'r': 6.5537, 'u': 6.3114, 'l': 5.4564, 'o': 5.3784,
        'd': 3.6695, 'm': 2.9680, 'p': 2.5210, 'c': 3.2606, 'v': 1.6286,
        'q': 1.3622, 'f': 1.0667, 'b': 0.9011, 'g': 0.8664, 'h': 0.7372,
        'j': 0.6134, 'x': 0.4273, 'y': 0.1285, 'z': 0.3264, 'k': 0.0497,
        'w': 0.1140
    }

    # fréquences des bigrammes
    frequences_bigrams = {
        'es': 3.59, 'de': 2.97, 'en': 2.55, 'on': 2.36, 'le': 2.32,
        'et': 2.26, 'la': 2.02, 'ou': 1.99, 'an': 1.90, 're': 1.89,
        'er': 1.85, 'me': 1.75, 'nt': 1.72, 'te': 1.71, 'se': 1.66,
        'el': 1.61, 'ne': 1.57, 'ce': 1.52, 'ra': 1.50, 'qu': 1.48,
        'ai': 1.47, 'il': 1.43, 'it': 1.42, 'ue': 1.41, 'le': 1.40,
        'is': 1.38, 'au': 1.37, 'ar': 1.36, 'in': 1.35, 've': 1.34,
        'to': 1.32, 'sa': 1.30, 'ou': 1.28, 'ur': 1.26, 'al': 1.25,
        'ma': 1.24, 'ir': 1.23, 'pe': 1.22, 'ro': 1.21, 'si': 1.20,
        'di': 1.19, 'ta': 1.18, 'la': 1.17, 'li': 1.16, 'pa': 1.15,
        'te': 1.14, 'po': 1.12, 'jo': 1.11, 'co': 1.10, 'so': 1.09,
        'mo': 1.08, 'no': 1.07, 'av': 1.06, 'bi': 1.05, 'ci': 1.04,
        'en': 1.03, 'bl': 1.02, 'do': 1.01, 'va': 1.00
    }

    # fréquences des trigrammes
    frequences_trigrams = {
        'ent': 1.07, 'les': 0.89, 'des': 0.79, 'ion': 0.73, 'men': 0.72,
        'eme': 0.69, 'est': 0.68, 'que': 0.65, 'our': 0.64, 'par': 0.63,
        'ons': 0.61, 'que': 0.60, 'ous': 0.59, 'ait': 0.58, 'eur': 0.57,
        'ant': 0.56, 'and': 0.55, 'ont': 0.54, 'res': 0.53, 'com': 0.52,
        'ver': 0.51, 'con': 0.50, 'une': 0.49, 'ais': 0.48, 'pro': 0.47,
        'tra': 0.46, 'ell': 0.45, 'sta': 0.44, 'est': 0.43, 'ist': 0.42,
        'nes': 0.41, 'ale': 0.40, 'ers': 0.39, 'lle': 0.38, 'san': 0.37,
        'sur': 0.36, 'nes': 0.35, 'ite': 0.34, 'art': 0.33, 'que': 0.32,
        'ine': 0.31, 'nce': 0.30, 'ont': 0.29, 'lle': 0.28, 'uni': 0.27,
        'sou': 0.26, 'ite': 0.25, 'mon': 0.24, 'ill': 0.23, 'rat': 0.22,
        'sou': 0.21, 'ter': 0.20, 'cha': 0.19, 'ren': 0.18, 'nti': 0.17,
        'lle': 0.16, 'pli': 0.15, 'ons': 0.14, 'sis': 0.13, 'nes': 0.12,
        'our': 0.11, 'fin': 0.10, 'ran': 0.09, 'mai': 0.08, 'eme': 0.07
    }

    # charger le dictionnaire de mots français french_dictionary.txt
    def load_french_dictionary():
        with open('french_dictionary.txt', 'r', encoding='utf-8') as f:
            french_words = set(word.strip().lower() for word in f)
        return french_words

    # fonctions auxiliaires
    def count_frequencies(text):
        total = len(text)
        frequencies = Counter(text)
        return {char: count / total * 100 for char, count in frequencies.items()}

    def get_ngrams(text, n):
        return [text[i:i+n] for i in range(len(text)-n+1)]

    def initialize_mapping(freq_ciphertext, freq_french):
        sorted_cipher = [item[0] for item in sorted(freq_ciphertext.items(), key=lambda x: x[1], reverse=True)]
        sorted_french = [item[0] for item in sorted(freq_french.items(), key=lambda x: x[1], reverse=True)]
        mapping = dict(zip(sorted_cipher, sorted_french))
        return mapping

    def score_mapping(mapping, ciphertext, bigram_freqs, trigram_freqs, french_words):
        decrypted_text = ''.join([mapping.get(c, '?') for c in ciphertext])
        score = 0

        # score basé sur les bigrammes
        bigrams = get_ngrams(decrypted_text, 2)
        for bg in bigrams:
            if bg in bigram_freqs:
                score += bigram_freqs[bg]
            else:
                score -= 1  # pénalité pour les bigrammes inconnus

        # score basé sur les trigrammes
        trigrams = get_ngrams(decrypted_text, 3)
        for tg in trigrams:
            if tg in trigram_freqs:
                score += trigram_freqs[tg]
            else:
                score -= 1  # pénalité pour les trigrammes inconnus

        # score basé sur les mots valides
        words = decrypted_text.split()
        valid_word_count = sum(1 for word in words if word in french_words)
        score += valid_word_count * 5 # on peut modifier le facteur plus tard si jamais

        return score

    def swap_two_letters(mapping):
        letters = list(mapping.keys())
        a, b = random.sample(letters, 2)
        new_mapping = mapping.copy()
        new_mapping[a], new_mapping[b] = new_mapping[b], new_mapping[a]
        return new_mapping

    def decrypt_with_mapping(mapping, ciphertext):
        return ''.join([mapping.get(c, '?') for c in ciphertext])

    def optimize_mapping(ciphertext, initial_mapping, bigram_freqs, trigram_freqs, french_words):
        current_mapping = initial_mapping.copy()
        current_score = score_mapping(current_mapping, ciphertext, bigram_freqs, trigram_freqs, french_words)
        best_mapping = current_mapping.copy()
        best_score = current_score

        temperature = 1000.0
        cooling_rate = 0.0001

        for iteration in range(100000):
            new_mapping = swap_two_letters(current_mapping)
            new_score = score_mapping(new_mapping, ciphertext, bigram_freqs, trigram_freqs, french_words)
            delta_score = new_score - current_score

            if delta_score > 0 or random.uniform(0, 1) < math.exp(delta_score / temperature):
                current_mapping = new_mapping
                current_score = new_score

                if new_score > best_score:
                    best_mapping = new_mapping
                    best_score = new_score
                    print(f"Iteration {iteration}: New best score {best_score}")

            temperature = temperature / (1 + cooling_rate * iteration)
            if temperature < 0.1:
                break

        return best_mapping

    # charger le dictionnaire
    french_words = load_french_dictionary()

    # nettoyer le cryptogramme pour avoir que les lettres
    ciphertext = ''.join([c for c in C.lower() if c.isalpha()])

    # compter les fréquences des caractères dans le cryptogramme
    freq_ciphertext = count_frequencies(ciphertext)

    # initialiser le mapping
    initial_mapping = initialize_mapping(freq_ciphertext, frequences_lettres)

    # optimiser le mapping
    best_mapping = optimize_mapping(ciphertext, initial_mapping, frequences_bigrams, frequences_trigrams, french_words)

    # décrypter le message avec le meilleur mapping
    M = decrypt_with_mapping(best_mapping, ciphertext)
    return M
