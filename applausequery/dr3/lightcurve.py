#
# Licensed under a 3-clause BSD style license - see LICENSE.rst
#

# internal imports
from .. import tap_session

# Standard library imports

# Third party modules

__all__ = ['lc_by_ucac4_id']

def lc_by_ucac4_id(ucac4_id):
    """
    Get a basic lightcurve containing only observation dates, magnitudes
    and magnitude errors.

    ADQL query: 
        SELECT jd_mid,bmag,bmagerr,vmag,vmagerr\n
        FROM applause_dr3.lightcurve\n
        WHERE bmag IS NOT NULL\n
        AND bmagerr IS NOT NULL\n
        AND vmag IS NOT NULL\n
        AND vmagerr IS NOT NULL\n
        AND ucac4_id='XXX-YYYYY'\n
        ORDER BY jd_mid
    
    Parameters
    ----------
    ucac4_id : str
        UCAC4 identifier in format XXX-YYYYY, e.g. 104-010297
    
    Returns
    -------
        Table object

    """
    query = "SELECT jd_mid,bmag,bmagerr,vmag,vmagerr \
        FROM applause_dr3.lightcurve \
        WHERE bmag IS NOT NULL \
        AND bmagerr IS NOT NULL \
        AND vmag IS NOT NULL \
        AND vmagerr IS NOT NULL \
        AND ucac4_id=\'%s\' \
        ORDER BY jd_mid" %(ucac4_id)
    lc = tap_session.run_async(query)
    return lc.to_table()
