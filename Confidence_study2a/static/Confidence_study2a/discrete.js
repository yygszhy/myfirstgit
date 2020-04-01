// discrete.js
// Sample from discrete distributions.

// Utility functions
function _sum(a, b) {
  return a + b;
};
function _fillArrayWithNumber(size, num) {
  // thanks be to stackOverflow... this is a beautiful one-liner
  return Array.apply(null, Array(size)).map(Number.prototype.valueOf, num);
};
function _rangeFunc(upper) {
  var i = 0, out = [];
  while (i < upper) out.push(i++);
  return out;
};
// Prototype function
function _samplerFunction(size) {
    if (!Number.isInteger(size) || size < 0) {
	throw new Error ("Number of samples must be a non-negative integer.");
    }
    if (!this.draw) {
        throw new Error ("Distribution must specify a draw function.");
    }
    var result = [];
    while (size--) {
        result.push(this.draw());
    }
    return result;
};
// Prototype for discrete distributions
var _samplerPrototype = {
  sample: _samplerFunction
};

/**
 * Constructor for Bernoulli distribution
 */
exports.Bernoulli = function(p) {

  var result = Object.create(_samplerPrototype);

  result.draw = function() {
    return (Math.random() < p) ? 1 : 0;
  };

  result.toString = function() {
    return "Bernoulli( " + p + " )";
  };

  return result;
}

/**
 * Constructor for Binomial distribution
 */
exports.Binomial = function(n, p) {
  
  var result = Object.create(_samplerPrototype),
  bern = exports.Bernoulli(p);

  result.draw = function() {
    return bern.sample(n).reduce(_sum, 0); // less space efficient than adding a bunch of draws, but cleaner :)
  }

  result.toString = function() { 
    return "Binom( " + 
      [n, p].join(", ") + 
      " )"; 
  }

  return result;
}

/**
 * Constructor for Discrete distribution
 */
exports.Discrete = function(probs) { // probs should be an array of probabilities. (they get normalized automagically) //
  
  var result = Object.create(_samplerPrototype),
  k = probs.length;

  result.draw = function() {
    var i, p;
    for (i = 0; i < k; i++) {
      p = probs[i] / probs.slice(i).reduce(_sum, 0); // this is the (normalized) head of a slice of probs
      if (exports.Bernoulli(p).draw()) return i;             // using the truthiness of a Bernoulli draw
    }
    return k - 1;
  };

  result.sampleNoReplace = function(size) {
    if (size>probs.length) {
      throw new Error("Sampling without replacement, and the sample size exceeds vector size.")
    }
    var disc, index, sum, samp = [];
    var currentProbs = probs;
    var live = _rangeFunc(probs.length);
    while (size--) {
      sum = currentProbs.reduce(_sum, 0);
      currentProbs = currentProbs.map(function(x) {return x/sum; });
      disc = exports.Discrete(currentProbs);
      index = disc.draw();
      samp.push(live[index]);
      live.splice(index, 1);
      currentProbs.splice(index, 1);
      sum = currentProbs.reduce(_sum, 0);
      currentProbs = currentProbs.map(function(x) {return x/sum; });
    }
    currentProbs = probs;
    live = _rangeFunc(probs.length);
    return samp;
  }

  result.toString = function() {
    return "Dicrete( [" + 
      probs.join(", ") + 
      "] )";
  };

  return result;
}

/**
 * Constructor for Multinomial distribution
 */
exports.Multinomial = function(n, probs) {

  var result = Object.create(_samplerPrototype),
  k = probs.length,
  disc = exports.Discrete(probs);

  result.draw = function() {
    var draw_result = _fillArrayWithNumber(k, 0),
    i = n;
    while (i--) {
      draw_result[disc.draw()] += 1;
    }
    return draw_result;
  };

  result.toString = function() {
    return "Multinom( " + 
      n + 
      ", [" + probs.join(", ") + 
      "] )";
  };

  return result;
}

/**
 * Constructor for Negative Binomial distribution
 */
exports.NegBinomial = function(r, p) {
  var result = Object.create(_samplerPrototype);

  result.draw = function() {
    var draw_result = 0, failures = r;
    while (failures) {
      exports.Bernoulli(p).draw() ? draw_result++ : failures--;
    }
    return draw_result;
  };

  result.toString = function() {
    return "NegBinomial( " +  r +
      ", " + p + " )";
  };

  return result;
}

/**
 * Constructor for Poisson distribution
 */
exports.Poisson = function(lambda) {
  var result = Object.create(_samplerPrototype);

  result.draw = function() {
    var draw_result, L = Math.exp(- lambda), k = 0, p = 1;

    do {
      k++;
      p = p * Math.random()
    } while (p > L);
    return k-1;
  }

  result.toString = function() {
    return "Poisson( " + lambda + " )";
  }

  return result;
}

/**
 * Sample from an array.
 */
exports.sample_from_array = function(array, numSamples, withReplacement) {
    var n = numSamples || 1,
    result = [],
    copy,
    disc,
    index;

    if (!withReplacement && numSamples > array.length) {
	throw new Error("Sampling without replacement, and the sample size exceeds vector size.")
    }

    if (withReplacement) {
	while(numSamples--) {
	    disc = exports.Discrete(_fillArrayWithNumber(array.length, 1));
	    result.push(array[disc.draw()]);
	}
    } else {
	// instead of splicing, consider sampling from an array of possible indices? meh?
	copy = array.slice(0);
	while (numSamples--) {
	    disc = exports.Discrete(_fillArrayWithNumber(copy.length, 1));
	    index = disc.draw();
	    result.push(copy[index]);
	    copy.splice(index, 1);
	}	
    }
    return result;
}

// Give a global variable for this library
if (typeof window !== 'undefined')
  window.SJS = window.Sampling = exports;
