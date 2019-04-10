import pymzml
import sys
import pygal

def main(mzml, specid):
    """
    Plot Spectrum <specID> form a given mzML

    Usage:

    ./plot_mzml_spec.py <mzML> <spec_ID>
    """
    run = pymzml.run.Reader(mzml)
    spectrum = run[specid]
    spectrum_plot = pygal.MZI(show_dots=False)
    spectrum_plot.title = f'Spectrum {specid}'
    # spectrum_plot.x_labels = [
    #     {'label': 'One', 'value': 0},
    #     {'label': 'b2', 'value': 0.3},
    #     {'label': 'y4', 'value': 0.5},
    # ]
    spectrum_plot.add('mz/i', spectrum.peaks('centroided'), allow_interruptions=True)
    # spectrum_plot.add('A', [(0,-10), (0.1, -7), (0.5,-2)], allow_interruptions=True)
    spectrum_plot.render()
    spectrum_plot.render_to_file(f'Spectrum_{specid}.svg')



if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(main.__doc__)
    else:
        main(sys.argv[1], sys.argv[2])
