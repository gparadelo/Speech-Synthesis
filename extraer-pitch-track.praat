form Arguments
  comment Args: input file (wav), output file (PitchTier), min pitch, max pitch.
  word file_in .wav
  word file_out .PitchTier
  real min_pitch 75
  real max_pitch 500
endform

Read from file... 'file_in$'
To Pitch... 0 'min_pitch' 'max_pitch'
Down to PitchTier
Save as text file... 'file_out$'
