import math
def SPL_to_sone(freq,loudness):
  float(freq)
  float(loudness)
  if freq > 30 and freq <= 60:
    af = 0.432
    Lu = -15.9
    Tf = 44
  elif freq > 60 and freq <= 80:
    af = 0.409
    Lu = -13
    Tf = 37.5
  elif freq > 80 and freq <= 125:
    af = 0.349
    Lu = -6.2
    Tf = 22.1
  elif freq > 125 and freq <= 200:
    af = 0.330
    Lu = -4.5
    Tf = 17.9
  elif freq > 200 and freq <= 300:
    af = 0.301
    Lu = -2
    Tf = 11.4
  elif freq > 300 and freq <= 500:
    af = 0.276
    Lu = -0.1
    Tf = 6.2
  elif freq > 500 and freq <= 800:
    af = 0.259
    Lu = 0.3
    Tf = 3
  elif freq > 800 and freq <= 1200:
    af = 0.250
    Lu = 0
    Tf = 2.4
  elif freq > 1200 and freq <= 1500:
    af = 0.246
    Lu = -2.7
    Tf = 3.5
  elif freq > 1500 and freq <= 1800:
    af = 0.244
    Lu = -4.1
    Tf = 1.7
  elif freq > 1800 and freq <= 2200:
    af = 0.243
    Lu = -1
    Tf = -1.3
  elif freq > 2200 and freq <= 2900:
    af = 0.243
    Lu = 1.7
    Tf = -4.2
  elif freq > 2900 and freq <= 3500:
    af = 0.243
    Lu = 2.5
    Tf = -6
  elif freq > 3500 and freq <= 4500:
    af = 0.242
    Lu = 1.2
    Tf = -5.2
  elif freq > 4500 and freq <= 5500:
    af = 0.242
    Lu = -2.1
    Tf = -1.5
  elif freq > 5500 and freq <= 7500:
    af = 0.245
    Lu = -7.1
    Tf = 6
  elif freq > 7500 and freq <= 9000:
    af = 0.245
    Lu = -11.2
    Tf = 12.6
  elif freq > 9000 and freq <= 11000:
    af = 0.271
    Lu = -10.7
    Tf = 13.9
  elif freq > 11000:
    af = 0.301
    Lu = -3.1
    Tf = 12.3

  Bf2 = ((0.4 * (10 ** (((loudness + Lu) / 10) - 9))) ** af) - (
          0.4 * (10 ** (((Tf + Lu) / 10) - 9)) ** af + 0.005135)
  if Bf2 > 0:
    Phlf2 = 40 * math.log10(Bf2) + 94
    return 2 ** (0.1 * Phlf2 - 4)
  else:
    return 0
#print(SPL_to_sone(100,80))