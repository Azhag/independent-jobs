"""
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

Written (W) 2013 Heiko Strathmann
"""
from abc import abstractmethod

class IndependentComputationEngine(object):
    def __init__(self):
        pass
    
    @abstractmethod
    def submit_job(self, job):
        raise NotImplementedError()
    
    @abstractmethod
    def wait_for_all(self):
        raise NotImplementedError()
