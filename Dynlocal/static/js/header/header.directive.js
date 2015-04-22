angular.module('headerModule')
.directive('headerWidget', function(){
  return {
    restrict : 'E',
    transclude : true,
    scope : false,
    templateUrl : '/header/'}
  });
