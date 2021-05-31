# This function returns a DNA sequence padded with indels in order for the sequence to be the same length
# as the other DNA sequence, which is longer in this case. num is the difference between the 
# larger and shorter sequence. The function pads the shorter DNA sequence with indels based on num.
def pad_with_indels(sequence, num):
    return sequence + "-" * num


# This function keeps an acculumator of how many characters match in every position of the sequences.
# It doesn't account for indels because they're just a placeholder to keep the strings the same length.
def count_matches(sequence1, sequence2):
    accumulator = 0
    for i in range(len(sequence1)):
        if sequence1[i] == sequence2[i]:
            accumulator += 1

            if sequence1[i] == "-" and sequence2[i] == "-":
                accumulator -= 1
    
    return accumulator 


def count_mismatches(sequence1, sequence2):
    accumulator = 0
    for i in range(len(sequence1)):
        if sequence1[i] != sequence2[i]:
            accumulator += 1
    
    return accumulator

# This function takes a DNA sequence inputted by the user and compares each character in the string 
# with another sequence. It checks to see if they are equal to each other to determine if 
# they need to be lowercased or stay the same (Assuming the entire string is capitalized).
# It returns the modified string.
def change_sequence1(seq1, seq2):
    seq1_changed = ""
    seq1.lower()
    seq2.lower()
    for i in range(len(seq1)):
        seq1[i].lower()
        if seq1[i] == seq2[i]:
            seq1_changed += seq1[i].lower()

        else:
            seq1_changed += seq1[i].upper()

    return seq1_changed


def change_sequence2(seq1, seq2):
    matchcount = ""
    seq1.lower()
    seq2.lower()
    for i in range(len(seq2)):
        if seq1[i] == seq2[i]:
            matchcount += seq2[i].lower()

        else:
            matchcount += seq2[i].upper()

    return matchcount


# This function inserts indels in the sequence at that given position and 
# shifts everything else right.
def insert_indel(sequence, index):
    if index == len(sequence):
        sequence_indel = sequence + "-"

    else:
        sequence_first_half = sequence[0:index]
        sequence_second_half = sequence[index: ]
        sequence_indel = sequence_first_half + "-" + sequence_second_half
    
    return sequence_indel


if __name__ == "__main__":
    DNAsequence1 = input("Please enter DNA Sequence 1: ")
    DNAsequence2 = input("Please enter DNA Sequence 2: ")

    print()
    # The if and else statement compares the total lengths of the 2 DNA sequence to determine 
    # which sequence is shorter to adjust it with indels.
    if len(DNAsequence1) < len(DNAsequence2):

        # DNA_indels_pad determines the difference between the two lengths of DNA sequence.
        # It calls the pad_with_indels function and modifies the shorter sequence to include indels. 
        DNA_indels_pad = pad_with_indels(DNAsequence1, len(DNAsequence2) - len(DNAsequence1))

        # It calls the change_sequence function and assigns seq1_letter_change with the new modified string.
        seq1_letter_change = change_sequence1(DNA_indels_pad, DNAsequence2) 
        seq2_letter_change = change_sequence2(DNA_indels_pad, DNAsequence2) 

        print("Sequence 1: ", seq1_letter_change)
        print("Sequence 2: ", seq2_letter_change)

        # Taking 2 modified sequences and sending them to the count_match function to count how many characters match in each position.
        matchcount = count_matches(seq1_letter_change, seq2_letter_change)
        
        
    else:
        DNA_indels_pad = pad_with_indels(DNAsequence2, len(DNAsequence1) - len(DNAsequence2))

        seq1_letter_change = change_sequence1(DNAsequence1, DNA_indels_pad)
        seq2_letter_change = change_sequence2(DNAsequence1, DNA_indels_pad)

        print("Sequence 1:", seq1_letter_change)
        print("Sequence 2:", seq2_letter_change)
        
        matchcount = count_matches(seq1_letter_change, seq2_letter_change)


    print()

    # This print statement prints all the number of matching characters. 
    # Mismatch is found by subtracting the total length of DNA_indels_pad with matchcount because it assumes everything else is a mismatch.
    print(f"Similarity: {matchcount} matches, {len(DNA_indels_pad) - matchcount} mismatches. {((matchcount / len(DNA_indels_pad)) * 100):0.1f}% match rate.")

    print() 
    indel_location = int(input( "Please enter an indel location for Sequence 1: "))

    print()
    
    # It calls the insert_indel function and takes the argument of seq1_letter_change and indel_location and puts an indel at that position minus 1.
    # Subtracting indel_location by 1 is important because the user inputs a position that starts at 1 instead of 0.
    seq1_modified = insert_indel(seq1_letter_change, indel_location - 1)

    seq2_modified = pad_with_indels(seq2_letter_change, len(seq1_modified) - len(seq2_letter_change))


    seq1_edit = change_sequence1(seq1_modified, seq2_modified)
    seq2_edit = change_sequence2(seq1_modified, seq2_modified)

    print(f"Sequence 1: {seq1_edit}")
    print(f"Sequence 2: {seq2_edit}")

    print()

    matchcount = count_matches(seq1_edit, seq2_edit)

    print(f"Similarity: {matchcount} matches, {len(seq1_edit) - matchcount} mismatches. {((matchcount / len(seq1_edit)) * 100):0.1f}% match rate.")


    
