# libraries and stuff
from PIL import Image
import numpy
import math

def REG_RGBs(IMG):
    with Image.open(IMG) as img:
        # Ignore PNGs Alpha cover
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            img = img.convert("RGB")
        else:        
            img = img.convert("RGB") # Image is now in RGB mode    
            
            # Numpy used to calculate the mean number of all RBG values (rounded up) & split into a 2D array
            array_means = numpy.mean((numpy.array(img)),axis=2).round()
            final_array_vals = array_means.tolist()

        return(final_array_vals)


def Encryption_Algorithm(message_to_encrypt,Given_Image):
    RGB_Vals = REG_RGBs(Given_Image)
    counter = 0
    encrypted_S1_message = str()
    
    for character in message_to_encrypt:
        to_ASCII = ord(character)
        value_to_use = int(RGB_Vals[counter][counter])
        encrypted_S1_message += chr(to_ASCII ^ value_to_use) # XOr operation performed to encrypt string
        counter += 1
        
        if counter >= len(RGB_Vals): # In case of going over the length of the list, just loop at the back of the list
            counter = 0
    
    operation_list = list(encrypted_S1_message)
     
    for i in range(math.floor(len(operation_list)/2)):
        for chr_index in range(len(operation_list)): # perform shifts to the right to add shuffling
            if chr_index + 1 > len(operation_list)-1:
                continue
            
            temp = operation_list[chr_index + 1]
            current = operation_list[chr_index]
            
            operation_list[chr_index + 1] = current
            operation_list[chr_index] = temp
       
    encrypt_string = ""
    for char in operation_list:
        encrypt_string += char
            
    return(encrypt_string)
        
        
def Unecryption_Algorithm(encrypted_string, provided_image):
    
    operation_list = list(encrypted_string)

    # Unshifting process
    unshifted_str = list()
    for index_of_char_to_shift in range( math.floor(len(operation_list) / 2) + 1, len(operation_list) - 1):
        # We perform an unshift in order to standardise the encrypted string
        unshifted_str.append(operation_list[index_of_char_to_shift])
        
        operation_list.pop(index_of_char_to_shift)
        
    # we reconsturct the string by merging the remaining characters with the 'unshifted_str' list
    unshifted_str.append(operation_list[len(operation_list)-1])
    operation_list.pop(len(operation_list)-1)
    
    for remaining_item in operation_list:  
        unshifted_str.append(remaining_item)
        
    RGB_Vals = REG_RGBs(provided_image)
    counter = 0
    unencrypted_str = str()
    for character in unshifted_str:
        to_ASCII = ord(character)
        value_to_use = int(RGB_Vals[counter][counter])
        unencrypted_str += chr(to_ASCII ^ value_to_use) # XOr operation performed to unencrypt string, as 2 XOr operations with the same values cancel each other
        counter += 1
        
        if counter >= len(RGB_Vals): # In case of going over the length of the list, just loop at the back of the list
            counter = 0

    return(unencrypted_str)

        

