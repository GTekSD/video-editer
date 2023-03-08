import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Create folders to save trimmed and joined videos
if not os.path.exists('Trimmed'):
    os.makedirs('Trimmed')
if not os.path.exists('Joined'):
    os.makedirs('Joined')

# Ask user whether they want to trim or join videos
option = input('Do you want to trim or join videos? Enter T for trim and J for join: ')

if option.lower() == 't':
    # Get input video file name
    input_file = input('Enter the name of the video file you want to trim: ')

    # Get start and end times for trimming
    start_time = input('Enter the start time for trimming in seconds: ')
    end_time = input('Enter the end time for trimming in seconds: ')

    # Open the input video file and extract the desired clip
    clip = VideoFileClip(input_file)
    trimmed_clip = clip.subclip(float(start_time), float(end_time))

    # Save the trimmed clip in the 'Trimmed' folder
    trimmed_clip.write_videofile(os.path.join('Trimmed', 'trimmed_' + input_file))

    print('Video trimming complete. Trimmed video saved in the \'Trimmed\' folder.')
    
elif option.lower() == 'j':
    # Get input video file names
    input_files = input('Enter the names of the video files you want to join (separated by commas): ')

    # Split the input file names into a list
    input_files = input_files.split(',')

    # Open each input video file and extract the clips
    clips = [VideoFileClip(f) for f in input_files]

    # Concatenate the clips into a single video
    joined_clip = concatenate_videoclips(clips)

    # Save the joined clip in the 'Joined' folder
    joined_clip.write_videofile(os.path.join('Joined', 'joined_' + '_'.join(input_files)))

    print('Video joining complete. Joined video saved in the \'Joined\' folder.')
    
else:
    print('Invalid option. Please enter T for trim or J for join.')
