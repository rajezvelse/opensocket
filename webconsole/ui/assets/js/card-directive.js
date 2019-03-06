opensocket.directive('chatCard', function ($timeout) {
    return {
        restrict: 'E',
        scope: {
            characterName: "@characterName",
        },
        templateUrl: '/ui-templates/chat-card.html',
        link: function ($scope, element, attrs) {
            $scope.channelType = 'public';
            $scope.isAdmin = $scope.characterName == 'Administrator';
            $scope.msgModel = '';
            $scope.isPrivate = false;
            $scope.messages = [];
            $scope.profileImages = {
                'Administrator': 'avatar-3',
                'Jeny William': 'avatar-4',
                'John Doue': 'avatar-2',
                'Alex Thompson': '01'
            };


            var namespace = '/chat';
            var chat = io('http://' + document.domain + ':' + location.port + namespace, {
                query: {token: "dummy"}
            });

            $scope.messages.push({
                type: 'message',
                name: $scope.characterName,
                msg: 'Greetings !',
                image: $scope.profileImages[$scope.characterName],
                time: new Date()
            });

            chat.emit('message', $scope.messages[0]);

            // Listen for reply messages
            chat.on('message', function (event) {
                $timeout(function () {
                    $scope.$apply(function () {

                        $scope.messages.push({
                            type: 'reply',
                            name: event.name,
                            msg: event.msg,
                            image: $scope.profileImages[event.name],
                            time: new Date()
                        });
                    })
                })
            });


            // Send messages
            $scope.sendMessage = function () {
                var data = {
                    type: 'message',
                    name: $scope.characterName,
                    msg: $scope.msgModel,
                    image: $scope.profileImages[$scope.characterName],
                    time: new Date()
                };

                if ($scope.isPrivate) {
                    data['room'] = 'discussion_channel';
                }

                chat.emit('message', data);
                $scope.messages.push(data);

                $timeout(function () {
                    $scope.$apply(function () {
                        $scope.msgModel = '';
                    })
                })
            };

            // Join / Leave discussion channel
            $scope.togglePrivate = function (val) {
                if (val) {
                    chat.emit('join_discussion_channel');
                } else {
                    chat.emit('leave_discussion_channel');
                }

                $timeout(function () {
                    $scope.$apply(function () {
                        $scope.isPrivate = val;
                        if (val) {
                            $scope.channelType = 'private';
                        } else {
                            $scope.channelType = 'public';
                        }
                    })
                })
            };

            // Private toggle button
            if (!$scope.isAdmin)
                setTimeout(function () {
                    var input = $(element).find('.js-primary');
                    var switchery = new Switchery(input[0], {color: '#4099ff', jackColor: '#fff', size: 'small'});
                    input[0].onchange = function () {
                        $scope.togglePrivate(input[0].checked)
                    };
                }, 100)

        }
    }
});