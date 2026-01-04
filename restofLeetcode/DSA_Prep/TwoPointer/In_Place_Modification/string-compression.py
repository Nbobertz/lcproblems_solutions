"""
This is to compress a string
"""

i = 0          # pointer to read characters
        write = 0      # pointer to write compressed output

        while i < len(chars):
            curr = chars[i]
            count = 0

            # count consecutive characters
            while i < len(chars) and chars[i] == curr:
                i += 1
                count += 1

            # write the character
            chars[write] = curr
            write += 1

            # write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
