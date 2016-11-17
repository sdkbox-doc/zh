
##初始化

目前，配置过程在Lua中完成，并在创建 Google Play Game 服务对象时传递进去。 这个对象是由你管理的，在Lua中可以用 ```gpg`` 访问。

要创建一个 Google Play Game 服务实例的话，你需要传递一个表中，表中 包含了 ```ClientID``` 项, 它的值是你在 Google 开发者中心创建的应用的ID。

```
    local config = {ClientID="..."}
    gpg:CreateGameServices(config)
```

请注意，使用的 ```ClientID``` 是Google 开发者中心的较新的版本。 还有一个是在plist设置的较旧的版本。 确保您有正确的版本，否则初始化将失败。

配置结构包含的所有项值如下

```
{
    LogLevel        = 1 or 2,
    EnableSnapshots = true or false,
    ClientID        = forwards client id
}
```

##回调

大多数Google Play服务方法都需要用回调参数来返回结果。 这主要是因为方法是异步执行的。

支持两种类型的回调。 类方法回调和函数回调（其中包括lambda函数）

###类方法例子

```
ExampleClass:CallbackMethod(result)
    -- use result here
end

local someClass = ExampleClass:new()

gpg:MethodWithCallback({someClass, ExampleClass.CallbackMethod})
```

请注意，在类方法示例中，您必须传递类的实例以及方法。

###Lambda 函数例子

```
gpg:MethodWithCallback(function(result)
    -- use result here
end)
```

##Authorization

在您可以对Google Play服务执行任何操作之前，您必须进行验证。 如果您之前已通过身份验证，则sdkbox将尝试自动登录。 你仍然会得到与你自动登录时相同的事件。

要开始认证过程，请调用以下代码，并传入类方法或lambda方法（参阅 回调）以接收响应。

```
gpg:StartAuthorizationUI(function(result)
    if result.authStatus == gpg.AuthStatus.VALID then
        -- successfully authenticated
    end
end)
```


##Quests API

###准备

请务必查看Google Play服务 Quests [文档](https://developers.google.com/games/services/common/concepts/quests)，以便更好地了解如何使用自己的门户网站设置任务，以及参考上的API。

在您的游戏可以访问事件和任务之前，您必须先在[Google Play开发者中心](https://play.google.com/apps/publish/)中定义它们

###提交 event

您可以将事件发送到 Events 服务，以便让它知道发生了什么事。 这个方法没有结果，因此不需要回调。

```
gpg.Events:Increment("<event id>")
```

### 获取 events

要取当前 events 的数量，其以下其中一个方法

```
gpg.Events:Fetch("<event id>", function(result)
    -- use result.count here
end)

-- 或

gpg.Events:FetchAll(function(results)
    for k,v in pairs(results.data) do
        -- k is the event id
        -- use v.count here
    end
end)
```

回调结果的完整成员列表可以在本文档后面的的回调结果描述部分找到。

###显示 quests

Google Play服务提供了一个用于选择任务的UI，或者您可以根据回调中的 quests 数据显示您自己的UI。

您可以显示所有可用的任务，或只显示一个任务UI。

```
gpg.Quests:ShowUI("<quest id>", function(result)
    -- use result.quest here
end)

-- 或

gpg.Quests:ShowAllUI(function(result)
    -- use result.quest here
end)
```

###处理 quest 接受

如果你的游戏使用内置的任务UI，那么回调结果将有一个有效的Quest对象，你可以使用 ```quest.valid（）``` 验证，如果你使用自己的UI，那么你可以调用accept，如下:

```
gpg.Quests:Accept("<quest id>", function(result)
    -- use result.quest here
end)
```

###处理 quest 完成

当玩家接受一个 quest(任务) 后，你发送事件到 quest 服务，通知它任务的进度。

一个所有的任务标准已经满足，你可以在内置的用户界面或自己的界面声明完成奖励。

您通过调用声明方法声明任务里程碑。

```
gpg.Quests:ClaimMilestone("<milestone id>", function(result)
    if result.status == gpg.ClaimMilestoneResponse.VALID
        -- use result.milestone.completionRewardData here
    end
end)
```

##Player statistics(玩家状态)

有关玩家状态的信息以及如何使用玩家状态信息的完整说明，请参阅Google Play服务中的[文档](https://developers.google.com/games/services/cpp/stats)

###获取当前登录玩家的状态信息

你可以获取当前登录玩家的信息，如下

```
gpg.Stats:FetchForPlayer(function(result)
    if result.status == gpg.FetchForPlayerResponse.VALID then
        -- use PlayerStats here
    end
end)
```

## Achievements (成就)

相关的完整文档，参见[这里](https://developers.google.com/games/services/common/concepts/achievements)

###状态

成就可以隐藏，提示和解锁。

成就可以指定为标准或增量。 通常，增量成就可以让玩家逐渐进步，在更长的时间内获得成就

### 显示
```
    gpg.Achievements:ShowAllUI(function(result)
        -- handle the result here
    end)
```

### 获取所有成就
```
    gpg.Achievements:FetchAll(nil, function(result)
        log:d(log:to_str(result))
    end)
```

### 获取成就
```
    gpg.Achievements:Fetch('CgkI6KjppNEWEAIQBQ', nil, function(result)
        log:d(log:to_str(result))
    end)
```

### 增量成就
```
   gpg.Achievements:Increment('CgkI6KjppNEWEAIQBQ')
```

### 解锁成就
```
   gpg.Achievements:Unlock('CgkI6KjppNEWEAIQBQ')
```

### 提示成就
```
    gpg.Achievements:Reveal('CgkI6KjppNEWEAIQBQ')
```

## Leaderboards (排行榜)

更多文档参见[这里](https://developers.google.com/games/services/common/concepts/leaderboards)

### 显示
```
    gpg.Leaderboards:ShowUI("achievement id")
```

### 显示所有排行榜
```
    gpg.Leaderboards:ShowAllUI()
```

### 提交分数
```
    gpg.Leaderboards:SubmitScore("achievement id", score, "meta data", function(result)
    end)
```

### 获取所有分数的概括
```
    gpg.Leaderboards:FetchAllScoreSummaries("achievement id", data source, function(result)
    end)
```

### 获取所有
```
    gpg.Leaderboards:FetchAll(datasource, function(result)
    end)
```

### 获取分数页面
```
    gpg.Leaderboards:FetchScorePage("achievement id", datasource, time, timespan, collection, maxitmes, function(result)
    end)
```

### 获取下一页分数页
```
    gpg.Leaderboards:FetchNextScorePage(datasource, max items, function(result)
    end)
```

## Realtime Multiplayer (实时多人)

开始之前，请先了解Google Play Game 实时多人游戏的概念[这里](https://developers.google.com/games/services/common/concepts/realtimeMultiplayer)。

要使用实时多人游戏，您必须在Google Play开发者中心[启用](https://developers.google.com/games/services/cpp/realtimeMultiplayer)。

开始实时多人游戏，有三种方式与其他玩家连接，开始实时多人游戏。

### 快速游戏

让玩家与随机用户对战 (通过 auto-matching).

```
    gpg.Realtime:CreateRealTimeRoom(
        {
            type = "quick_match", -- select automatching
            quick_match_params =
            {
                maximumAutomatchingPlayers = 1,
                minimumAutomatchingPlayers = 1
            }
        },
        listener,
        function(result)
            if (gpg:IsSuccess(result.result)) then
                -- use result.room here
            end
        end
    )
```

### 邀请玩家

可以选择邀请特定玩家

```
    gpg.Realtime:CreateRealTimeRoom(
        {
            type = "ui", -- select invite players UI
            ui_params =
            {
                maximumPlayers = 1,
                minimumPlayers = 1
            }
        },
        listener,
        function(result)
            if (gpg:IsSuccess(result.result)) then
                -- use result.room here
            end
        end
    )
```

###接受邀请

在选择特定玩家的情况下，您将收到邀请，可以接受或拒绝。

```
    -- you can fetch all pending invitations like this
    -- this will call you back with a result and array of invitations
    gpg.Realtime:FetchInvitations(function(result)
        if (gpg:IsSuccess(result.result)) then
            -- do something with result.invitations
        end
    end)

    -- or you can use the UI to accept or decline an invitation
    gpg.Realtime:ShowRoomInboxUI(function(result)
        if (gpg:IsSuccess(result.result)) then
            -- do something with result.invitation
        end
    end)
```

###监听

房间创建方法，包括接受邀请，监听对象。 这是为了当房间状态有变化时，可以通过监听被告知。

这也是你将通过 ```onDataReceived``` 回调方法从其他玩家接收数据消息。

```
listener =
{
    -- called when something about the room changes
    onRoomStatusChanged = function(room)
    end,

    -- called when something about the connection changes
    onConnectedSetChanged = function(room)
    end,

    -- called when you get connected
    onP2PConnected = function(room, participant)
    end,

    -- called when you get disconnected
    onP2PDisconnected = function(room, participant)
    end,

    -- called if the status of one of the room participants changes
    onParticipantStatusChanged = function(room, participant)
    end,

    -- called whenever someone sends you a message
    onDataReceived = function(room, from_participant, data, is_reliable)
    end
}
```

### 给其他玩家发消息

有两种类型的消息可以发送，可靠和不可靠。
可靠的消息是保证的，如果丢失，将自动重新发送。
这有一些开销，所以如果你不需要可靠性，那么你可以发送一个不可靠的消息，这更高效,但以可靠性为代价。

```
gpg.Realtime:SendReliableMessage(room_id, participant_id, message, function(result)
    if (gpg:IsSuccess(result.result)) then
        -- message send was successful
    end
end)
```

发送不可靠的消息的参数json编码的字符串。
没有回调，因为是不可靠消息，没有返回状态。

```
gpg.Realtime:SendUnreliableMessage(json.encode({
    data = message,
    room_id = room_id
    participant_ids = {}
}))
```

### 离开房间

```
gpg.Realtime:LeaveRoom(room_id, function(result)
end)
```

### 接受 / 拒绝和忽略邀请

要接受邀请，你必须在你加入房间时设置监听，然后通过监听收取对应事件.

```
gpg.Realtime:AcceptInvitation(invitation_id, listener, function(result)
end)
```

拒绝和忽略邀请不需要回调参数，他们就是告诉服务器，你对这个邀请不感兴趣.
忽略邀请用在游戏结束了，但是这个邀请还在你的收件箱中.
```
gpg.Realtime:DeclineInvitation(invitation_id)
```

```
gpg.Realtime:DismissInvitation(invitation_id)
```

## Turn Based Multiplayer (回合制多人)

在开始之前，请务必先查看Google的文档[这里](https://developers.google.com/games/services/cpp/turnbasedMultiplayer)，并查看基于回合的多人游戏概念[这里](https://developers.google.com/games/services/common/concepts/turnbasedMultiplayer)

要开始一个基于回合的多人游戏，有两种方式这样做。 您可以使用UI来选择玩家（Google的或您自己的玩家），也可以开始快速匹配，为您选择玩家。

###快速比赛
```
local minimumPlayers = 1
local maximumPlayers = 2
local allowAutoMatching = false
gpg.Turnbased:ShowPlayerSelectUI(minimumPlayers, maximumPlayers, allowAutoMatching, function(result)
    params = {
        type = "quick_match",
        minimumAutomatchingPlayers = result.minimumAutomatchingPlayers,
        maximumAutomatchingPlayers = result.maximumAutomatchingPlayers,
        playerIds = result.playerIds
    }
    gpg.Turnbased:CreateTurnBasedMatch(params, function(result)
        if gpg:IsSuccess(result.result) then
            -- use result.match to start playing
        end
    end)
end)
```

###选择玩家界面
```
params = {
    type = "ui",
    minimumAutomatchingPlayers = 1,
    maximumAutomatchingPlayers = 2
}
gpg.Turnbased:CreateTurnBasedMatch(params, function(result)
	if gpg:IsSuccess(result.result) then
	    -- use result.match to start playing
	end
end)
```

### 处理比赛事件

对于基于回合的多人游戏，需要处理两个事件。 您可以注册两个回调（参阅 回调）以处理这些事件。

```
gpg.Turnbased:addMatchEventCallback(
	gpg.DefaultCallbacks.TURN_BASED_MATCH_EVENT,
	function(event)
	    gpg.Turnbased:ShowMatchInboxUI(function(result)
	        if gpg:IsSuccess(result.result) then
	            -- start using result.match here
	        end
	    end)
	end
)

-- 或

gpg.Turnbased:addMatchEventCallback(
	gpg.DefaultCallbacks.MULTIPLAYER_INVITATION_EVENT,
	{instance, method}
)

function class:method()
	gpg.Turnbased:ShowMatchInboxUI(function(result)
		if gpg:IsSuccess(result.result) then
			local match = result.match
			if match.matchStatus == gpg.MatchStatus.MY_TURN then
				-- do something with match, take a turn
			elseif match.matchStatus == gpg.MatchStatus.THEIR_TURN then
				-- update for their turn
			elseif match.matchStatus == gpg.MatchStatus.COMPLETED then
				-- complete match, dismiss
			else match.matchStatus == gpg.MatchStatus.EXPIRED then
				-- dismiss
	    	end
	    end
	end)
end
```

###进行回合

要进行回合，您必须使用回合数据更新比赛数据，并将其传递给下一个参赛者。 如果您希望自动匹配下一个参与者，则可以使用ID“AUTOMATCHING_PARTICIPANT”。

```
local results = match.participantResults
if winnig then
    results = gpg.Turnbased:createParticipantResult(match_id, match.pendingParticipant.id, my_rank, win_token)
elseif losing then
    results = gpg.Turnbased:createParticipantResult(match.id, match.pendingParticipant.id, my_rank, lose_token)
end

local nextParticipant = "AUTOMATCHING_PARTICIPANT"
if match.suggestedNextParticipant.valid and
   match.suggestedNextParticipant.id ~= "" then
	nextParticipant = match.suggestedNextParticipant.id
end
gpg.Turnbased:TakeMyTurn(match_id, match.pendingParticipant.id, nextParticipant, data, function(result)
end)
```

### 创建参与者结果

有时您需要将参与者结果传递给方法。 在 C++ 中，可以直接使用一个结构体，但在Lua，你需要使用一个id。 这个id用于查找结构体并为帮你传递。 您可以重复使用现有的参与者ID或仅创建自己的ID。 该方法还将返回 Lua 对象。

```
local results = gpg.Turnbased:CreateParticipantResult(match_id, participant_id, placement, match_result)
-- use results, or call method and pass participant_id
```

### 完成比赛

```
gpg.Turnbased:FinishMatchDuringMyTurn(match_id, participant_results_id, data, function(result)
	if gpg:IsSuccess(result.result) then
		-- success
	end
end)
```

### 离开比赛

您可以随时离开比赛，但您需要调用正确的方法，以下任一方法。

```
gpg.Turnbased:LeaveMatchDuringMyTurn(match_id, next_participant_id, function(result)
	if gpg:IsSuccess(result.result) then
		-- success
	end
end)

-- 或

gpg.Turnbased:LeaveMatchDuringTheirTurn(match_id, function(result)
	if gpg:IsSuccess(result.result) then
		-- success
	end
end)
```

### 取消比赛

```
gpg.Turnbased:CancelMatch(match_id, function(result)
	if gpg:IsSuccess(result.result) then
		-- success
	end
end)
```

### 忽略比赛

```
gpg.Turnbased:CancelMatch(match_id)
```

### 开始比赛

```
gpg.Turnbased:Rematch(match_id, function(result)
	if gpg:IsSuccess(result.result) then
		-- success
	end
end)
```

### 获取之前的比赛

```
gpg.Turnbased:FetchMatch(match_id, function(result)
	if gpg:IsSuccess(result.result) then
		-- success
	end
end)
```

### 获取所有比赛

```
gpg.Turnbased:FetchMatches(function(result)
	if gpg:IsSuccess(result.result) then
		-- use result.matches here
	end
end)
```

## NearbyConnections (附近联接)

更多文档，参见[Nearby Connections](https://developers.google.com/games/services/cpp/nearby)

### 初始化

初始化 Nearby Connection, 如果不支持当前平台，会返回 false

```lua
local support = gpg.NearbyConnections:Init("{\"LogLevel\":1}",
    function(result)
        if result.InitializationStatus then
            print('GPG Nearby init success')
        else
            print('GPG Nearby init failed')
        end
    end)
if not support then
    print('GPG Nearby is not support ios')
end
```

### 取本地端的id

联接成功后，获取本地端的id

```lua
local endpoint = gpg.NearbyConnections:GetLocalEndpointId();
print('Local Endpoint Id:' .. endpoint)
```

### 获取本地的设备id

```lua
local deviceid = gpg.NearbyConnections:GetLocalDeviceId();
print('Local device id:' .. deviceid)
```

### 服务

开始服务，在附近广播, 让附近的手机可以找到本机

```lua
gpg.NearbyConnections:StartAdvertising(
    "\"name\":\"\",\"duration\":0,\"app_identifiers\":{\"identifier\":\"com.sdkbox.gpg\"},",
    function(result)
        -- start advertising result

        if (1 == result.start_advertising_result.status) then
            print("GPG start advertising result:" .. result.client_id
                .. " status:" .. result.start_advertising_result.status
                .. " local_endpoint_name:" .. result.start_advertising_result.local_endpoint_name)
        else
            print('start advertising failed:' .. result.start_advertising_result.status)
        end
    end,
    function(result)
        --request connect callback

        local remote_endpoint_id = result.request.remote_endpoint_id
        local payload = result.request.payload

        log:d('GPG receive connect request:' .. remote_endpoint_id)

        -- auto accept or query user
        -- 1. accept connect request
        -- invoke AcceptConnectionRequest
        -- gpg.NearbyConnections:AcceptConnectionRequest(remote_endpoint_id, payload, function (result) end)

        -- 2. reject connect request
        -- invoke RejectConnectionRequest
    end)
```

### 停止服务

```lua
gpg.NearbyConnections:StopAdvertising()
```

### 接受联接请求

```lua
gpg.NearbyConnections:AcceptConnectionRequest(
    remote_endpoint_id,
    payload,
    function (result)
        print('event:' .. result.event)
        if 'OnMessageReceived' == result.event then
            print('OnMessageReceived client_id:' .. tostring(result.client_id)
                .. ' remote_endpoint_id:' .. tostring(result.remote_endpoint_id)
                .. ' payload:' .. tostring(result.payload)
                .. ' is_reliable:' .. tostring(result.is_reliable))
        elseif 'OnDisconnected' == result.event then
            print('OnDisconnected client_id:' .. tostring(result.client_id)
                .. ' remote_endpoint_id:' .. tostring(result.remote_endpoint_id))
        else
            print('Unknown event:' .. result.event);
        end
    end)

```

### 拒绝联接请求

```lua
gpg.NearbyConnections:RejectConnectionRequest(remote_endpoint_id)
```

### 开始搜索附近

搜索本地附近打开服务的设备,
duration 参数单位是 milliseconds

```lua
gpg.NearbyConnections:StartDiscovery(server_id, duration,
    function (result)
        if 'OnEndpointFound' == result.event then
            print('found client_id:' .. tostring(result.client_id)
                .. ' endpoint_id:' .. tostring(result.endpoint_details.endpoint_id)
                .. ' device_id:' .. tostring(result.endpoint_details.device_id)
                .. ' name:' .. tostring(result.endpoint_details.name)
                .. ' service_id:' .. tostring(result.endpoint_details.server_id))
        elseif 'OnEndpointLost' == result.event then
            print('endpoint lost')
        else
            print('unknown event')
        end
    end)
```

### 结束搜索

```lua
gpg.NearbyConnections:StopDiscovery()
```

### 发送联接请求

```lua
gpg.NearbyConnections:SendConnectionRequest(
    name, remote_endpoint_id, payload,
    function(result)
        -- connect response callback
        if (1 == result.response.status) then
            print('Connect advertising success');
            local remote_endpoint_id = result.response.remote_endpoint_id;
        else
            print('Connect advertising failed');
        end
    end,
    function(result)
        if 'OnMessageReceived' == result.event then
            print('OnMessageReceived client_id:' .. tostring(result.client_id)
                .. ' remote_endpoint_id:' .. tostring(result.remote_endpoint_id)
                .. ' payload:' .. tostring(result.payload)
                .. ' is_reliable:' .. tostring(result.is_reliable))
        elseif 'OnDisconnected' == result.event then
            print('OnDisconnected client_id:' .. tostring(result.client_id)
                .. ' remote_endpoint_id:' .. tostring(result.remote_endpoint_id))
        else
            print('Unknown event:' .. result.event);
        end
    end)
```

### 发送可靠消息

```lua
gpg.NearbyConnections:SendReliableMessage(remote_endpoint_id1, message)
gpg.NearbyConnections:SendReliableMessage([remote_endpoint_id1, remote_endpoint_id2], message);
```

### 发送不可靠消息

```lua
gpg.NearbyConnections:SendUnreliableMessage(remote_endpoint_id1, message)
gpg.NearbyConnections:SendUnreliableMessage([remote_endpoint_id1, remote_endpoint_id2], message);
```

### 断开

```lua
gpg.NearbyConnections:Disconnect(remote_endpoint_id)
```

### 停止

```lua
gpg.NearbyConnections:Stop()
```
