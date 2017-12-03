var waveletTransformer = angular.module('waveletTransformer',['ui.bootstrap']);
waveletTransformer.controller('waveletController',function($scope,$uibModal){
  // default values
  $scope.motherWavelet = "morlet";
  $scope.angFreq = 8;
  $scope.minFreq = 0.01;
  $scope.freqResolution = 50;
  $scope.freqVecType = "lin"

  $scope.openParamSettings = function(){
    var modalInstance = $uibModal.open({
      templateUrl: 'param-settings.html',
      controller: 'paramSettingsController',
      scope: $scope,
    });
    modalInstance.result.then(function(results){
      //ok
      $scope.motherWavelet = results.motherWavelet;
      $scope.angFreq = results.angFreq;
      $scope.minFreq = results.minFreq;
      $scope.freqResolution = results.freqResolution;
      $scope.freqVecType = results.freqVecType;
    }, function(){
      //dismiss
    });
  };
});

waveletTransformer.controller('paramSettingsController',function($scope,$uibModalInstance){
  $scope.ok = function () {
      var results = {
        motherWavelet: $scope.motherWavelet,
        angFreq: $scope.angFreq,
        minFreq: $scope.minFreq,
        freqResolution: $scope.freqResolution,
        freqVecType: $scope.freqVecType,
      };
      $uibModalInstance.close(results);
    };
    $scope.cancel = function () {
      $uibModalInstance.dismiss();
    };
});
