def encryption(char):
    encrypted = (123 * ord(char) + 18) % 256
    return encrypted

msg = '6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8' \
      '539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921'

ascii_table = [chr(x) for x in range(1,129)]

map = {encryption(element): element for element in ascii_table}
print(map)

sentence = [map[x] for x in bytes.fromhex(msg)]
print(''.join(sentence))
