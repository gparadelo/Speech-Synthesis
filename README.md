Speech Synthesis
================

Project to synthesize speech for a language consisting of a subset of phonemes of the Spanish language. Only the letters e, k, m, r, s, t, f are allowed. Each appearance of a letter 'e' in the word can be stressed or not.

This is achieved by combining pre-recorded and prepared diphones corresponding to the inputed word.

Aditionaly, the system can synthesize a word to sound with the entonation of a question. To achieve this the frequencies of the combined word are tweaked slightly.


To use, execute the following command:

	python tts.py <word_to_synthesize> <result_file_name>

For instance:

	python tts.py EsemeketrEfe? /tmp/output.wav
	
	
The letters 'E' and 'e' are used to indicate stress ('E' is stressed).
The question mark a the end of the word indicates that it should sound like a question.
	