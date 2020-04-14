def estimator(data):
    return data


def covid19ImpactEstimator(reportedCases):
    '''
    '''
    results = {
        'data': {
            reportedCases
        },
        'impact': {},
        'severeImpact': {}
    }
    currentlyInfected = int(reportedCases) * 10
    results['impact']['currentlyInfected'] = currentlyInfected
    severeImpact = reportedCases * 50
    results['severeImpact']['currentlyInfected'] = severeImpact
    infectionsByRequestedTime = currentlyInfected * 512
    results['impact'] = infectionsByRequestedTime
    results['severeImpact'] = infectionsByRequestedTime

    return results
