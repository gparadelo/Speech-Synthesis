form Arguments
  comment Args: input files (wav, PitchTier), output file (wav), min pitch, max pitch.
  word file_wav_in .wav
  word file_PitchTier_in .PitchTier
  word file_wav_out .wav
  real min_pitch 75
  real max_pitch 500
endform

Read from file... 'file_wav_in$'
Rename... myfile
Read from file... 'file_PitchTier_in$'
Rename... myfile

select PitchTier myfile
To Pitch... 0.02 'min_pitch' 'max_pitch'

select Sound myfile
plus Pitch myfile
To Manipulation
Get resynthesis (overlap-add)
Save as WAV file... 'file_wav_out$'

