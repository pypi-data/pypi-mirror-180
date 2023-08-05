from os.path import dirname, join

class Constants:
    """
    Define fixed parameters in this class
    """
    def __init__(self):
        """
        Instance attributes
        ----------------------
        fair_threshold_low : float
                Fairness threshold minimum value

        fair_threshold_high : float
                Fairness threshold maximum value

        fair_neutral_tolerance : float
                Fairness neutral tolerance
                
        fair_neutral_threshold_low : float
                Fairness neutral threshold minumum value

        fair_neutral_threshold_high : float
                Fairness neutral threshold maximum value

        proportion_of_interpolation_fitting_low : float
                Proportion of interpolation fitting minumum value

        proportion_of_interpolation_fitting_high : float
                Proportion of interpolation fitting maximum value

        selection_threshold : float
                Selection threshold
        
        tradeoff_threshold_bins : float
                Tradeoff threshold bins

        uplift_threshold_proportion: float
                Tradeoff uplift threshold proportion for e_lift
                
        perf_dynamics_array_size : int
                To be used in performance_dynamics() to determine size of samples

        uplift_min_threshold: float
                performance dynamics uplift minimum threshold

        uplift_max_threshold : float
                performance dynamics uplift maximum threshold

        classify_min_threshold: float
                Tradeoff minimum threshold

        classify_max_threshold: float
                Tradeoff maximum threshold

        k : int
                Number of samples to calculate confidence interval

        decimals : int
                Number of decimal places for values to be rounded off
        """
        import configparser
        file = join(dirname(__file__), 'config.ini')
        config = configparser.ConfigParser()
        config.read(file)
        self.fair_threshold_low = config.getfloat('threshold', 'fair_threshold_low')
        self.fair_threshold_high  = config.getfloat('threshold', 'fair_threshold_high')
        self.fair_neutral_tolerance = config.getfloat('threshold', 'fair_neutral_tolerance')
        self.fair_neutral_threshold_low = config.getfloat('threshold', 'fair_neutral_tolerance_low')
        self.fair_neutral_threshold_high = config.getfloat('threshold', 'fair_neutral_tolerance_high')
        self.proportion_of_interpolation_fitting_low = config.getfloat('threshold', 'proportion_of_interpolation_fitting_low')
        self.proportion_of_interpolation_fitting_high = config.getfloat('threshold', 'proportion_of_interpolation_fitting_high')
        self.selection_threshold = config.getfloat('threshold', 'selection_threshold')
        self.tradeoff_threshold_bins = config.getint('threshold', 'tradeoff_threshold_bins')
        self.uplift_threshold_proportion = config.getfloat('threshold', 'uplift_threshold_proportion')
        self.perf_dynamics_array_size = config.getint('default', 'perf_dynamics_array_size')
        self.uplift_min_threshold = config.getfloat('threshold', 'uplift_min_threshold')
        self.uplift_max_threshold = config.getfloat('threshold', 'uplift_max_threshold')
        self.classify_min_threshold = config.getfloat('threshold', 'classify_min_threshold')
        self.classify_max_threshold = config.getfloat('threshold', 'classify_max_threshold')
        self.k = config.getint('default', 'k')
        self.decimals = config.getint('default', 'decimals')
