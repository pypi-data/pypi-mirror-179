#
# set up json input file needed for gnssir

import argparse
import json
import os
import subprocess
import sys

import gnssrefl.gps as g

from gnssrefl.utils import str2bool


def parse_arguments():
    # user inputs the observation file information
    parser = argparse.ArgumentParser()
    # required arguments
    parser.add_argument("station", help="station (lowercase)", type=str)
    parser.add_argument("lat", help="latitude (degrees)", type=float)
    parser.add_argument("long", help="longitude (degrees)", type=float)
    parser.add_argument("height", help="ellipsoidal height (meters)", type=float)
    # optional inputs
    parser.add_argument("-e1", default=None, type=int, help="lower limit elevation angle (deg)")
    parser.add_argument("-e2", default=None, type=int, help="upper limit elevation angle (deg)")
    parser.add_argument("-h1", default=None, type=float, help="lower limit reflector height (m)")
    parser.add_argument("-h2", default=None, type=float, help="upper limit reflector height (m)")
    parser.add_argument("-nr1",default=None, type=float, help="lower limit noise region for QC(m)")
    parser.add_argument("-nr2",default=None, type=float, help="upper limit noise region for QC(m)")
    parser.add_argument("-peak2noise", default=None, type=float, help="peak to noise ratio used for QC")
    parser.add_argument("-ampl", default=None, type=float, help="required spectral peak amplitude for QC")
    parser.add_argument("-allfreq", default=None, type=str, help="set to True to include all GNSS")
    parser.add_argument("-l1", default=None, type=str, help="set to True to only use GPS L1")
    parser.add_argument("-l2c", default=None, type=str, help="set to True to only use GPS L2C")
    parser.add_argument("-xyz", default=None, type=str, help="set to True if using Cartesian coordinates")
    parser.add_argument("-refraction", default=None, type=str, help="Set to False to turn off refraction correction")
    parser.add_argument("-extension", default=None, type=str, help="Provide extension name so you can try different strategies")
    parser.add_argument("-ediff", default=None, type=str, help="ediff (degrees) default is 2")
    parser.add_argument("-delTmax", default=None, type=float, help="max arc length (min) default is 75")
#    parser.add_argument('-az_list', nargs="*",type=float,  help='azimuth min/max, e.g. 0 180  )')


    args = parser.parse_args().__dict__

    # convert all expected boolean inputs from strings to booleans
    boolean_args = ['allfreq', 'l1', 'l2c', 'xyz', 'refraction']
    args = str2bool(args, boolean_args)

    # only return a dictionary of arguments that were added from the user - all other defaults will be set in code below
    return {key: value for key, value in args.items() if value is not None}


def make_json(station: str, lat: float, long: float, height: float, e1: int = 5, e2: int = 25,
              h1: float = 0.5, h2: float = 6.0, nr1: float = None, nr2: float = None,
              peak2noise: float = 2.7, ampl: float = 6.0, allfreq: bool = False,
              l1: bool = False, l2c: bool = False, xyz: bool = False, refraction: bool = True,
              extension: str = None, ediff: float=2.0, delTmax: float=75.0  ):

    """

    Parameters
    ----------
    station : string
        4 or 9 character ID of the station.

    lat : float
        latitude in degrees.

    long : float
        longitude in degrees.

    height : float
        ellipsoidal height in meters.

    e1 : integer, optional
        elevation angle lower limit in degrees. default is 5.

    e2 : integer, optional
        elevation angle upper limit in degrees. default is 25.

    h1 : float, optional
        reflector height lower limit in meters. default is 0.5.

    h2 : float, optional
        reflector height upper limit in meters. default is 6.

    nr1 : float, optional
        noise region lower limit for QC in meters. default is None.

    nr2 : float, optional
        noise region upper limit for QC in meters. default is None.

    peak2noise : float, optional
        peak to noise ratio used for QC.
        default is 2.7 (just a starting point for water - should be 3 or 3.5 for snow or soil...)

    ampl : float, optional
        spectral peak amplitude for QC. default is 6.0
        this is receiver and elevation angle region dependent - so you need to change it based on your site 

    allfreq : Boolean, optional
        True requests all GNSS frequencies.
        default is False (defaults to use GPS frequencies).

    l1 : boolean, optional
        set to True to use only GPS L1 frequency. default is False.

    l2c : boolean, optional
        set to use only GPS L2C frequency. default is False.

    xyz : boolean, optional
        set to True if using Cartesian coordinates instead of Lat/Long/Ht.
        default is False.

    refraction : boolean, optional
        set to False to turn off refraction correction.
        default is True.

    extension : string, optional
        provide extension name so you can try different strategies. 
        Results will then go into $REFL_CODE/YYYY/results/ssss/extension
        Default is None

    az_list : list of floats
        azimuth min and max (for now)
        default is 0 to 360

    ediff : float
        quality control parameter (Degrees)
        default is 2

    delTmax : float
        maximum allowed arc length (minutes)
        default is 75, appropriate for snow or soil moisture
        should be shorter (30 minutes or so) for tidal regimes

    """

    # make sure environment variables exist
    g.check_environ_variables()

    #print(az_list)

    ns = len(station)
    if ns != 4:
        print('station name must be four characters long. Exiting.')
        sys.exit()

# location of the site - does not have to be very good.  within 100 meters is fine
    query_unr = False
    if lat + long == 0:
        print('Going to assume that you want to use the UNR database.')
        query_unr = True

    if xyz:
        xyz = [lat, long, height]
        lat, long, height = g.xyz2llhd(xyz)

    if query_unr:
        # try to find the coordinates  at UNR
        lat, long, height = g.queryUNR_modern(station)
        if lat == 0:
            print('Tried to find coordinates in our UNR database. Not found so exiting')
            sys.exit()

# start the lsp dictionary
    reqA = ampl

    lsp = {}
    lsp['station'] = station.lower()
    lsp['lat'] = lat
    lsp['lon'] = long
    lsp['ht'] = height

    if h1 > h2:
        print(f'h1 cannot be greater than h2. You have set h1 to {h1} and h2 to {h2}. Exiting.')
        sys.exit()

    lsp['minH'] = h1
    lsp['maxH'] = h2
    lsp['e1'] = e1
    lsp['e2'] = e2

# the default noise region will the same as the RH exclusion area for now
    if nr1 is None:
        nr1 = h1
    if nr2 is None:
        nr2 = h2

    lsp['NReg'] = [nr1, nr2]
    lsp['PkNoise'] = peak2noise

    # where the instructions will be written
    xdir = os.environ['REFL_CODE']
    outputdir = xdir + '/input'
    if not os.path.isdir(outputdir):
        subprocess.call(['mkdir', outputdir])

    if extension is None:
        outputfile = outputdir + '/' + station + '.json'
    else:
        outputfile = outputdir + '/' + station + '.' + extension + '.json'

    lsp['polyV'] = 4 # polynomial order for DC removal
    # change this so the min elevation angle for polynomial removal is the same as the 
    # requested analysis region. previously it was hardwired to 5-30
    #lsp['pele'] = [5, 30] # elevation angles used for DC removal
    if (lsp['e1']) < 5:
        usethis = lsp['e1']
        lsp['pele'] = [usethis, 30] # elevation angles used for DC removal
    else:
        lsp['pele'] = [5, 30] # elevation angles used for DC removal
    lsp['ediff'] = ediff # degrees
    lsp['desiredP'] = 0.005 # precision of RH in meters
    # azimuth regions in degrees (in pairs)
    # you can of course have more subdivisions here
    #if (az_list[0]) == 0 & (az_list[-1] == 360):
    if True:
        lsp['azval'] = [0, 90, 90, 180, 180, 270, 270, 360]
    # leaving this so the notebooks are not broken
    #else:
    #    print('You have requested specific azimuth limits')
    #    lsp['azval'] = g.make_azim_choices(az_list)

    # default frequencies to use - and their required amplitudes. The amplitudes are not set in stone
    # this is the case for only GPS, but the good L2 
    lsp['freqs'] = [1, 20, 5]
    if allfreq is True:
        # 307 was making it crash.  did not check as to why
        # includes glonass, galileo, and beidou
        lsp['freqs'] = [1, 20, 5, 101, 102, 201, 205, 206, 207, 208, 302, 306]

    if l1 is True:
        lsp['freqs'] = [1]

    if l2c is True:
        lsp['freqs'] = [20]

    # create a list with all values equal to reqA
    # but the length of the list depends on the length of the list of frequencies
    lsp['reqAmp'] = [reqA]*len(lsp['freqs'])

    lsp['refraction'] = refraction

    # write new RH results  each time you run the code
    lsp['overwriteResults'] = True

    # if snr file does not exist, try to make one
    lsp['seekRinex'] = False

    # compress snr files after analysis - saves disk space
    lsp['wantCompression'] = False

    # periodogram plots come to the screen
    lsp['plt_screen'] = False

    # command line req to only do a single satellite - default is do all satellites
    lsp['onesat'] = None

    # default will now be False ....
    # send some information on periodogram RH retrievals to the screen
    lsp['screenstats'] = False

    # save the output plots
    lsp['pltname'] = station + '_lsp.png'

    # how long can the arc be, in minutes
    lsp['delTmax'] = delTmax  
 

    print('writing out to:', outputfile)
    with open(outputfile, 'w+') as outfile:
        json.dump(lsp, outfile, indent=4)


def main():
    args = parse_arguments()
    make_json(**args)


if __name__ == "__main__":
    main()
