__version__ = '0.4'



#import os
#import sys
#print( 'full sys path: 1' )
#print( '\n'.join(sys.path) )
#print( 'init path: ', os.path.realpath( __file__ ) )
#sys.path.append( os.path.dirname( __file__ ) )
#print( 'full sys path: 2' )
#print( '\n'.join(sys.path) )

#---------------------------------------------------------------------------------------------------------------------------------------------------#
#####################################################################################################################################################
#
#	Import user functions:
#
#####################################################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------------------------------#
from VocalTractLab.VocalTractLabApi import automatic_calculation_of_TRX_and_TRY
from VocalTractLab.VocalTractLabApi import get_version
from VocalTractLab.VocalTractLabApi import get_constants
from VocalTractLab.VocalTractLabApi import get_param_info
from VocalTractLab.VocalTractLabApi import get_shape
from VocalTractLab.VocalTractLabApi import get_shapes
from VocalTractLab.VocalTractLabApi import load_speaker_file
from VocalTractLab.VocalTractLabApi import load_speaker
from VocalTractLab.VocalTractLabApi import get_gestural_score_audio_duration
from VocalTractLab.VocalTractLabApi import gestural_score_to_audio
from VocalTractLab.VocalTractLabApi import gestural_score_to_tract_sequence
from VocalTractLab.VocalTractLabApi import segment_sequence_to_gestural_score
from VocalTractLab.VocalTractLabApi import tract_sequence_to_audio
from VocalTractLab.VocalTractLabApi import motor_sequence_to_spectrogram
from VocalTractLab.VocalTractLabApi import motor_sequence_to_melspectrogram
from VocalTractLab.VocalTractLabApi import tract_sequence_to_limited_tract_sequence
from VocalTractLab.VocalTractLabApi import tract_sequence_to_svg
from VocalTractLab.VocalTractLabApi import tract_sequence_to_transfer_functions
from VocalTractLab.VocalTractLabApi import tract_sequence_to_tube_states
from VocalTractLab.audio_tools import calculate_spectral_distances
from VocalTractLab.text_to_speech import text_to_speech
from VocalTractLab.text_to_speech import tts
from VocalTractLab.function_tools import load
from VocalTractLab.function_tools import save
from VocalTractLab.phonemes import *
#---------------------------------------------------------------------------------------------------------------------------------------------------#
#####################################################################################################################################################


#---------------------------------------------------------------------------------------------------------------------------------------------------#
#####################################################################################################################################################
#
#	Import classes
#
#####################################################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------------------------------#
from VocalTractLab import audio_tools
from VocalTractLab.frequency_domain import Transfer_Function
from VocalTractLab import function_tools
from VocalTractLab import g2p
from VocalTractLab import plotting_tools
from VocalTractLab import mc_generator
from VocalTractLab.segment_sequence import Segment_Sequence
from VocalTractLab.targets import Target
from VocalTractLab.targets import Target_Sequence
from VocalTractLab.targets import Target_Score
from VocalTractLab.targets import Synchronous_Target_Score
from VocalTractLab.targets import Sub_Glottal_Motor_Score
from VocalTractLab.targets import Supra_Glottal_Motor_Score
from VocalTractLab.targets import Motor_Score
#from VocalTractLab import target_estimation
from VocalTractLab.tract_sequence import Sub_Glottal_Sequence
from VocalTractLab.tract_sequence import Supra_Glottal_Sequence
from VocalTractLab.tract_sequence import Motor_Sequence
from VocalTractLab.tube_states import Tube_State
#---------------------------------------------------------------------------------------------------------------------------------------------------#
#####################################################################################################################################################
