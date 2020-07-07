%%%----------------------------------------------------------------------
%%% This is the MIT license.
%%%
%%% Copyright (c) 2014 Peter Lemenkov <lemenkov@gmail.com>
%%%
%%% Permission is hereby granted, free of charge, to any person
%%% obtaining a copy of this software and associated documentation
%%% files (the "Software"), to deal in the Software without
%%% restriction, including without limitation the rights to use,
%%% copy, modify, merge, publish, distribute, sublicense, and/or sell
%%% copies of the Software, and to permit persons to whom the
%%% Software is furnished to do so, subject to the following
%%% conditions:
%%%
%%% The above copyright notice and this permission notice shall be
%%% included in all copies or substantial portions of the Software.
%%%
%%% THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
%%% EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
%%% OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
%%% NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
%%% HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
%%% WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
%%% FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
%%% OTHER DEALINGS IN THE SOFTWARE.
%%%----------------------------------------------------------------------

-module(sd_notify).

-export([sd_notify/2, sd_notifyf/3, sd_pid_notify/3, sd_pid_notifyf/4, sd_pid_notify_with_fds/4]).

sd_notify(UnsetEnv, Data) ->
	sd_pid_notify_with_fds(0, UnsetEnv, Data, []).

sd_pid_notify(Pid, UnsetEnv, Data) ->
	sd_pid_notify_with_fds(Pid, UnsetEnv, Data, []).

sd_notifyf(UnsetEnv, Format, Data) ->
	sd_pid_notify_with_fds(0, UnsetEnv, lists:flatten(io_lib:format(Format, Data)), []).

sd_pid_notifyf(Pid, UnsetEnv, Format, Data) ->
	sd_pid_notify_with_fds(Pid, UnsetEnv, lists:flatten(io_lib:format(Format, Data)), []).

sd_pid_notify_with_fds(_Pid, UnsetEnv, Call, _Fds) ->
	error_logger:info_msg("systemd: ~p", [Call]),
	case os:getenv("NOTIFY_SOCKET") of
		false -> {error, not_configured};
		Path ->
			case gen_udp:open(0, [local]) of
				{error, SocketError} ->
					{error, SocketError};
				{ok, Socket} ->
					Result = gen_udp:send(Socket, {local,Path}, 0, Call),
					gen_udp:close(Socket),

					UnsetEnv == true andalso os:unsetenv("NOTIFY_SOCKET"),

					Result
			end
	end.
