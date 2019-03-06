var opensocket = angular.module('opensocket', ['ui.router']);

opensocket.controller('layoutCtrl', function ($state) {
    $state.go('app.workbench');
});

opensocket.config(function ($stateProvider) {

    $stateProvider
        .state({
            name: 'app',
            url: '',
            templateUrl: '/ui-templates/layout.html',
            controller: 'layoutCtrl'
        })
        .state({
            name: 'app.console',
            url: '/console',
            templateUrl: '/ui-templates/console.html'
        }).state({
        name: 'app.workbench',
        url: '/workbench',
        templateUrl: '/ui-templates/workbench.html'
    });
});

opensocket.run(function ($rootScope) {
    // Initializations
});

angular.element(function () {
    angular.bootstrap(document.body, ['opensocket']);
});




