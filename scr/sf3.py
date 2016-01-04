
def design_filter(lowcut, highcut, fs, order=3):
    nyq = 0.5*fs
    low = lowcut/nyq
    high = highcut/nyq
    b,a = butter(order, [low,high], btype='band')
    return b,a

def normalize(block):
    count = len(block)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format, block )
    doubles = [x * SHORT_NORMALIZE from x in shorts]
    return doubles


def get_rms(samples):
    sum_squares = 0.0
    for sample in doubles:
        sum_squares += n*n
    return math.sqrt( sum_squares / count )


pa = pyaudio.PyAudio()
stream = pa.open(format = FORMAT,
         channels = CHANNELS,
         rate = RATE,
         input = True,
         frames_per_buffer = INPUT_FRAMES_PER_BLOCK)

errorcount = 0

# design the filter
b,a = design_filter(19400, 19600, 48000, 3)
# compute the initial conditions.
zi = lfilter_zi(b, a)

for i in range(1000):
    try:
        block = stream.read(INPUT_FRAMES_PER_BLOCK)
    except IOError, e:
        errorcount += 1
        print( "(%d) Error recording: %s"%(errorcount,e) )
        noisycount = 1

    samples = normalize(block)

    bandpass_samples,zi = lfilter(b, a, samples, zi)

    amplitude = get_rms(samples)
    bandpass_ampl = get_rms(bandpass_samples)
    print amplitude
    print bandpass_ampl
