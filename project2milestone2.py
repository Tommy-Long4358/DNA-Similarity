# Project 2 Milestone 2
# Christopher Pineda and Tommy Long

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


# This function takes a DNA sequence inputted by the user and compares each character in the string 
# with another sequence. It checks to see if they are equal to each other to determine if 
# they need to be lowercased or stay the same (Assuming the entire string is capitalized).
# It returns the modified string.
def change_sequence1(seq1, seq2):
    seq1_changed = ""
    seq1_low = seq1.lower()
    seq2_low = seq2.lower()

    for i in range(len(seq1_low)):
        if seq1_low[i] == seq2_low[i]:
            seq1_changed += seq1_low[i].lower()

        else:
            seq1_changed += seq1_low[i].upper()

    return seq1_changed


def change_sequence2(seq1, seq2):
    seq2_changed = ""
    seq1_lower = seq1.lower()
    seq2_low = seq2.lower()

    for i in range(len(seq2_low)):
        if seq1_lower[i] == seq2_low[i]:
            seq2_changed += seq2_low[i].lower()

        else:
            seq2_changed += seq2_low[i].upper()

    return seq2_changed


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


# This function prints the main menu for the user to see what options they can input as a number.
def print_menu():
    print( "Main Menu")
    print( "1. Insert an indel")
    print( "2. Remove an indel")
    print( "3. Score similarity")
    print( "4. Suggest indel")
    print( "5. Quit")


# This function valids that the input the user puts is between 1 and 5.
# It returns the validated option.
def get_menu_choice():
    option = int(input("Please choose an option: "))

    while option < 0 or option > 5:
        option = int(input("Please choose an option: "))

    return option


# This function is similar to get_menu_choice(), but it checks for a number between 1 and 2.
# It returns the validated sequence choice that the user wants.
def get_sequence_number():
    sequence_choice = int(input("Sequence 1 or 2? "))

    while sequence_choice < 1 or sequence_choice > 2:
        sequence_choice = int(input("Sequence 1 or 2? "))

    return sequence_choice


# This function validates that the position the user inputs is inbetween 1 and the total length of the sequence.
# It returns the position of our validated choice.
def get_insert_position(sequence):
    position_choice = int(input("Please choose a position: "))

    while position_choice < 1 or position_choice > len(sequence):
        position_choice = int(input("Please choose a position: "))

    return position_choice


# The get_remove_position function gets a position from the user and makes sure
# it is in the range of zero to the total length of the sequence. It tests 0 as a special
# case because we wouldn't be able to use the index of that position since its -1 and 
# sequence[-1] is the last index in the sequence. This function returns a position that has an indel.
def get_remove_position(sequence):
    position = int(input("Please choose a position: "))
    
    while position < 0 or position > len(sequence):
       position = int(input("Please choose a position: "))
    
    else:
        if position == 0:
            if sequence[position] == "-":
                return position
                
            else:
                position = int(input("Please choose a position: "))

        # With DeMorgan's laws, the while loop tests if its first outside the range so that it's not included
        # into finding the index for it. 
        while position < 0 or position > len(sequence) or sequence[position - 1] != "-":
            position = int(input("Please choose a position: "))

    return position 

# THE BETTER SOLUTION
def get_remove_position(sequence):
    position = int(input("Please choose a position: "))
    x = 0
    sequence_split = []
    for i in range(len(sequence)):

        if sequence[i] == "-":
            sequence_split.append(i)

    
    while x == 0:
        if position in sequence_split:
            x += 1
            return position
        else:
            position = int(input("Please choose a position: "))


# This function slices the sequence into 2 parts and leaving out the indel at that index.
# It combines the sliced sequences and returns the modified removed sequence.
def remove_indel(sequence,index):
    sequence_first_half = sequence[0:index]

    sequence_second_half = sequence[index + 1:: ]
    # In sequence_second_half, we add the index by 1 to exclude the indel and by doing so, 
    # it only prints out everything past index plus 1.

    sequence_indel = sequence_first_half + sequence_second_half
    
    return sequence_indel


# This function serves the purpose of adjusting both sequences to the same length, excluding the last index.
# It returns everything up until the 2nd to last index.
def indel_modify(sequence):
    return sequence[:-1]

# This function goes through every position in the sequence and inserts an indel at that position to see how many 
# matches and mistmatches the sequence has. In order to find the biggest number of matches, it returns the position 
# that had the most optimal outcome. If there are two optimal locations equal to each other, it returns the first instance instead.
def optimal_indel_position(sequence, other_sequence):
    max_matches = 0
    optimal_position = 0
    seq1_indel = sequence

    # This for loop uses brute force because it will go through 
    # every single index in the sequence to compare each outcome
    for i in range(len(sequence)):
        seq1_modified = insert_indel(seq1_indel, i)
        # seq1_modified calls insert_indel() to insert an indel in seq1_indel at what ever index "i" is at.

        seq2_modified = pad_with_indels(other_sequence, len(seq1_modified) - len(other_sequence))
        # Because seq1_indel has an indel added to its sequence, other_sequence needs to be the 
        # same langth as seq1_indel, so it calls pad_with_indels to add as many indels it 
        # needs to have other_sequence be equal in length to seq1_indel.

        matches = count_matches(seq1_modified, seq2_modified)
        # Matches calls the count_matches function to compare how many matches seq1_modified shares with seq2_modified.

        # The if statement compares the number of matches that position "i" has in seq1_indel
        # If this "position" is greater than the previous "position" in matches, it assigns max_matches the current number of matches.
        # For optimal_position, it is assigned that current position that has the biggest number of matches.
        if matches > max_matches:
            max_matches = matches
            optimal_position = i
    
    # This resets the sequence back to the original sequence so that it can test the other positions where an indel needs to be placed.
    seq1_indel = sequence
    
    # Returns the best optimal_position plus 1 because optimal_position is an index rather than a position that starts from 1.
    return optimal_position + 1



if __name__ == "__main__":
    DNAsequence1 = input("Please enter DNA Sequence 1: ")
    DNAsequence2 = input("Please enter DNA Sequence 2: ")

    
    if len(DNAsequence1) < len(DNAsequence2):

        # DNA_indels_pad determines the difference between the two lengths of DNA sequence.
        # It calls the pad_with_indels function and modifies the shorter sequence to include indels. 
        DNA_indels_pad = pad_with_indels(DNAsequence1, len(DNAsequence2) - len(DNAsequence1))

        # It calls the change_sequence function and assigns seq1_letter_change with the new modified string.
        seq1_letter_change = change_sequence1(DNA_indels_pad, DNAsequence2) 
        seq2_letter_change = change_sequence2(DNA_indels_pad, DNAsequence2) 

        print("Sequence 1: ", seq1_letter_change)
        print("Sequence 2: ", seq2_letter_change)

    else:
        DNA_indels_pad = pad_with_indels(DNAsequence2, len(DNAsequence1) - len(DNAsequence2))

        seq1_letter_change = change_sequence1(DNAsequence1, DNA_indels_pad)
        seq2_letter_change = change_sequence2(DNAsequence1, DNA_indels_pad)

        print("Sequence 1:", seq1_letter_change)
        print("Sequence 2:", seq2_letter_change)


    # These variables keep track of the updated sequences throughout the while loop.
    seq1_accum = seq1_letter_change
    seq2_accum = seq2_letter_change
    
    print_menu()
    choice = get_menu_choice()
    
    # This while loop makes sure the choice inputted isn't 5 so that it keeps going. 
    while choice != 5:
        
        if choice == 1:
            sequence_choice = get_sequence_number()
            # sequence_choice calls get_sequnece_number() for input on what sequence the user wants to modify.
        
            if sequence_choice == 1:
                indel_position = get_insert_position(seq1_accum)
                # It calls get_insert_position to find out what position the user wants to put an indel at. 

                seq1_modified = insert_indel(seq1_accum, indel_position - 1)
                # It calls insert_indel to put the indel at that position indel_position asks for minus one
                # because it has to be inserted as an index 

                seq2_modified = pad_with_indels(seq2_accum, len(seq1_modified) - len(seq2_accum))


            else:
                indel_position = get_insert_position(seq2_accum)

                seq2_modified = insert_indel(seq2_accum, indel_position - 1)
                seq1_modified = pad_with_indels(seq1_accum, len(seq2_modified) - len(seq1_accum))
            
            seq1_change = change_sequence1(seq1_modified, seq2_modified)
            seq2_change = change_sequence2(seq1_modified, seq2_modified)

            print(f"Sequence 1: {seq1_change}")
            print(f"Sequence 2: {seq2_change}")

            
        elif choice == 2:
            sequence_choice = get_sequence_number()

            if sequence_choice == 1:
                remover = get_remove_position(seq1_accum)
                # The "remover" variable calls get_remove_position() to find out what position the user wants to remove an indel from.

                seq1_modified = remove_indel(seq1_accum, remover - 1 )
                # The "seq1_modified" actually removes the indel at that position.

                seq2_modified = indel_modify(seq2_accum)
                # seq2_modified calls indel_modify to remove an indel from the last position. 

            else:
                remover = get_remove_position(seq2_accum)

                seq2_modified = remove_indel(seq2_accum, remover - 1 )
                seq1_modified = indel_modify(seq1_accum)
                

            seq1_change = change_sequence1(seq1_modified, seq2_modified)
            seq2_change = change_sequence2(seq1_modified, seq2_modified)

            print(f"Sequence 1: {seq1_change}")
            print(f"Sequence 2: {seq2_change}")

               
        elif choice == 3:
            # Since choice #3 does no modifications to the sequences, seq1_change and seq2_change is set to the accumulator variable
            # to store for future use.  
            seq1_change = seq1_accum
            seq2_change = seq2_accum

            matchcount = count_matches(seq1_change, seq2_change)
            print(f"Similarity: {matchcount} matches, {len(seq1_change) - matchcount} mismatches. {((matchcount / len(seq1_change)) * 100):0.1f}% match rate.")

            print(f"Sequence 1: {seq1_change}")
            print(f"Sequence 2: {seq2_change}")

        elif choice == 4:
            sequence_choice = get_sequence_number()

            seq1_change = seq1_accum
            seq2_change = seq2_accum

            if sequence_choice == 1:
                optimal_position = optimal_indel_position(seq1_change, seq2_change)
                # Optimal_positions calls optimal_indel_position() to find the optimal position with the greatest number of matches. 

                print(f"Insert an indel into Sequence 1 at position {optimal_position}.")

                seq1_edit = insert_indel(seq1_change, optimal_position - 1)
                seq2_edit = pad_with_indels(seq2_change, len(seq1_edit) - len(seq2_change))

            
            else:
                
                optimal_position = optimal_indel_position(seq2_change, seq1_change)
                print(f"Insert an indel into Sequence 2 at position {optimal_position}.")

                seq2_edit = insert_indel(seq2_change, optimal_position - 1)
                seq1_edit = pad_with_indels(seq1_change, len(seq2_edit) - len(seq1_change))
            
            seq1_modify = change_sequence1(seq1_edit, seq2_edit)
            seq2_modify = change_sequence2(seq1_edit, seq2_edit)

            matchcount = count_matches(seq1_modify, seq2_modify)

            print(f"Similarity: {matchcount} matches, {len(seq1_modify) - matchcount} mismatches. {((matchcount / len(seq1_modify)) * 100):0.1f}% match rate.")
            
            # These variables do not change the overall sequences and prints the original sequences without the optimal indel before calling option #4.
            print(f"Sequence 1: {seq1_change}")
            print(f"Sequence 2: {seq2_change}")


        else:
            # Using option #5 quits the program.
            break
        
        # After an if-branch, it stores the updated sequence into seq1_accum and seq2_accum so that
        # it can be used for the other options once it loops again to the main menu.
        seq1_accum = seq1_change
        seq2_accum = seq2_change
        print_menu()
        choice = get_menu_choice()