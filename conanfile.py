from conans import ConanFile, CMake, tools
import os

channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "memsharded")

class httpPOCOReuseConan(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   requires = "httpPOCO/0.1@%s/%s" % (username, channel)
   generators = "cmake"

   def build(self):
       cmake = CMake(self)
       cmake.configure()
       cmake.build()

   def test(self):
       # equal to ./bin/greet, but portable win: .\bin\greet
       if not tools.cross_building(self.settings):
           self.run(os.sep.join([".","bin", "http"]))
