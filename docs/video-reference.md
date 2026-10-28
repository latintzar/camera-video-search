# Function reference

[Architecture](video-architecture.md) · [Workflows](workflows.md) · [Setup](video-setup.md)

Named Python definitions and JavaScript function declarations. Arguments list names; source links preserve the containing module and its callbacks.

## Routes

| Method | Path | Source |
| --- | --- | --- |
| GET | `/api/connections/custom/{connector_id}/execution` | [execution](../harness/mechanics/custom_routes.py#L41) |
| POST | `/api/connections/custom/{connector_id}/execution/target` | [target](../harness/mechanics/custom_routes.py#L49) |
| POST | `/api/connections/custom/{connector_id}/execution/activate` | [activate](../harness/mechanics/custom_routes.py#L61) |
| POST | `/api/connections/custom/{connector_id}/execution/test` | [test](../harness/mechanics/custom_routes.py#L78) |
| POST | `/api/connections/custom/{connector_id}/execution/revoke` | [revoke](../harness/mechanics/custom_routes.py#L98) |
| POST | `/api/connections/custom/{connector_id}/execution/stop` | [stop](../harness/mechanics/custom_routes.py#L109) |
| GET | `/api/files/{file_id}/page-preview` | [metadata](../harness/mechanics/document_preview_routes.py#L65) |
| POST | `/api/files/{file_id}/preview` | [prepare](../harness/mechanics/document_preview_routes.py#L71) |
| GET | `/api/files/{file_id}/pages/{page}` | [page](../harness/mechanics/document_preview_routes.py#L101) |
| GET | `/api/harness` | [harness](../harness/mechanics/harness_routes.py#L51) |
| GET | `/api/mcp/connections` | [connections](../harness/mechanics/mcp_host.py#L98) |
| POST | `/api/mcp/connections` | [create_connection](../harness/mechanics/mcp_host.py#L106) |
| DELETE | `/api/mcp/connections/{key}` | [revoke_connection](../harness/mechanics/mcp_host.py#L136) |
| GET | `/api/agents/{agent_id}/phone` | [phone_block](../harness/mechanics/phone_routes.py#L95) |
| POST | `/api/agents/{agent_id}/phone/participants` | [phone_add](../harness/mechanics/phone_routes.py#L100) |
| POST | `/api/agents/{agent_id}/phone/participants/{member_id}/remove` | [phone_remove](../harness/mechanics/phone_routes.py#L106) |
| POST | `/api/agents/{agent_id}/phone/participants/{member_id}` | [phone_participant](../harness/mechanics/phone_routes.py#L112) |
| POST | `/api/agents/{agent_id}/phone/delivery` | [phone_delivery_state](../harness/mechanics/phone_routes.py#L119) |
| POST | `/api/agents/{agent_id}/phone/contact-request` | [phone_contact_request](../harness/mechanics/phone_routes.py#L125) |
| GET | `/api/profile-covers/{cover_id}` | [cover](../harness/mechanics/profile_cover_routes.py#L22) |
| GET | `/api/plugins/installed` | [installed](../harness/runtime/plugin_routes.py#L253) |
| POST | `/api/plugins/{plugin_id}/install` | [install](../harness/runtime/plugin_routes.py#L265) |
| DELETE | `/api/plugins/{plugin_id}/installation` | [remove](../harness/runtime/plugin_routes.py#L286) |
| GET | `/api/organization/chats` | [organization_chats](../harness/server.py#L877) |
| POST | `/api/organization/chats` | [organization_chat](../harness/server.py#L889) |
| GET | `/api/messaging` | [messaging_status](../harness/server.py#L903) |
| POST | `/api/messaging/verification` | [messaging_verification](../harness/server.py#L907) |
| POST | `/api/messaging/verification/confirm` | [messaging_confirm](../harness/server.py#L922) |
| POST | `/api/messaging/hello` | [messaging_hello](../harness/server.py#L937) |
| POST | `/hooks/in/{environment}/{hook_id}` | [incoming_hook](../harness/server.py#L1016) |
| POST | `/api/hooks/{environment}/{hook_id}` | [incoming_hook](../harness/server.py#L1016) |
| GET | `/api/wakes` | [wake_sources](../harness/server.py#L1038) |
| POST | `/api/wakes/endpoints/{endpoint_id}/secret` | [endpoint_secret](../harness/server.py#L1048) |
| POST | `/api/wakes/hooks/{hook_id}/secret` | [reveal_wake_secret](../harness/server.py#L1060) |
| POST | `/hooks/{channel}/{environment}` | [messaging_webhook](../harness/server.py#L1075) |
| GET | `/hooks/{channel}/{environment}` | [messaging_webhook](../harness/server.py#L1075) |
| POST | `/api/messaging/webhook/{environment}/{channel}` | [messaging_webhook](../harness/server.py#L1075) |
| GET | `/api/plugins/catalogue` | [plugins_catalogue](../harness/server.py#L1184) |
| GET | `/api/plugins/{plugin_id}` | [plugin_details](../harness/server.py#L1188) |
| GET | `/api/connections` | [connections](../harness/server.py#L1195) |
| GET | `/api/connections/custom` | [custom_connections](../harness/server.py#L1231) |
| POST | `/api/connections/custom` | [create_custom_connection](../harness/server.py#L1246) |
| GET | `/api/connections/custom/{connector_id}` | [custom_connection](../harness/server.py#L1285) |
| GET | `/api/connections/custom/{connector_id}/package` | [custom_connection_package](../harness/server.py#L1303) |
| POST | `/api/connections/custom/{connector_id}/secrets` | [custom_connection_secret](../harness/server.py#L1312) |
| DELETE | `/api/connections/custom/{connector_id}/secrets/{name}` | [custom_connection_secret_remove](../harness/server.py#L1333) |
| POST | `/api/connections/{provider}/connect` | [connect_provider](../harness/server.py#L1339) |
| GET | `/api/connections/flows/{flow_id}` | [connection_flow](../harness/server.py#L1382) |
| DELETE | `/api/connections/{provider}` | [disconnect_provider](../harness/server.py#L1391) |
| GET | `/api/connections/oauth/callback` | [oauth_landing](../harness/server.py#L1402) |
| GET | `/oauth-callback.js` | [oauth_script](../harness/server.py#L1408) |
| POST | `/api/connections/oauth/callback` | [oauth_callback](../harness/server.py#L1412) |
| GET | `/` | [home](../harness/server.py#L1421) |
| GET | `/app.js` | [script](../harness/server.py#L1441) |
| GET | `/question-box.js` | [question_box_script](../harness/server.py#L1445) |
| GET | `/question-box.css` | [question_box_style](../harness/server.py#L1449) |
| GET | `/brand/rocoto-mark.svg` | [logo](../harness/server.py#L1453) |
| GET | `/fonts/fraunces/fraunces-latin-500-700.woff2` | [wordmark_font](../harness/server.py#L1458) |
| GET | `/connection-brands/{filename}` | [connection_brand](../harness/server.py#L1463) |
| GET | `/vendor/{filename:path}` | [vendor](../harness/server.py#L1469) |
| GET | `/assets/chat-dreamscape.png` | [workspace_artwork](../harness/server.py#L1476) |
| GET | `/assets/search-dreamscape.png` | [workspace_artwork](../harness/server.py#L1476) |
| GET | `/assets/monet-water-lilies.jpg` | [empty_state_artwork](../harness/server.py#L1481) |
| GET | `/style.css` | [style](../harness/server.py#L1486) |
| GET | `/business-summary.js` | [interface_component](../harness/server.py#L1520) |
| GET | `/business-summary.css` | [interface_component](../harness/server.py#L1520) |
| GET | `/settings-shell.js` | [interface_component](../harness/server.py#L1520) |
| GET | `/settings-shell.css` | [interface_component](../harness/server.py#L1520) |
| GET | `/harness-shell.js` | [interface_component](../harness/server.py#L1520) |
| GET | `/workspace-tabs.js` | [interface_component](../harness/server.py#L1520) |
| GET | `/workspace-extensions.js` | [interface_component](../harness/server.py#L1520) |
| GET | `/wake-controls.js` | [interface_component](../harness/server.py#L1520) |
| GET | `/wake-controls.css` | [interface_component](../harness/server.py#L1520) |
| GET | `/workspace-tabs.css` | [interface_component](../harness/server.py#L1520) |
| GET | `/workspace-home.js` | [interface_component](../harness/server.py#L1520) |
| GET | `/workspace-home.css` | [interface_component](../harness/server.py#L1520) |
| GET | `/display-charts.js` | [interface_component](../harness/server.py#L1520) |
| GET | `/display-charts.css` | [interface_component](../harness/server.py#L1520) |
| GET | `/display-canvas.js` | [interface_component](../harness/server.py#L1520) |
| GET | `/display-canvas.css` | [interface_component](../harness/server.py#L1520) |
| GET | `/tool-trail.js` | [interface_component](../harness/server.py#L1520) |
| GET | `/tool-trail.css` | [interface_component](../harness/server.py#L1520) |
| GET | `/rich-content.js` | [interface_component](../harness/server.py#L1520) |
| GET | `/rich-content.css` | [interface_component](../harness/server.py#L1520) |
| GET | `/rich-diagram.js` | [interface_component](../harness/server.py#L1520) |
| GET | `/profile-settings.js` | [interface_component](../harness/server.py#L1520) |
| GET | `/profile-settings.css` | [interface_component](../harness/server.py#L1520) |
| GET | `/plugin-settings.js` | [interface_component](../harness/server.py#L1520) |
| GET | `/plugin-settings.css` | [interface_component](../harness/server.py#L1520) |
| GET | `/messaging-settings.js` | [interface_component](../harness/server.py#L1520) |
| GET | `/messaging-settings.css` | [interface_component](../harness/server.py#L1520) |
| GET | `/workspace-settings.js` | [interface_component](../harness/server.py#L1520) |
| GET | `/workspace-settings.css` | [interface_component](../harness/server.py#L1520) |
| GET | `/business-map.js` | [interface_component](../harness/server.py#L1520) |
| GET | `/business-map.css` | [interface_component](../harness/server.py#L1520) |
| GET | `/rich-diagram.html` | [diagram_component](../harness/server.py#L1526) |
| GET | `/static/vendor/{filename:path}` | [shared_vendor](../harness/server.py#L1547) |
| GET | `/api/source-icon` | [source_icon](../harness/server.py#L1551) |
| GET | `/theme.css` | [theme](../harness/server.py#L1559) |
| GET | `/healthz` | [health](../harness/server.py#L1591) |
| GET | `/api/session` | [session_info](../harness/server.py#L1606) |
| POST | `/api/session` | [login](../harness/server.py#L1614) |
| POST | `/api/session/demo` | [demo_session](../harness/server.py#L1624) |
| DELETE | `/api/session` | [logout](../harness/server.py#L1633) |
| POST | `/api/session/company` | [select_environment](../harness/server.py#L1641) |
| POST | `/api/environment` | [select_environment](../harness/server.py#L1641) |
| GET | `/api/observers` | [observers](../harness/server.py#L1648) |
| POST | `/api/observer` | [observe](../harness/server.py#L1655) |
| DELETE | `/api/observer` | [end_observation](../harness/server.py#L1662) |
| GET | `/api/status` | [status](../harness/server.py#L1669) |
| GET | `/api/business` | [business](../harness/server.py#L1687) |
| GET | `/api/business/map` | [business_map](../harness/server.py#L1698) |
| POST | `/api/business/profile` | [business_profile](../harness/server.py#L1729) |
| POST | `/api/business/onboarding` | [onboarding](../harness/server.py#L1736) |
| GET | `/api/profile/activity` | [profile_activity](../harness/server.py#L1754) |
| GET | `/api/usage` | [usage](../harness/server.py#L1779) |
| POST | `/api/usage/settings` | [usage_settings](../harness/server.py#L1802) |
| GET | `/api/skills/catalogue` | [skills_catalogue](../harness/server.py#L1825) |
| GET | `/api/skills` | [skills_installed](../harness/server.py#L1830) |
| POST | `/api/skills/install` | [skills_install](../harness/server.py#L1835) |
| GET | `/api/ready-agents` | [agent_catalogue](../harness/server.py#L1843) |
| GET | `/api/agents/catalogue` | [agent_catalogue](../harness/server.py#L1843) |
| GET | `/api/workspace/capabilities` | [workspace_capabilities](../harness/server.py#L1896) |
| GET | `/api/agents` | [agents_list](../harness/server.py#L1901) |
| POST | `/api/agents` | [agents_create](../harness/server.py#L1922) |
| GET | `/api/agents/{agent_id}` | [agent_details](../harness/server.py#L1935) |
| POST | `/api/agents/{agent_id}/update` | [agent_update](../harness/server.py#L1939) |
| POST | `/api/agents/{agent_id}/activate` | [agent_activate](../harness/server.py#L1967) |
| POST | `/api/agents/{agent_id}/run` | [agent_run](../harness/server.py#L1971) |
| POST | `/api/agents/{agent_id}/pause` | [agent_pause](../harness/server.py#L1975) |
| GET | `/api/agents/{agent_id}/runs/{run_id}/report` | [agent_report](../harness/server.py#L1983) |
| POST | `/api/chat` | [chat](../harness/server.py#L2006) |
| GET | `/api/chats` | [chats](../harness/server.py#L2117) |
| POST | `/api/chats/{chat_id}/metadata` | [chat_metadata](../harness/server.py#L2126) |
| GET | `/api/chats/{chat_id}` | [child_chat](../harness/server.py#L2137) |
| POST | `/api/chats/{chat_id}/approvals/{request_id}` | [answer_native_approval](../harness/server.py#L2176) |
| POST | `/api/chats/{chat_id}/questions/{request_id}` | [answer_native_question](../harness/server.py#L2209) |
| POST | `/api/chats/{chat_id}/credential-requests/{request_id}` | [answer_credential_request](../harness/server.py#L2244) |
| POST | `/api/chat/{chat_id}/stop` | [stop_chat](../harness/server.py#L2289) |
| POST | `/api/chat/{chat_id}/steer` | [steer_chat](../harness/server.py#L2306) |
| POST | `/api/attachments` | [attachment](../harness/server.py#L2328) |
| GET | `/attachments/{attachment_id}.png` | [attachment_image](../harness/server.py#L2347) |
| GET | `/api/files` | [list_files](../harness/server.py#L2405) |
| GET | `/api/files/{file_id}` | [get_file](../harness/server.py#L2424) |
| GET | `/api/files/{file_id}/content` | [file_content](../harness/server.py#L2432) |
| PATCH | `/api/files/{file_id}` | [rename_file](../harness/server.py#L2441) |
| POST | `/api/files/{file_id}/opened` | [mark_file_opened](../harness/server.py#L2454) |
| GET | `/api/files/{file_id}/download` | [download_file](../harness/server.py#L2463) |
| GET | `/api/files/{file_id}/preview` | [preview_file](../harness/server.py#L2482) |
| GET | `/api/retail/catalog/setup` | [setup](../harness/verticals/retail/catalog_setup_routes.py#L39) |
| POST | `/api/retail/catalog/import` | [import_catalog](../harness/verticals/retail/catalog_setup_routes.py#L44) |
| POST | `/api/retail/catalog/import-file` | [import_file](../harness/verticals/retail/catalog_setup_routes.py#L49) |
| POST | `/api/retail/catalog/photo-handoff` | [handoff](../harness/verticals/retail/catalog_setup_routes.py#L60) |
| GET | `/api/retail/catalog/shelf-crops/{key}/{index}/image` | [shelf_crop](../harness/verticals/retail/catalog_setup_routes.py#L65) |
| GET | `/api/retail/catalog/photos/{key}/image` | [photo](../harness/verticals/retail/catalog_setup_routes.py#L77) |
| GET | `/static/retail/catalog-upload.css` | [mobile_style](../harness/verticals/retail/catalog_setup_routes.py#L87) |
| GET | `/static/retail/catalog-upload.js` | [mobile_script](../harness/verticals/retail/catalog_setup_routes.py#L90) |
| GET | `/pages/retail/catalog-upload/{environment}` | [mobile_page](../harness/verticals/retail/catalog_setup_routes.py#L92) |
| POST | `/pages/retail/catalog-upload/{environment}` | [mobile_upload](../harness/verticals/retail/catalog_setup_routes.py#L96) |
| GET | `/api/catalog/inspections/{inspection_id}/image` | [item_image](../harness/verticals/retail/control_room_routes.py#L127) |
| GET | `/api/retail/viewer/bootstrap` | [bootstrap](../harness/verticals/retail/control_room_routes.py#L145) |
| GET | `/api/retail/viewer` | [control_room_status](../harness/verticals/retail/control_room_routes.py#L156) |
| GET | `/api/tiles/revision` | [control_room_revision](../harness/verticals/retail/control_room_routes.py#L171) |
| GET | `/control-room/` | [control_room_asset](../harness/verticals/retail/control_room_routes.py#L207) |
| GET | `/control-room/{asset:path}` | [control_room_asset](../harness/verticals/retail/control_room_routes.py#L207) |
| GET | `/api/retail/source-links` | [listing](../harness/verticals/retail/link_routes.py#L71) |
| POST | `/api/retail/source-links` | [create](../harness/verticals/retail/link_routes.py#L83) |
| GET | `/api/retail/source-links/{identity}` | [detail](../harness/verticals/retail/link_routes.py#L96) |
| POST | `/api/retail/source-links/{identity}/retry` | [retry](../harness/verticals/retail/link_routes.py#L100) |
| DELETE | `/api/retail/source-links/{identity}` | [cancel](../harness/verticals/retail/link_routes.py#L106) |
| GET | `/api/retail/location/weather` | [location_weather](../harness/verticals/retail/location_context.py#L955) |
| GET | `/api/retail/location/map` | [location_map](../harness/verticals/retail/location_context.py#L964) |
| GET | `/api/retail/location` | [location](../harness/verticals/retail/location_intelligence_routes.py#L11) |
| GET | `/api/retail/catalog/products` | [catalog](../harness/verticals/retail/location_intelligence_routes.py#L24) |
| GET | `/api/retail/visit-basket` | [visit_basket](../harness/verticals/retail/location_intelligence_routes.py#L38) |
| GET | `/api/retail/monitoring/profiles` | [profiles](../harness/verticals/retail/monitoring_routes.py#L187) |
| POST | `/api/retail/monitoring/profiles` | [create_profile](../harness/verticals/retail/monitoring_routes.py#L194) |
| GET | `/api/retail/monitoring/profiles/{profile_id}` | [profile](../harness/verticals/retail/monitoring_routes.py#L199) |
| POST | `/api/retail/monitoring/profiles/{profile_id}` | [update_profile](../harness/verticals/retail/monitoring_routes.py#L203) |
| GET | `/api/retail/monitoring/events` | [events](../harness/verticals/retail/monitoring_routes.py#L209) |
| GET | `/api/retail/monitoring/events/{event_id}` | [event](../harness/verticals/retail/monitoring_routes.py#L216) |
| POST | `/api/retail/monitoring/events` | [commit_event](../harness/verticals/retail/monitoring_routes.py#L222) |
| GET | `/api/agents/{agent_id}/observations` | [observations](../harness/verticals/retail/monitoring_routes.py#L227) |
| POST | `/api/agents/{agent_id}/presentation` | [save_presentation](../harness/verticals/retail/monitoring_routes.py#L232) |
| POST | `/api/chats/{chat_id}/promote-agent` | [promote](../harness/verticals/retail/monitoring_routes.py#L243) |
| GET | `/api/retail/visit-basket` | [legacy_basket](../harness/verticals/retail/realtime_read_routes.py#L152) |
| GET | `/api/retail/realtime/sources/{source_id}/epochs/{epoch_id}/snapshot` | [epoch_snapshot](../harness/verticals/retail/realtime_read_routes.py#L157) |
| GET | `/api/retail/realtime/sources/{source_id}/assets/{asset_id}/snapshot` | [asset_snapshot](../harness/verticals/retail/realtime_read_routes.py#L166) |
| POST | `/api/retail/business/settings` | [business_settings](../harness/verticals/retail/retail_business.py#L99) |
| POST | `/api/retail/business/connections` | [business_connection](../harness/verticals/retail/retail_business.py#L107) |
| POST | `/api/retail/search` | [search](../harness/verticals/retail/retail_http.py#L69) |
| POST | `/api/retail/cameras/review` | [review_cameras](../harness/verticals/retail/retail_http.py#L77) |
| POST | `/api/retail/exports` | [prepare_export](../harness/verticals/retail/retail_http.py#L126) |
| GET | `/api/retail/exports` | [list_exports](../harness/verticals/retail/retail_http.py#L167) |
| GET | `/api/retail/inspection-previews/{receipt_id}/{index}.jpg` | [inspection_preview](../harness/verticals/retail/retail_http.py#L176) |
| GET | `/api/retail/exports/{payload_id}` | [get_export](../harness/verticals/retail/retail_http.py#L212) |
| GET | `/api/retail/exports/{payload_id}/download` | [download_export](../harness/verticals/retail/retail_http.py#L223) |
| GET | `/api/retail/cameras` | [cameras](../harness/verticals/retail/retail_http.py#L236) |
| GET | `/api/retail/cameras/{camera_id}` | [camera_details](../harness/verticals/retail/retail_http.py#L244) |
| POST | `/api/retail/cameras/{camera_id}/context` | [camera_context_draft](../harness/verticals/retail/retail_http.py#L252) |
| POST | `/api/retail/cameras/{camera_id}/confirm` | [confirm_camera_context](../harness/verticals/retail/retail_http.py#L263) |
| GET | `/api/retail/library` | [source_library](../harness/verticals/retail/retail_http.py#L274) |
| GET | `/api/retail/assets/{asset_id}` | [source_asset](../harness/verticals/retail/retail_http.py#L284) |
| GET | `/clips/{clip_id}.mp4` | [evidence_clip](../harness/verticals/retail/retail_http.py#L309) |
| GET | `/thumbnails/{clip_id}.jpg` | [thumbnail](../harness/verticals/retail/retail_http.py#L324) |
| GET | `/downloads/{clip_id}.mp4` | [download_clip](../harness/verticals/retail/retail_http.py#L340) |
| GET | `/api/retail/clip/{clip_id}/manifest` | [download_manifest](../harness/verticals/retail/retail_http.py#L399) |
| GET | `/api/retail/clip/{clip_id}` | [clip_details](../harness/verticals/retail/retail_http.py#L422) |
| GET | `/originals/{asset_id}` | [original_source](../harness/verticals/retail/retail_http.py#L464) |
| GET | `/static/retail/assets/demo-companies/sij-acroni.png` | [sij_acroni_logo](../harness/verticals/retail/retail_http.py#L477) |
| GET | `/static/retail/control-room.js` | [control_room_script](../harness/verticals/retail/retail_http.py#L482) |
| GET | `/static/retail/assets/camera-providers/{filename}` | [camera_provider_asset](../harness/verticals/retail/retail_http.py#L487) |
| GET | `/static/retail/retail-scope.js` | [retail_scope_component](../harness/verticals/retail/retail_http.py#L498) |
| GET | `/static/retail/retail-scope.css` | [retail_scope_component](../harness/verticals/retail/retail_http.py#L498) |
| GET | `/static/retail/retail-ui.js` | [retail_component](../harness/verticals/retail/retail_http.py#L509) |
| GET | `/static/retail/retail-ui.css` | [retail_component](../harness/verticals/retail/retail_http.py#L509) |
| GET | `/static/retail/retail-shell.js` | [retail_component](../harness/verticals/retail/retail_http.py#L509) |
| GET | `/static/retail/tracker-canvas.js` | [retail_component](../harness/verticals/retail/retail_http.py#L509) |
| GET | `/static/retail/tracker-canvas.css` | [retail_component](../harness/verticals/retail/retail_http.py#L509) |
| GET | `/static/retail/camera-streams.js` | [retail_component](../harness/verticals/retail/retail_http.py#L509) |
| GET | `/static/retail/camera-streams.css` | [retail_component](../harness/verticals/retail/retail_http.py#L509) |
| GET | `/api/retail/scope` | [graph](../harness/verticals/retail/retail_scope_routes.py#L70) |
| GET | `/api/retail/scope/events` | [graph_events](../harness/verticals/retail/retail_scope_routes.py#L77) |
| POST | `/api/retail/scope/{kind}` | [change](../harness/verticals/retail/retail_scope_routes.py#L82) |
| GET | `/api/retail/chats/{chat_id}/scope` | [chat_scope](../harness/verticals/retail/retail_scope_routes.py#L90) |
| PUT | `/api/retail/chats/{chat_id}/scope` | [change_chat_scope](../harness/verticals/retail/retail_scope_routes.py#L96) |
| GET | `/api/retail/library/imports` | [imports](../harness/verticals/retail/source_routes.py#L231) |
| POST | `/api/retail/library/imports` | [begin](../harness/verticals/retail/source_routes.py#L259) |
| GET | `/api/retail/library/imports/{upload_id}` | [detail](../harness/verticals/retail/source_routes.py#L277) |
| PATCH | `/api/retail/library/imports/{upload_id}/content` | [content](../harness/verticals/retail/source_routes.py#L282) |
| POST | `/api/retail/library/imports/{upload_id}/complete` | [complete](../harness/verticals/retail/source_routes.py#L319) |
| DELETE | `/api/retail/library/imports/{upload_id}` | [cancel](../harness/verticals/retail/source_routes.py#L328) |
| GET | `/api/retail/sources` | [sources](../harness/verticals/retail/source_routes.py#L335) |
| POST | `/api/retail/sources` | [add_source](../harness/verticals/retail/source_routes.py#L345) |
| GET | `/api/retail/sources/{source_id}` | [source](../harness/verticals/retail/source_routes.py#L353) |
| GET | `/api/retail/storage/{connector_id}` | [status](../harness/verticals/retail/storage_routes.py#L25) |
| POST | `/api/retail/storage/{connector_id}/approve` | [approve](../harness/verticals/retail/storage_routes.py#L29) |
| POST | `/api/retail/storage/{connector_id}/run` | [run](../harness/verticals/retail/storage_routes.py#L38) |
| POST | `/api/retail/storage/{connector_id}/pause` | [pause](../harness/verticals/retail/storage_routes.py#L47) |
| GET | `/sources/{source_id}/assets/{asset_id}/snapshot` | [source_snapshot](../backend/realtime/routes.py#L118) |
| GET | `/sources/{source_id}/epochs/{epoch_id}/snapshot` | [epoch_snapshot](../backend/realtime/routes.py#L139) |
| GET | `/replays/{run_id}` | [replay_status](../backend/realtime/routes.py#L170) |

## Configuration

Values belong in recipient-owned private runtime configuration.

`DATABASE_URL`, `ROCOTO_AGENT_AUTH_MODE`, `ROCOTO_BROWSE_SESSIONS`, `ROCOTO_BUILTIN_CAPABILITIES_CONFIG`, `ROCOTO_CAPABILITY_SPEND_CONFIG`, `ROCOTO_CONNECTION_WRITE_PROVIDERS`, `ROCOTO_CUSTOM_EXECUTOR_ENABLED`, `ROCOTO_DOCUMENT_PREVIEWS_ENABLED`, `ROCOTO_DOCUMENT_PREVIEW_RECEIPT_SHA256`, `ROCOTO_MANAGED_SPENDING_MODE`, `ROCOTO_MESSAGING_CONFIG`, `ROCOTO_NATIVE_WRITE_PROVIDERS`, `ROCOTO_OPENAI_API_KEY`, `ROCOTO_OPERATOR_ID`, `ROCOTO_OPERATOR_NAME`, `ROCOTO_PHONE_SPEND_CONFIG`, `ROCOTO_PUBLIC_ORIGIN`, `ROCOTO_STATE_DIRECTORY`, `ROCOTO_VIDEO_DEMO_BROWSING`, `ROCOTO_VIDEO_MESSAGING_CONFIG`, `ROCOTO_VIDEO_OPERATOR_NAME`, `ROCOTO_VIDEO_PHONE_SPEND_CONFIG`, `ROCOTO_VIDEO_PUBLIC_ORIGIN`, `RUNTIME_DATABASE_URL`, `VIDEO_OPERATIONS_MODAL_WORKSPACE`, `XDG_STATE_HOME`

## Definitions

### backend/realtime/configuration.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [maintained_core](../backend/realtime/configuration.py#L45) | self |  |
| [unique_ids](../backend/realtime/configuration.py#L60) | cls, values |  |
| [event_type](../backend/realtime/configuration.py#L77) | self |  |
| [unique_interests](../backend/realtime/configuration.py#L89) | self |  |
| [_clock](../backend/realtime/configuration.py#L102) | body |  |
| [_core_events](../backend/realtime/configuration.py#L109) |  |  |
| [_zone_available](../backend/realtime/configuration.py#L113) | con, context, source_id, zone_id, kind |  |
| [_support](../backend/realtime/configuration.py#L136) | parameters, actual_input, tracker |  |
| [validate_admission](../backend/realtime/configuration.py#L151) | con, context, source_id, event | Enforce actual acknowledged configuration only for managed observations. |
| [__init__](../backend/realtime/configuration.py#L232) | self, store |  |
| [_head](../backend/realtime/configuration.py#L235) | self, con, context, source_id |  |
| [_camera](../backend/realtime/configuration.py#L242) | self, con, context, source_id |  |
| [_capacity](../backend/realtime/configuration.py#L249) | self, con, context, body, records |  |
| [_validate](../backend/realtime/configuration.py#L262) | self, con, context, source_id, intent |  |
| [_compile](../backend/realtime/configuration.py#L272) | self, intent, validation |  |
| [requirements](../backend/realtime/configuration.py#L302) | self, context, source_id |  |
| [_bounded](../backend/realtime/configuration.py#L318) | context, body |  |
| [propose](../backend/realtime/configuration.py#L322) | self, context, source_id, proposal_id, raw_intent |  |
| [validate](../backend/realtime/configuration.py#L367) | self, context, source_id, proposal_id |  |
| [_proposal](../backend/realtime/configuration.py#L376) | self, con, context, source_id, proposal_id |  |
| [activate](../backend/realtime/configuration.py#L390) | self, context, source_id, proposal_id | Set desired configuration atomically. There is deliberately no enqueue. |
| [_worker](../backend/realtime/configuration.py#L447) | self, con, context, source_id |  |
| [worker_configuration](../backend/realtime/configuration.py#L454) | self, context, source_id | Private adapter read. Never expose this shape through customer tools. |
| [acknowledge](../backend/realtime/configuration.py#L478) | self, context, source_id, raw_ack |  |
| [status](../backend/realtime/configuration.py#L592) | self, context, source_id, limit |  |

### backend/realtime/continuity.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [bounded_ids](../backend/realtime/continuity.py#L30) | self |  |
| [complete_clock](../backend/realtime/continuity.py#L61) | self |  |
| [preserve_existing_receipts](../backend/realtime/continuity.py#L79) | self, handler |  |
| [retained_configuration](../backend/realtime/continuity.py#L86) | self |  |
| [same_elapsed_time](../backend/realtime/continuity.py#L109) | self |  |
| [preserve_existing_intervals](../backend/realtime/continuity.py#L124) | self, handler |  |
| [reported_frame_s](../backend/realtime/continuity.py#L156) | run, frame | Source time of one frame in a retained run: its start plus frame index over frame rate. |
| [reported_birth_id](../backend/realtime/continuity.py#L161) | namespace, sidecar_sha256, tracker_id, first_frame | Identify the first report in one retained run, independently of physical entry. |
| [_contains](../backend/realtime/continuity.py#L168) | outer, inner |  |
| [_stream_window](../backend/realtime/continuity.py#L172) | mapping, local |  |
| [__init__](../backend/realtime/continuity.py#L180) | self, store |  |
| [_epoch](../backend/realtime/continuity.py#L183) | self, con, context, source_id, epoch_id |  |
| [_mapping](../backend/realtime/continuity.py#L195) | self, con, context, source_id, mapping_id |  |
| [_room](../backend/realtime/continuity.py#L207) | self, con, context, body |  |
| [_retry](../backend/realtime/continuity.py#L219) | self, con, context, table, key, source_id, value, body |  |
| [start_epoch](../backend/realtime/continuity.py#L231) | self, context, source_id, record |  |
| [end_epoch](../backend/realtime/continuity.py#L280) | self, context, source_id, record |  |
| [map_artifact](../backend/realtime/continuity.py#L324) | self, context, source_id, record |  |
| [_validate_clock](../backend/realtime/continuity.py#L387) | self, con, context, source_id, asset, local, lineage |  |
| [validate_input](../backend/realtime/continuity.py#L402) | self, con, context, source_id, body |  |
| [event_reason](../backend/realtime/continuity.py#L463) | self, con, context, source_id, event, replay_context |  |
| [_track_evidence](../backend/realtime/continuity.py#L494) | self, con, context, source_id, receipt_id, receipt_sha, tracker_id, birth_id, window, state |  |
| [validate_visit](../backend/realtime/continuity.py#L519) | self, con, context, record, attrs |  |
| [record_segment](../backend/realtime/continuity.py#L549) | self, context, source_id, record |  |
| [validate_binding](../backend/realtime/continuity.py#L609) | self, con, context, source_id, event, subject |  |
| [_playback_rows](../backend/realtime/continuity.py#L643) | self, con, context, source_id, epoch_id, playhead, table |  |
| [_playback](../backend/realtime/continuity.py#L675) | self, con, context, source_id, epoch_id, playhead | Fresh tracker-only descriptor under current RLS and subject lifecycle. |
| [intervals](../backend/realtime/continuity.py#L697) | mapping, local |  |
| [playback](../backend/realtime/continuity.py#L818) | self, context, source_id, epoch_id, at_s | Read receipt-backed selectable visitors, even with zero admitted activities. |
| [segments](../backend/realtime/continuity.py#L828) | self, context, source_id, visit_subject_id, limit |  |

### backend/realtime/contracts.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_opaque_id](../backend/realtime/contracts.py#L31) | value | Validate an opaque existing identifier without assigning it semantics. |
| [_utc_datetime](../backend/realtime/contracts.py#L39) | value |  |
| [_finite_decimal](../backend/realtime/contracts.py#L45) | value |  |
| [_validate_capabilities](../backend/realtime/contracts.py#L81) | cls, values |  |
| [_validate_deadline](../backend/realtime/contracts.py#L89) | cls, value |  |
| [_validate_finite](../backend/realtime/contracts.py#L101) | cls, value |  |
| [_validate_order](../backend/realtime/contracts.py#L105) | self |  |
| [_preserve_recording_wire](../backend/realtime/contracts.py#L129) | self, handler |  |
| [_validate_receipts](../backend/realtime/contracts.py#L139) | cls, values |  |
| [_validate_effective_at](../backend/realtime/contracts.py#L157) | cls, value |  |
| [_validate_event_refs](../backend/realtime/contracts.py#L182) | cls, values |  |
| [_validate_json_value](../backend/realtime/contracts.py#L192) | value, depth, ancestors | Validate JSON shape, finite numbers, depth, and cycles before encoding. |
| [_encoded_json](../backend/realtime/contracts.py#L225) | value, label |  |
| [_validate_timestamps](../backend/realtime/contracts.py#L252) | cls, value |  |
| [_validate_event_type](../backend/realtime/contracts.py#L257) | cls, value |  |
| [_serialize_event](../backend/realtime/contracts.py#L263) | self, handler |  |
| [_validate_envelope](../backend/realtime/contracts.py#L272) | self |  |
| [_validate_changes](../backend/realtime/contracts.py#L308) | cls, value |  |

### backend/realtime/identity.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../backend/realtime/identity.py#L32) | self, code, message |  |
| [__post_init__](../backend/realtime/identity.py#L56) | self |  |
| [from_context](../backend/realtime/identity.py#L70) | cls, context, environment | Convert the existing trusted platform-owner ``require_owner`` result. |
| [_identifier](../backend/realtime/identity.py#L93) | value, field |  |
| [_email](../backend/realtime/identity.py#L99) | value |  |
| [_reason](../backend/realtime/identity.py#L108) | value |  |
| [_fingerprint](../backend/realtime/identity.py#L116) | company_id, operator_id, email, reason |  |
| [_require_control_connection](../backend/realtime/identity.py#L128) | connection | Fail closed when a runtime role reaches this control-plane mutation. |
| [reconcile_verified_login](../backend/realtime/identity.py#L142) | connection, company_id, operator_id, verified_email, owner, request_id, reason | Bind ``verified_email`` to one existing imported operator. |

### backend/realtime/import_stream.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [canonical](../backend/realtime/import_stream.py#L41) | value |  |
| [digest](../backend/realtime/import_stream.py#L46) | value |  |
| [raw_digest](../backend/realtime/import_stream.py#L50) | value |  |
| [checked_json](../backend/realtime/import_stream.py#L54) | value, maximum |  |
| [identity_record](../backend/realtime/import_stream.py#L60) | value |  |
| [_read_db](../backend/realtime/import_stream.py#L78) | path |  |
| [_has_table](../backend/realtime/import_stream.py#L88) | con, name |  |
| [_reference](../backend/realtime/import_stream.py#L95) | event |  |
| [_profile_key](../backend/realtime/import_stream.py#L106) | profile_id, revision |  |
| [export_snapshot](../backend/realtime/import_stream.py#L116) | state, identity_path, owner, source_ids, export_reference | Read committed native admissions from a host-selected private snapshot. |
| [validate_export](../backend/realtime/import_stream.py#L264) | manifest, expected_sha256 | Validate a reviewed neutral artifact; its checksum is integrity, not authorization. |
| [_utc](../backend/realtime/import_stream.py#L431) | seconds |  |
| [plan_import](../backend/realtime/import_stream.py#L435) | manifest, expected_sha256 | Create inspectable SDK commands; empty exports remain explicitly empty. |
| [import_export](../backend/realtime/import_stream.py#L592) | context, manifest, expected_sha256, dry_run, retained_export_path, store | Apply idempotent SDK phases after host identity commissioning and review. |
| [write_export](../backend/realtime/import_stream.py#L664) | path, manifest | Retain private raw admission evidence before using the import service. |
| [main](../backend/realtime/import_stream.py#L682) |  | Read-only source export CLI; database import stays an authenticated host call. |

### backend/realtime/import_tracker_run.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../backend/realtime/import_tracker_run.py#L92) | self, code, message |  |
| [_need](../backend/realtime/import_tracker_run.py#L97) | condition, code, message |  |
| [_sha](../backend/realtime/import_tracker_run.py#L102) | data |  |
| [_whole](../backend/realtime/import_tracker_run.py#L106) | value, low, high |  |
| [_entry](../backend/realtime/import_tracker_run.py#L110) | root, relative | One retained path below the resolved run root, reached through real directories. |
| [_read](../backend/realtime/import_tracker_run.py#L122) | root, relative, limit |  |
| [_media](../backend/realtime/import_tracker_run.py#L132) | root, relative |  |
| [_json](../backend/realtime/import_tracker_run.py#L144) | data, relative |  |
| [sidecar_digest](../backend/realtime/import_tracker_run.py#L151) | files | One sealed digest of a per-frame tracker directory, from (name, bytes) pairs. |
| [_frame_rows](../backend/realtime/import_tracker_run.py#L165) | data, relative | The tracker rows of one frame file, in the producer's own record shape. |
| [_sidecar](../backend/realtime/import_tracker_run.py#L200) | root, relative, count |  |
| [_reports](../backend/realtime/import_tracker_run.py#L213) | frames | Each raw tracker ID with its runs of consecutive reported frames, end exclusive. |
| [_recording](../backend/realtime/import_tracker_run.py#L226) | record, listed, clip | The producer's own run receipt: one complete recording on an exact frame clock. |
| [_application](../backend/realtime/import_tracker_run.py#L265) | data, clip, record | The retained application configuration names this view's media, sidecar and one pass. |
| [value](../backend/realtime/import_tracker_run.py#L273) | section, name |  |
| [_end_of_stream](../backend/realtime/import_tracker_run.py#L300) | data, clip |  |
| [_tracks](../backend/realtime/import_tracker_run.py#L310) | value, clip, record, frames | The producer's JSON conversion agrees with the per-frame sidecar, row for row. |
| [_sample_mapping](../backend/realtime/import_tracker_run.py#L333) | value, clip, record | Every encoded frame names the publisher frame it holds, on the encoded clock. |
| [_inventory](../backend/realtime/import_tracker_run.py#L371) | root |  |
| [identifiers](../backend/realtime/import_tracker_run.py#L386) | clip | The stable identifiers of one view. Content hashes stay out of every identifier. |
| [_verify_view](../backend/realtime/import_tracker_run.py#L402) | root, clip, listed, shared | Read and verify one view's retained evidence. Every check precedes any record. |
| [_plan_view](../backend/realtime/import_tracker_run.py#L448) | root, clip, listed, shared | State the exact SDK records one verified view becomes. |
| [evidence](../backend/realtime/import_tracker_run.py#L457) | name, sha256 |  |
| [subject](../backend/realtime/import_tracker_run.py#L576) | registration |  |
| [plan_run](../backend/realtime/import_tracker_run.py#L724) | run_root, reference, company_id, principal_id, clips | Verify the retained run and plan every record. Reads files only. |
| [summary](../backend/realtime/import_tracker_run.py#L800) | plan | The reviewable plan: identifiers, sealed hashes, counts and visitor boundaries per view. |
| [require_reviewed](../backend/realtime/import_tracker_run.py#L820) | plan, expected_sha256 | The checksum is integrity of the reviewed dry run; authority stays with the database. |
| [_context](../backend/realtime/import_tracker_run.py#L829) | plan |  |
| [_authority](../backend/realtime/import_tracker_run.py#L840) | context, store | The restricted role, a commissioned company and a principal that configures and ingests. |
| [_retained](../backend/realtime/import_tracker_run.py#L852) | context, store, view | Compare every record this view already holds with its plan, before any write. |
| [_rows](../backend/realtime/import_tracker_run.py#L936) | context, store, source_id |  |
| [_import_view](../backend/realtime/import_tracker_run.py#L949) | context, store, view | One view through the maintained SDK. Every call returns its retained record on a retry. |
| [import_run](../backend/realtime/import_tracker_run.py#L1022) | plan, store | Import every planned view, or refuse the whole run before its first write. |
| [_identity](../backend/realtime/import_tracker_run.py#L1074) | path |  |
| [_receipt_path](../backend/realtime/import_tracker_run.py#L1083) | value, root | A new file in an existing folder outside the repository and outside the retained run. |
| [_write_receipt](../backend/realtime/import_tracker_run.py#L1107) | path, receipt |  |
| [_apply](../backend/realtime/import_tracker_run.py#L1119) | plan, dsn | Open only the restricted pool for this command's lifetime. |
| [main](../backend/realtime/import_tracker_run.py#L1134) | argv |  |

### backend/realtime/locations.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_tracker_keys](../backend/realtime/locations.py#L124) | cls, value |  |
| [_size](../backend/realtime/locations.py#L130) | value | UTF-8 bytes of a document as PostgreSQL prints jsonb. |
| [_document](../backend/realtime/locations.py#L157) | value, limit, name |  |
| [_listing](../backend/realtime/locations.py#L166) | value, limit, name |  |
| [_sha](../backend/realtime/locations.py#L174) | value |  |
| [_iso](../backend/realtime/locations.py#L178) | moment |  |
| [_day](../backend/realtime/locations.py#L185) | value |  |
| [_stamp](../backend/realtime/locations.py#L193) | value |  |
| [_keys](../backend/realtime/locations.py#L199) | value |  |
| [_moment](../backend/realtime/locations.py#L211) | value | An ISO 8601 time with its offset, as a record's body carries it. |
| [_run](../backend/realtime/locations.py#L222) | row | A run as the tools and the page read it: no principal, no stamp, no lease. |
| [_tracker](../backend/realtime/locations.py#L249) | row |  |
| [_order](../backend/realtime/locations.py#L268) | tracker |  |
| [_flags](../backend/realtime/locations.py#L273) | tracker |  |
| [__init__](../backend/realtime/locations.py#L320) | self, store |  |
| [_tx](../backend/realtime/locations.py#L326) | self, context, capability | One scoped transaction; a refusal of the tables arrives as the SDK's own error. |
| [_location](../backend/realtime/locations.py#L338) | self, con, context, location_id, lock, reach | The location row behind the wall. `reach` names the capability a write takes on each camera. |
| [_budget](../backend/realtime/locations.py#L360) | self, con, context, limits, added |  |
| [_bump](../backend/realtime/locations.py#L365) | con, context, location_id | A tracker change moves what a commit expects and what the page shows. |
| [_identity](../backend/realtime/locations.py#L375) | row |  |
| [register_location](../backend/realtime/locations.py#L384) | self, context, location_id, collection, business_type | Give a location its PostgreSQL identity. An exact retry returns the same row. |
| [bind_source](../backend/realtime/locations.py#L421) | self, context, location_id, source_id, camera_id, body | Bind one camera source to its location. A camera belongs to one location. |
| [locations](../backend/realtime/locations.py#L474) | self, context | The company's locations this principal reads, with how many trackers each holds. |
| [_definition](../backend/realtime/locations.py#L490) | definition |  |
| [_trackers](../backend/realtime/locations.py#L522) | self, con, context, location_id, include_retired |  |
| [_one_tracker](../backend/realtime/locations.py#L531) | self, con, context, tracker_id |  |
| [install_trackers](../backend/realtime/locations.py#L538) | self, context, location_id, definitions | Record tracker definitions for a location. An exact retry returns the same rows. |
| [_revision](../backend/realtime/locations.py#L632) | con, context, location_id, item, part, revision |  |
| [save_revision](../backend/realtime/locations.py#L647) | self, context, tracker_id, part, body, expected_revision | Append the next revision of one part of a company's tracker. |
| [activate](../backend/realtime/locations.py#L700) | self, context, tracker_id, expected_head, definition, script, presentation, state | Point a company's tracker at saved revisions or change its state, as one head move. |
| [trackers](../backend/realtime/locations.py#L760) | self, context, location_id, include_retired | The location's trackers with their active revision bodies: Core first, then by key. |
| [_records](../backend/realtime/locations.py#L773) | kind, rows, basis, occurred_key, source_key |  |
| [_write_records](../backend/realtime/locations.py#L801) | self, con, context, limits, location_id, kind, basis, prepared, replace_all | Insert new rows, rewrite changed ones, and turn the rows that left a rebuild inactive. |
| [put_records](../backend/realtime/locations.py#L869) | self, context, location_id, kind, rows, basis, replace_all, occurred_key, source_key | Write ingested or configured records of one kind; returns how many rows changed. |
| [load](../backend/realtime/locations.py#L901) | self, context, location_id | Everything one tracker run reads, bounded by the context's event and byte limits. |
| [_output](../backend/realtime/locations.py#L1012) | value |  |
| [commit](../backend/realtime/locations.py#L1059) | self, context, location_id, changes, run_id, lease_token, expected_run_seq | Commit one run in one transaction: all of it lands, or the location stays as it was. |
| [home](../backend/realtime/locations.py#L1318) | self, context, location_id, known_revision | The page keys of a location with their revision. No event is read. |
| [claim_events](../backend/realtime/locations.py#L1397) | self, context, location_id, limit, lease_seconds | Lease pending live outbox rows of location cameras, grouped by location. |
| [input_stamp](../backend/realtime/locations.py#L1451) | self, context, location_id | A digest of what a run of this location reads. It moves when an input is added or changed. |
| [_state](../backend/realtime/locations.py#L1471) | self, con, context, location_id, now |  |
| [state](../backend/realtime/locations.py#L1493) | self, context, location_id, now | The location's schedule as the probe and the tools read it. Times are epoch seconds. |
| [policy](../backend/realtime/locations.py#L1502) | self, context, location_id | The location's run policy with its revision. |
| [set_policy](../backend/realtime/locations.py#L1507) | self, context, location_id, changes, expected_revision | Change the location's run policy. `expected_revision` is the revision the caller read. |
| [request](../backend/realtime/locations.py#L1533) | self, context, location_id, by, only | Ask for a pass now. Requests made before the pass starts become that one pass. |
| [claim](../backend/realtime/locations.py#L1551) | self, context, location_id, trigger, stamp, day, lease_seconds | Take the location's lease and open a run. None while another pass holds the lease. |
| [finish](../backend/realtime/locations.py#L1647) | self, context, run_id, lease_token, status, stamp, day, period, derived, outputs, errors, skipped, wall_ms, error, published | Close a run and free its lease; the holder's token is the key. |
| [runs](../backend/realtime/locations.py#L1758) | self, context, location_id, limit | The location's runs, newest first. The newest 200 are kept. |
| [last_run](../backend/realtime/locations.py#L1774) | self, context, location_id | The newest run of one location, or of the company's locations this principal reads. |

### backend/realtime/media.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../backend/realtime/media.py#L11) | self, store |  |
| [bindings](../backend/realtime/media.py#L14) | self, context, references | Join each reference to its current source grant, active camera, epoch and mapping. |

### backend/realtime/module_store.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_json_bytes](../backend/realtime/module_store.py#L32) | value, limit |  |
| [_wire](../backend/realtime/module_store.py#L44) | value | Round-trip JSON values so asyncpg/Decimal values cannot escape the API. |
| [_bounded_digest](../backend/realtime/module_store.py#L50) | value | Hash the full bounded wire, without the small event helper limit. |
| [_playhead](../backend/realtime/module_store.py#L56) | value |  |
| [__init__](../backend/realtime/module_store.py#L68) | self, store |  |
| [_lane](../backend/realtime/module_store.py#L73) | source |  |
| [_original_source](../backend/realtime/module_store.py#L77) | source, source_id |  |
| [_context_key](../backend/realtime/module_store.py#L83) | value |  |
| [_epoch_asset_id](../backend/realtime/module_store.py#L87) | epoch_id |  |
| [_history](../backend/realtime/module_store.py#L92) | self, con, context, source_id, source_asset_id, max_events, epoch_id | Read a bounded cursor after latest-revision selection. |
| [_binding_manifest](../backend/realtime/module_store.py#L140) | bindings, current_revisions |  |
| [_result](../backend/realtime/module_store.py#L157) | self, row, context, status |  |
| [_collect](../backend/realtime/module_store.py#L179) | self, con, context, source_id, asset_id, playhead, epoch_id |  |
| [_pending](../backend/realtime/module_store.py#L307) | collected, playhead |  |
| [_empty](../backend/realtime/module_store.py#L323) | collected, playhead |  |
| [_ephemeral_result](../backend/realtime/module_store.py#L337) | self, collected, context, playhead |  |
| [project_at](../backend/realtime/module_store.py#L370) | self, context, source_id, asset_id, at_s | Read an ephemeral source-time projection without creating a row. |
| [_verify_epoch](../backend/realtime/module_store.py#L384) | self, con, context, source_id, epoch_id |  |
| [_with_playback](../backend/realtime/module_store.py#L400) | self, con, context, source_id, epoch_id, result, playhead |  |
| [project_epoch_at](../backend/realtime/module_store.py#L409) | self, context, source_id, epoch_id, at_s | Read an epoch projection at stream time without creating a row. |
| [refresh_epoch](../backend/realtime/module_store.py#L432) | self, context, source_id, epoch_id, at_s | Persist one tracker epoch ordered by its host stream clock. |
| [latest_epoch](../backend/realtime/module_store.py#L528) | self, context, source_id, epoch_id, at_s | Read the stored head for an epoch namespace. |
| [refresh](../backend/realtime/module_store.py#L569) | self, context, source_id, asset_id, at_s | Persist the canonical head; playhead reads use :meth:`project_at`. |
| [_authorize_manifest](../backend/realtime/module_store.py#L664) | self, con, context, source_id, manifest | Recheck every retained subject dependency through its current grant. |
| [_fetch_bounded_projection](../backend/realtime/module_store.py#L692) | self, con, context, projection_id | Preflight size and current dependency grants before fetching snapshot JSON. |
| [get](../backend/realtime/module_store.py#L722) | self, context, projection_id | Read one projection through its current source grant. |
| [latest](../backend/realtime/module_store.py#L733) | self, context, source_id, asset_id, at_s | Read the canonical stored head; source-time reads are ephemeral. |

### backend/realtime/modules.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_number](../backend/realtime/modules.py#L76) | value |  |
| [_text](../backend/realtime/modules.py#L80) | value, fallback |  |
| [_reference](../backend/realtime/modules.py#L84) | event |  |
| [_subject](../backend/realtime/modules.py#L88) | binding |  |
| [_one](../backend/realtime/modules.py#L97) | bindings, role |  |
| [project_observations](../backend/realtime/modules.py#L105) | facts, at_s | Return JSON-safe journey, basket, interest and stock views as of source time. |
| [visit](../backend/realtime/modules.py#L163) | subject |  |
| [observe](../backend/realtime/modules.py#L183) | v, start, end |  |
| [close_interval](../backend/realtime/modules.py#L191) | v, name, end, ref |  |
| [wire](../backend/realtime/modules.py#L485) | value |  |
| [project_continuous_observations](../backend/realtime/modules.py#L514) | facts, at_s, epoch_id | Project one tracker epoch across rotated artifacts on its stream clock. |

### backend/realtime/provision.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../backend/realtime/provision.py#L33) | self, code, message |  |
| [_text](../backend/realtime/provision.py#L42) | value, field, maximum |  |
| [_timestamp](../backend/realtime/provision.py#L53) | value |  |
| [_manifest](../backend/realtime/provision.py#L72) | saved_identity, principals, environment_alias, display_name, migration_source |  |
| [_conflict](../backend/realtime/provision.py#L149) | code, message |  |
| [import_workspace_identity](../backend/realtime/provision.py#L153) | connection, saved_identity, principals, environment_alias, display_name, migration_source, migration_role | Import once or validate an exact retry, without committing the caller's transaction. |

### backend/realtime/provision_host.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../backend/realtime/provision_host.py#L50) | self, code, message |  |
| [_identity](../backend/realtime/provision_host.py#L55) | info |  |
| [_open_private](../backend/realtime/provision_host.py#L59) | state, parts, maximum | Open one private regular file below the state directory, following no symbolic link. |
| [read_identity](../backend/realtime/provision_host.py#L99) | state, environment | The saved workspace identity and the SHA-256 of its exact bytes. |
| [read_principals](../backend/realtime/provision_host.py#L114) | state, environment | The environment's display name and its principals, from an unchanged read-only store. |
| [_sha256](../backend/realtime/provision_host.py#L167) | value |  |
| [_tool_digests](../backend/realtime/provision_host.py#L172) |  |  |
| [_connect](../backend/realtime/provision_host.py#L180) | dsn |  |
| [_reserve_receipt](../backend/realtime/provision_host.py#L186) | path |  |
| [_validate](../backend/realtime/provision_host.py#L195) | options, dsn |  |
| [_import](../backend/realtime/provision_host.py#L211) | connection, options, arguments |  |
| [import_identity](../backend/realtime/provision_host.py#L253) | options, dsn, connect | Run the dry run or the real import and return its receipt. |
| [parser](../backend/realtime/provision_host.py#L315) |  |  |
| [main](../backend/realtime/provision_host.py#L331) | argv, environ |  |

### backend/realtime/read_contract.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [bounded_playhead](../backend/realtime/read_contract.py#L15) | value | Accept finite nonnegative source seconds within the public wire bounds. |
| [public_projection](../backend/realtime/read_contract.py#L30) | result, epoch_id | Expose business data and playback evidence, keeping private lineage inside the SDK. |

### backend/realtime/replay.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_seconds](../backend/realtime/replay.py#L30) | value, positive |  |
| [_id](../backend/realtime/replay.py#L40) | value |  |
| [_json](../backend/realtime/replay.py#L46) | value |  |
| [_unsupported](../backend/realtime/replay.py#L57) | value |  |
| [_key](../backend/realtime/replay.py#L61) | prefix, *values |  |
| [replay_context_dict](../backend/realtime/replay.py#L139) | context | Omit absent optional fields to preserve already-compiled plan/event hashes. |
| [_planned_dict](../backend/realtime/replay.py#L147) | event |  |
| [canonical_event](../backend/realtime/replay.py#L159) | self |  |
| [to_dict](../backend/realtime/replay.py#L177) | self |  |
| [to_dict](../backend/realtime/replay.py#L207) | self |  |
| [from_dict](../backend/realtime/replay.py#L211) | cls, value |  |
| [_reference](../backend/realtime/replay.py#L235) | value |  |
| [compile_replay](../backend/realtime/replay.py#L247) | company_id, run_id, sources, receipts, records, loops, rate, readiness_lag_s | Compile accepted history; emit only after every actual input window ends. |
| [initial_cursor](../backend/realtime/replay.py#L493) | plan |  |
| [due_events](../backend/realtime/replay.py#L497) | plan, cursor, elapsed_s, limit | Return due work plus an uncommitted checkpoint; never advance on reads. |
| [seek](../backend/realtime/replay.py#L534) | plan, elapsed_s | Inspect a playback position without skipping or rewinding committed work. |
| [restore_plan](../backend/realtime/replay.py#L542) | value | Restore an immutable database plan and verify its compiler digest/identities. |
| [exact](../backend/realtime/replay.py#L554) | model, data |  |

### backend/realtime/replay_store.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_wire](../backend/realtime/replay_store.py#L37) | value |  |
| [_unsupported](../backend/realtime/replay_store.py#L49) | value |  |
| [_bytes](../backend/realtime/replay_store.py#L53) | value |  |
| [__init__](../backend/realtime/replay_store.py#L58) | self, store |  |
| [_request](../backend/realtime/replay_store.py#L63) | sources, loops, rate, readiness_lag_s |  |
| [_load_inputs](../backend/realtime/replay_store.py#L108) | self, con, context, sources, loops |  |
| [start](../backend/realtime/replay_store.py#L198) | self, context, run_id, sources, loops, rate, readiness_lag_s | Persist one immutable plan, commission its sources, then start the DB clock. |
| [_prepare](../backend/realtime/replay_store.py#L260) | self, context, run_id, plan |  |
| [_elapsed](../backend/realtime/replay_store.py#L344) | row, now |  |
| [_row](../backend/realtime/replay_store.py#L350) | self, con, context, run_id, lock, include_plan |  |
| [_status](../backend/realtime/replay_store.py#L369) | row |  |
| [get](../backend/realtime/replay_store.py#L383) | self, context, run_id |  |
| [inspect_plan](../backend/realtime/replay_store.py#L387) | self, context, run_id |  |
| [tick](../backend/realtime/replay_store.py#L402) | self, context, run_id, limit |  |
| [pause](../backend/realtime/replay_store.py#L466) | self, context, run_id, expected_revision |  |
| [resume](../backend/realtime/replay_store.py#L469) | self, context, run_id, expected_revision |  |
| [_set_paused](../backend/realtime/replay_store.py#L472) | self, context, run_id, expected_revision, paused |  |

### backend/realtime/replay_worker.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_pairs](../backend/realtime/replay_worker.py#L22) | plan |  |
| [_summary](../backend/realtime/replay_worker.py#L41) | result | Return a bounded receipt without copying the potentially large snapshot. |
| [__init__](../backend/realtime/replay_worker.py#L66) | self, replay, modules |  |
| [run_once](../backend/realtime/replay_worker.py#L70) | self, context, run_id, limit |  |
| [run_once](../backend/realtime/replay_worker.py#L103) | context, run_id, limit | Convenience boundary for a scheduled ordinary-host invocation. |

### backend/realtime/routes.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_principal_id](../backend/realtime/routes.py#L42) | ctx | Resolve the session's verified email to the durable imported principal. |
| [_context](../backend/realtime/routes.py#L69) | request, ctx |  |
| [_read_context](../backend/realtime/routes.py#L97) | request, ctx |  |
| [_error](../backend/realtime/routes.py#L103) | exc |  |
| [source_snapshot](../backend/realtime/routes.py#L118) | source_id, asset_id, request, at_s, context |  |
| [epoch_snapshot](../backend/realtime/routes.py#L139) | source_id, epoch_id, request, at_s, context | Read one admitted continuous session on its mapped stream clock. |
| [replay_status](../backend/realtime/routes.py#L170) | run_id, request, context |  |

### backend/realtime/store.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [scope_for_company](../backend/realtime/store.py#L50) | company_id | Preserve safe canonical labels; otherwise use a collision-resistant label. |
| [_encoded](../backend/realtime/store.py#L64) | value, limit |  |
| [_digest](../backend/realtime/store.py#L73) | value |  |
| [_identifier](../backend/realtime/store.py#L77) | value |  |
| [_transaction](../backend/realtime/store.py#L87) | self, context, capability |  |
| [_source](../backend/realtime/store.py#L129) | self, con, context, source_id, writing |  |
| [register_source](../backend/realtime/store.py#L151) | self, context, source_id, kind, metadata |  |
| [register_profile](../backend/realtime/store.py#L193) | self, context, source_id, revision_id, event_types |  |
| [_register_profile](../backend/realtime/store.py#L197) | self, con, context, source_id, revision_id, event_types |  |
| [record_receipt](../backend/realtime/store.py#L241) | self, context, source_id, receipt_id, body |  |
| [_lock_budget](../backend/realtime/store.py#L296) | self, con, context |  |
| [_usage](../backend/realtime/store.py#L304) | self, con, context |  |
| [_check_bytes](../backend/realtime/store.py#L308) | limits, usage, added |  |
| [_evidence_reason](../backend/realtime/store.py#L312) | self, con, context, source_id, event, replay_context |  |
| [admit](../backend/realtime/store.py#L395) | self, context, source_id, event |  |
| [_admit](../backend/realtime/store.py#L399) | self, con, context, source_id, event, replay_context |  |
| [depth](../backend/realtime/store.py#L408) | value |  |
| [read_events](../backend/realtime/store.py#L550) | self, context, source_id, after_sequence, limit |  |
| [claim_outbox](../backend/realtime/store.py#L577) | self, context, limit, lease_seconds, lane |  |
| [finish_outbox](../backend/realtime/store.py#L614) | self, context, outbox_id, lease_token |  |

### backend/realtime/subjects.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_preserve_recording_identity](../backend/realtime/subjects.py#L57) | self, handler |  |
| [quantity_evidence](../backend/realtime/subjects.py#L75) | self |  |
| [identity](../backend/realtime/subjects.py#L89) | self |  |
| [interval](../backend/realtime/subjects.py#L112) | self |  |
| [typed](../backend/realtime/subjects.py#L132) | self |  |
| [_identity](../backend/realtime/subjects.py#L147) | record |  |
| [__init__](../backend/realtime/subjects.py#L162) | self, store |  |
| [_read](../backend/realtime/subjects.py#L165) | self, con, context, subject_id, revision |  |
| [get](../backend/realtime/subjects.py#L205) | self, context, subject_id, revision |  |
| [_budget](../backend/realtime/subjects.py#L209) | self, con, context, additional_bytes |  |
| [register](../backend/realtime/subjects.py#L219) | self, context, registration, expected_revision |  |
| [_evidence](../backend/realtime/subjects.py#L322) | self, con, context, record, attrs, parent_record |  |
| [bind_event](../backend/realtime/subjects.py#L421) | self, context, source_id, event_id, event_revision, bindings |  |
| [_bind_event](../backend/realtime/subjects.py#L425) | self, con, context, source_id, event_id, event_revision, bindings |  |
| [_validate_binding](../backend/realtime/subjects.py#L489) | self, con, context, source_id, event, binding, subject |  |
| [_event_bindings](../backend/realtime/subjects.py#L519) | self, con, context, source_id, event_id, event_revision |  |
| [event_bindings](../backend/realtime/subjects.py#L551) | self, context, source_id, event_id, event_revision |  |
| [replay_entities](../backend/realtime/subjects.py#L555) | self, context, source_id, event_id, event_revision |  |
| [_replay_entities](../backend/realtime/subjects.py#L559) | self, con, context, source_id, event_id, event_revision |  |
| [copy_replay_event](../backend/realtime/subjects.py#L580) | self, context, source_id, event_id, event_revision |  |
| [_copy_replay_event](../backend/realtime/subjects.py#L584) | self, con, context, source_id, event_id, event_revision | Copy and seal with event admission/cursor in the caller's transaction. |
| [copy](../backend/realtime/subjects.py#L626) | subject |  |

### harness/deploy/build_preview.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [source_paths](../harness/deploy/build_preview.py#L29) | repo, prefix | Use Git in a checkout or the explicit reviewed inventory in a source export. |
| [maintained_read_files](../harness/deploy/build_preview.py#L47) | repo | Package the shared read closure, the host commands and the immutable schema chain. |
| [artifact_root](../harness/deploy/build_preview.py#L67) | vertical_id |  |
| [artifact_destination](../harness/deploy/build_preview.py#L71) | repo, output, source, vertical_id |  |
| [source_layout](../harness/deploy/build_preview.py#L80) | here, vertical_id | Use the runtime's layout rather than maintaining a second folder inventory. |
| [template_files](../harness/deploy/build_preview.py#L89) | here, vertical_id | Every file the selected vertical declares, including Python and prompts. |
| [artifact_files](../harness/deploy/build_preview.py#L97) | repo, here, vertical_id | Tracked shared code/assets and the selected vertical, with missing Python reported. |
| [copy_artifact](../harness/deploy/build_preview.py#L130) | repo, output, selected, vertical_id | Copy each selected regular file to its place in the artifact layout. |
| [build_output](../harness/deploy/build_preview.py#L155) | here, vertical_id |  |
| [build](../harness/deploy/build_preview.py#L163) | vertical_id |  |

### harness/deploy/connections/configure_google.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [save_registration](../harness/deploy/connections/configure_google.py#L30) | state, directory, client_id, client_secret, public_origin |  |
| [main](../harness/deploy/connections/configure_google.py#L74) |  |  |

### harness/deploy/document-preview/closure/broker_service.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [main](../harness/deploy/document-preview/closure/broker_service.py#L15) |  |  |

### harness/deploy/document-preview/closure/document_preview_contract.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__post_init__](../harness/deploy/document-preview/closure/document_preview_contract.py#L22) | self |  |
| [parse](../harness/deploy/document-preview/closure/document_preview_contract.py#L27) | cls, value |  |
| [validate_manifest](../harness/deploy/document-preview/closure/document_preview_contract.py#L31) | manifest, files, request, original_sha256, original_bytes |  |
| [require](../harness/deploy/document-preview/closure/document_preview_contract.py#L32) | condition |  |

### harness/deploy/document-preview/closure/native_executor.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__post_init__](../harness/deploy/document-preview/closure/native_executor.py#L54) | self |  |
| [key](../harness/deploy/document-preview/closure/native_executor.py#L60) | self |  |
| [__post_init__](../harness/deploy/document-preview/closure/native_executor.py#L71) | self |  |
| [name](../harness/deploy/document-preview/closure/native_executor.py#L90) | self |  |
| [_command](../harness/deploy/document-preview/closure/native_executor.py#L94) | timeout, input, *argv |  |
| [__init__](../harness/deploy/document-preview/closure/native_executor.py#L122) | self, root, size_bytes |  |
| [mount](../harness/deploy/document-preview/closure/native_executor.py#L128) | self, key |  |
| [unmount](../harness/deploy/document-preview/closure/native_executor.py#L169) | self, volume |  |
| [__init__](../harness/deploy/document-preview/closure/native_executor.py#L177) | self, volumes |  |
| [mount](../harness/deploy/document-preview/closure/native_executor.py#L182) | self, key |  |
| [volume_path](../harness/deploy/document-preview/closure/native_executor.py#L185) | self, key |  |
| [unmount](../harness/deploy/document-preview/closure/native_executor.py#L188) | self, volume |  |
| [inspect](../harness/deploy/document-preview/closure/native_executor.py#L191) | self, spec |  |
| [flags](../harness/deploy/document-preview/closure/native_executor.py#L197) | spec |  |
| [start](../harness/deploy/document-preview/closure/native_executor.py#L211) | self, spec, capability |  |
| [pause](../harness/deploy/document-preview/closure/native_executor.py#L244) | self, spec |  |
| [unpause](../harness/deploy/document-preview/closure/native_executor.py#L250) | self, spec |  |
| [stop](../harness/deploy/document-preview/closure/native_executor.py#L253) | self, spec |  |
| [_path_parts](../harness/deploy/document-preview/closure/native_executor.py#L260) | value |  |
| [_checked_directory](../harness/deploy/document-preview/closure/native_executor.py#L269) | parent, name, uid |  |
| [snapshot_outputs](../harness/deploy/document-preview/closure/native_executor.py#L278) | workspace, destination, uid, paths | Snapshot owned ordinary files without following a mutable path or symlink. |
| [copy_file](../harness/deploy/document-preview/closure/native_executor.py#L293) | parent, name, relative |  |
| [walk](../harness/deploy/document-preview/closure/native_executor.py#L327) | parent, prefix, depth |  |
| [__init__](../harness/deploy/document-preview/closure/native_executor.py#L383) | self, root, run_root, backend, app_uid, app_gid, clock, socket_owner, socket_group |  |
| [_row](../harness/deploy/document-preview/closure/native_executor.py#L408) | self, key |  |
| [_spec](../harness/deploy/document-preview/closure/native_executor.py#L411) | self, row |  |
| [_update](../harness/deploy/document-preview/closure/native_executor.py#L417) | self, key, status, volume |  |
| [_validate](../harness/deploy/document-preview/closure/native_executor.py#L423) | self, scope, lease |  |
| [prepare](../harness/deploy/document-preview/closure/native_executor.py#L435) | self, scope |  |
| [_freeze_sockets](../harness/deploy/document-preview/closure/native_executor.py#L464) | self, spec |  |
| [install_packages](../harness/deploy/document-preview/closure/native_executor.py#L482) | self, scope, lease, reader, writer | Reserve the lease before accepting a bounded stream; no host paths. |
| [start](../harness/deploy/document-preview/closure/native_executor.py#L535) | self, scope, lease, capability |  |
| [_stop_row](../harness/deploy/document-preview/closure/native_executor.py#L557) | self, row |  |
| [stop](../harness/deploy/document-preview/closure/native_executor.py#L585) | self, scope, lease | Caller revokes model/MCP grants first; removal kills the whole process tree. |
| [reconcile](../harness/deploy/document-preview/closure/native_executor.py#L601) | self | After broker restart, remove every recorded worker before accepting input. |
| [expire_prepared](../harness/deploy/document-preview/closure/native_executor.py#L612) | self |  |
| [snapshot](../harness/deploy/document-preview/closure/native_executor.py#L623) | self, scope, lease, paths |  |
| [output_file](../harness/deploy/document-preview/closure/native_executor.py#L667) | self, scope, lease, snapshot_id, index |  |
| [_read_package_frame](../harness/deploy/document-preview/closure/native_executor.py#L684) | reader, limit |  |
| [_read_frame](../harness/deploy/document-preview/closure/native_executor.py#L690) | reader |  |
| [_write_frame](../harness/deploy/document-preview/closure/native_executor.py#L697) | writer, kind, body |  |
| [__init__](../harness/deploy/document-preview/closure/native_executor.py#L705) | self, broker, path |  |
| [start](../harness/deploy/document-preview/closure/native_executor.py#L712) | self |  |
| [expire](../harness/deploy/document-preview/closure/native_executor.py#L726) |  |  |
| [close](../harness/deploy/document-preview/closure/native_executor.py#L732) | self |  |
| [_connection](../harness/deploy/document-preview/closure/native_executor.py#L750) | self, reader, writer |  |
| [_fields](../harness/deploy/document-preview/closure/native_executor.py#L830) | value, allowed |  |
| [_reply](../harness/deploy/document-preview/closure/native_executor.py#L836) | writer, value |  |
| [_relay](../harness/deploy/document-preview/closure/native_executor.py#L844) | process, reader, writer |  |
| [stdin](../harness/deploy/document-preview/closure/native_executor.py#L845) |  |  |
| [output](../harness/deploy/document-preview/closure/native_executor.py#L856) | source, kind |  |
| [__init__](../harness/deploy/document-preview/closure/native_executor.py#L877) | self, writer |  |
| [write](../harness/deploy/document-preview/closure/native_executor.py#L880) | self, data |  |
| [drain](../harness/deploy/document-preview/closure/native_executor.py#L885) | self |  |
| [write_eof](../harness/deploy/document-preview/closure/native_executor.py#L888) | self |  |
| [close](../harness/deploy/document-preview/closure/native_executor.py#L891) | self |  |
| [__init__](../harness/deploy/document-preview/closure/native_executor.py#L898) | self, client, scope, lease, reader, writer |  |
| [_pump](../harness/deploy/document-preview/closure/native_executor.py#L907) | self |  |
| [wait](../harness/deploy/document-preview/closure/native_executor.py#L934) | self |  |
| [stop](../harness/deploy/document-preview/closure/native_executor.py#L937) | self |  |
| [__init__](../harness/deploy/document-preview/closure/native_executor.py#L946) | self, socket_path |  |
| [_connect](../harness/deploy/document-preview/closure/native_executor.py#L949) | self, operation, scope, lease, **values |  |
| [_request](../harness/deploy/document-preview/closure/native_executor.py#L969) | self, operation, scope, lease, **values |  |
| [prepare](../harness/deploy/document-preview/closure/native_executor.py#L975) | self, scope |  |
| [install_packages](../harness/deploy/document-preview/closure/native_executor.py#L978) | self, scope, lease, selection |  |
| [start](../harness/deploy/document-preview/closure/native_executor.py#L1019) | self, scope, lease, gateway_capability |  |
| [stop](../harness/deploy/document-preview/closure/native_executor.py#L1023) | self, scope, lease |  |
| [snapshot](../harness/deploy/document-preview/closure/native_executor.py#L1026) | self, scope, lease, paths |  |
| [read_output](../harness/deploy/document-preview/closure/native_executor.py#L1029) | self, scope, lease, snapshot_id, index |  |

### harness/deploy/document-preview/closure/native_package_mount.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [encoded](../harness/deploy/document-preview/closure/native_package_mount.py#L30) | value |  |
| [digest](../harness/deploy/document-preview/closure/native_package_mount.py#L33) | value |  |
| [parts](../harness/deploy/document-preview/closure/native_package_mount.py#L36) | value |  |
| [validate_metadata](../harness/deploy/document-preview/closure/native_package_mount.py#L44) | value, company, owner |  |
| [selection_metadata](../harness/deploy/document-preview/closure/native_package_mount.py#L86) | selection |  |
| [_read_json](../harness/deploy/document-preview/closure/native_package_mount.py#L93) | path |  |
| [native_config](../harness/deploy/document-preview/closure/native_package_mount.py#L98) | root, metadata | Enable original skills; explicitly disable every bundled MCP server. |
| [seal](../harness/deploy/document-preview/closure/native_package_mount.py#L128) | root |  |
| [ensure_mount_target](../harness/deploy/document-preview/closure/native_package_mount.py#L138) | volume | Never follow model-created links when preparing Docker's nested target. |
| [open_source](../harness/deploy/document-preview/closure/native_package_mount.py#L150) | root, relative | Held descriptor chain prevents app-owned source symlinks from redirecting. |
| [toml_value](../harness/deploy/document-preview/closure/native_package_mount.py#L166) | value | Codex -c expects TOML values; JSON object colons are not TOML assignments. |

### harness/deploy/document-preview/closure/source_media.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_require](../harness/deploy/document-preview/closure/source_media.py#L62) | condition, code |  |
| [_identifier](../harness/deploy/document-preview/closure/source_media.py#L67) | value, pattern |  |
| [_number](../harness/deploy/document-preview/closure/source_media.py#L71) | value |  |
| [_json](../harness/deploy/document-preview/closure/source_media.py#L75) | value |  |
| [__post_init__](../harness/deploy/document-preview/closure/source_media.py#L86) | self |  |
| [key](../harness/deploy/document-preview/closure/source_media.py#L94) | self |  |
| [__post_init__](../harness/deploy/document-preview/closure/source_media.py#L104) | self |  |
| [__post_init__](../harness/deploy/document-preview/closure/source_media.py#L118) | self |  |
| [parse](../harness/deploy/document-preview/closure/source_media.py#L134) | cls, value |  |
| [manifest_request](../harness/deploy/document-preview/closure/source_media.py#L139) | self, scope, collection, checksum |  |
| [wall_seconds](../harness/deploy/document-preview/closure/source_media.py#L157) | self |  |
| [image](../harness/deploy/document-preview/closure/source_media.py#L161) | self |  |
| [arguments](../harness/deploy/document-preview/closure/source_media.py#L165) | self |  |
| [name](../harness/deploy/document-preview/closure/source_media.py#L175) | self |  |
| [original](../harness/deploy/document-preview/closure/source_media.py#L179) | self |  |
| [output](../harness/deploy/document-preview/closure/source_media.py#L183) | self |  |
| [__init__](../harness/deploy/document-preview/closure/source_media.py#L189) | self, root |  |
| [volume_path](../harness/deploy/document-preview/closure/source_media.py#L195) | self, key, generation |  |
| [mount](../harness/deploy/document-preview/closure/source_media.py#L198) | self, spec |  |
| [flags](../harness/deploy/document-preview/closure/source_media.py#L202) | self, spec |  |
| [start](../harness/deploy/document-preview/closure/source_media.py#L213) | self, spec |  |
| [wait](../harness/deploy/document-preview/closure/source_media.py#L230) | self, spec |  |
| [stop](../harness/deploy/document-preview/closure/source_media.py#L235) | self, spec |  |
| [present](../harness/deploy/document-preview/closure/source_media.py#L236) |  |  |
| [unmount](../harness/deploy/document-preview/closure/source_media.py#L244) | self, spec |  |
| [_directory](../harness/deploy/document-preview/closure/source_media.py#L250) | path |  |
| [_identity](../harness/deploy/document-preview/closure/source_media.py#L260) | info |  |
| [_copy_original](../harness/deploy/document-preview/closure/source_media.py#L264) | fd, destination, uid, size, checksum |  |
| [_read_json](../harness/deploy/document-preview/closure/source_media.py#L283) | path, limit |  |
| [_validate_manifest](../harness/deploy/document-preview/closure/source_media.py#L293) | manifest, files, scope, collection, size, checksum, sealed |  |
| [_validate_derived_manifest](../harness/deploy/document-preview/closure/source_media.py#L369) | manifest, files, scope, collection, size, checksum, request | Validate fixed-profile claims and sealed byte hashes without media decoding. |
| [dimensions](../harness/deploy/document-preview/closure/source_media.py#L406) | row |  |
| [source_frame](../harness/deploy/document-preview/closure/source_media.py#L410) | frame |  |
| [_snapshot](../harness/deploy/document-preview/closure/source_media.py#L478) | spec, scope, size, checksum, worker_uid | Copy ordinary files only after the whole worker is confirmed absent. |
| [_drain](../harness/deploy/document-preview/closure/source_media.py#L550) | task | Finish an owned bounded operation even after repeated cancellation. |
| [__init__](../harness/deploy/document-preview/closure/source_media.py#L563) | self, root, backend, app_uid, app_gid, clock, worker_uid, document_previews |  |
| [_row](../harness/deploy/document-preview/closure/source_media.py#L579) | self, key |  |
| [_derivation_body](../harness/deploy/document-preview/closure/source_media.py#L582) | self, row |  |
| [_spec](../harness/deploy/document-preview/closure/source_media.py#L586) | self, row |  |
| [_valid](../harness/deploy/document-preview/closure/source_media.py#L595) | self, scope, lease |  |
| [_update](../harness/deploy/document-preview/closure/source_media.py#L601) | self, key, status, confirmed, error, result |  |
| [submit](../harness/deploy/document-preview/closure/source_media.py#L605) | self, scope, generation, collection, original_sha256, original_bytes, expires_at, original_fd |  |
| [derive](../harness/deploy/document-preview/closure/source_media.py#L609) | self, scope, generation, collection, original_sha256, original_bytes, expires_at, original_fd, derivation |  |
| [preview](../harness/deploy/document-preview/closure/source_media.py#L615) | self, scope, document, **values |  |
| [_submit](../harness/deploy/document-preview/closure/source_media.py#L622) | self, scope, generation, collection, original_sha256, original_bytes, expires_at, original_fd, derivation |  |
| [_expiry](../harness/deploy/document-preview/closure/source_media.py#L670) | self, expires |  |
| [heartbeat](../harness/deploy/document-preview/closure/source_media.py#L673) | self, scope, lease, expires_at |  |
| [_run](../harness/deploy/document-preview/closure/source_media.py#L682) | self, scope, row, spec |  |
| [enforce_expiry](../harness/deploy/document-preview/closure/source_media.py#L686) |  |  |
| [cleanup](../harness/deploy/document-preview/closure/source_media.py#L731) |  |  |
| [status](../harness/deploy/document-preview/closure/source_media.py#L745) | self, scope, lease |  |
| [stop](../harness/deploy/document-preview/closure/source_media.py#L752) | self, scope, lease |  |
| [_reconcile](../harness/deploy/document-preview/closure/source_media.py#L770) | self, row |  |
| [recover_lease](../harness/deploy/document-preview/closure/source_media.py#L781) | self, scope, generation |  |
| [recover](../harness/deploy/document-preview/closure/source_media.py#L789) | self |  |
| [output_file](../harness/deploy/document-preview/closure/source_media.py#L794) | self, scope, lease, index |  |
| [release](../harness/deploy/document-preview/closure/source_media.py#L809) | self, scope, lease |  |
| [close](../harness/deploy/document-preview/closure/source_media.py#L818) | self |  |
| [_send_packet](../harness/deploy/document-preview/closure/source_media.py#L826) | sock, payload |  |
| [_receive_packet](../harness/deploy/document-preview/closure/source_media.py#L831) | sock |  |
| [_send_json](../harness/deploy/document-preview/closure/source_media.py#L837) | sock, value |  |
| [_receive_json](../harness/deploy/document-preview/closure/source_media.py#L845) | sock |  |
| [_receive_request](../harness/deploy/document-preview/closure/source_media.py#L861) | sock, app_uid |  |
| [__init__](../harness/deploy/document-preview/closure/source_media.py#L881) | self, broker, path |  |
| [start](../harness/deploy/document-preview/closure/source_media.py#L886) | self |  |
| [_accept](../harness/deploy/document-preview/closure/source_media.py#L907) | self |  |
| [_connection](../harness/deploy/document-preview/closure/source_media.py#L917) | self, sock |  |
| [close](../harness/deploy/document-preview/closure/source_media.py#L973) | self |  |
| [__init__](../harness/deploy/document-preview/closure/source_media.py#L986) | self, socket_path, server_uid |  |
| [_connect](../harness/deploy/document-preview/closure/source_media.py#L989) | self, operation, scope, lease, original_fd, **values |  |
| [_exchange](../harness/deploy/document-preview/closure/source_media.py#L1004) | self, operation, scope, lease, **values |  |
| [_request](../harness/deploy/document-preview/closure/source_media.py#L1008) | self, operation, scope, lease, **values |  |
| [submit](../harness/deploy/document-preview/closure/source_media.py#L1011) | self, scope, **values |  |
| [derive](../harness/deploy/document-preview/closure/source_media.py#L1014) | self, scope, **values |  |
| [preview](../harness/deploy/document-preview/closure/source_media.py#L1018) | self, scope, **values |  |
| [_admit](../harness/deploy/document-preview/closure/source_media.py#L1022) | self, operation, scope, **values |  |
| [exchange](../harness/deploy/document-preview/closure/source_media.py#L1026) |  |  |
| [recover](../harness/deploy/document-preview/closure/source_media.py#L1037) | self, scope, generation |  |
| [status](../harness/deploy/document-preview/closure/source_media.py#L1041) | self, scope, lease |  |
| [heartbeat](../harness/deploy/document-preview/closure/source_media.py#L1044) | self, scope, lease, expires_at |  |
| [stop](../harness/deploy/document-preview/closure/source_media.py#L1047) | self, scope, lease |  |
| [release](../harness/deploy/document-preview/closure/source_media.py#L1052) | self, scope, lease |  |
| [read_output](../harness/deploy/document-preview/closure/source_media.py#L1055) | self, scope, lease, index |  |
| [_main](../harness/deploy/document-preview/closure/source_media.py#L1084) | args |  |

### harness/deploy/migrate_state.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_now](../harness/deploy/migrate_state.py#L41) |  |  |
| [_hash](../harness/deploy/migrate_state.py#L44) | path |  |
| [_json](../harness/deploy/migrate_state.py#L48) | path |  |
| [_write](../harness/deploy/migrate_state.py#L51) | path, data |  |
| [_stamp](../harness/deploy/migrate_state.py#L57) | path |  |
| [_regular](../harness/deploy/migrate_state.py#L62) | path |  |
| [_sqlite_files](../harness/deploy/migrate_state.py#L67) | source | SHM is a reader/writer coordination cache, never database content. |
| [_private_database](../harness/deploy/migrate_state.py#L78) | source | Let SQLite recover only a private, identity-checked database/WAL copy. |
| [_workspace](../harness/deploy/migrate_state.py#L102) | relative |  |
| [_include](../harness/deploy/migrate_state.py#L109) | relative, indexed |  |
| [_check_idle](../harness/deploy/migrate_state.py#L132) | source |  |
| [_json_value](../harness/deploy/migrate_state.py#L146) | value |  |
| [_cosmos_generations](../harness/deploy/migrate_state.py#L149) | source | Verified committed indexes; retained/uncommitted directories stay at source. |
| [inventory](../harness/deploy/migrate_state.py#L167) | source | Read-only selection audit; credentials and unindexed experiment media stay on dev. |
| [_relocate](../harness/deploy/migrate_state.py#L202) | value, source, target, fields |  |
| [_backup](../harness/deploy/migrate_state.py#L213) | source, destination |  |
| [_relocate_database](../harness/deploy/migrate_state.py#L224) | path, source, target | Only mutable operational links move; immutable event bodies remain verbatim. |
| [build_snapshot](../harness/deploy/migrate_state.py#L239) | source, bundle, target, quiesced, native_exports |  |
| [verify_snapshot](../harness/deploy/migrate_state.py#L353) | bundle, installed_root |  |
| [install_snapshot](../harness/deploy/migrate_state.py#L375) | bundle, target, quiesced |  |
| [export_native](../harness/deploy/migrate_state.py#L419) | source, output, codex_bin | Local thread/read only. No thread/start, turn, provider inference or auth export. |
| [main](../harness/deploy/migrate_state.py#L450) |  |  |

### harness/deploy/migration/app_server.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/deploy/migration/app_server.py#L12) | self, process |  |
| [write](../harness/deploy/migration/app_server.py#L20) | self, value, guard |  |
| [_read](../harness/deploy/migration/app_server.py#L27) | self |  |
| [rpc](../harness/deploy/migration/app_server.py#L48) | self, method, params, guard |  |
| [close](../harness/deploy/migration/app_server.py#L59) | self |  |

### harness/deploy/migration/config.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [cli_args](../harness/deploy/migration/config.py#L26) | config |  |

### harness/deploy/migration/history.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_thread](../harness/deploy/migration/history.py#L25) | response |  |
| [_image_mime](../harness/deploy/migration/history.py#L32) | data |  |
| [_image](../harness/deploy/migration/history.py#L44) | part, attachment_root, item_id | Copy existing references or owned attachment bytes; never fetch a URL. |
| [_public_history](../harness/deploy/migration/history.py#L82) | thread, cwd |  |
| [history_export](../harness/deploy/migration/history.py#L175) | thread, state, chat_id, owner_principal_id | Export only host-owned public messages; never export credentials/native internals. |
| [history_export_path](../harness/deploy/migration/history.py#L191) | state, chat_id |  |
| [load_history_export](../harness/deploy/migration/history.py#L195) | state, chat_id, existing_id, owner_principal_id | Accept one private host export only for the exact company/chat/owner/native binding. |

### harness/deploy/migration/legacy/isolated_native.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/deploy/migration/legacy/isolated_native.py#L31) | self, path |  |
| [__call__](../harness/deploy/migration/legacy/isolated_native.py#L39) | self, scope, receive, send |  |
| [__aenter__](../harness/deploy/migration/legacy/isolated_native.py#L47) | self |  |
| [__aexit__](../harness/deploy/migration/legacy/isolated_native.py#L70) | self, *args |  |
| [__init__](../harness/deploy/migration/legacy/isolated_native.py#L85) | self, scope, lease, launch, client, listener, stack, storage_scope |  |
| [thread_params](../harness/deploy/migration/legacy/isolated_native.py#L100) | self, instructions, tools |  |
| [bind_mcp](../harness/deploy/migration/legacy/isolated_native.py#L107) | self, app | Called once, in the lease task, after host verifies the native root ID. |
| [drain_stderr](../harness/deploy/migration/legacy/isolated_native.py#L151) | self |  |
| [stop](../harness/deploy/migration/legacy/isolated_native.py#L156) | self | Safe from a separate Stop task; context managers exit on their owner. |
| [__init__](../harness/deploy/migration/legacy/isolated_native.py#L178) | self, auth, company_id, enabled, client, gateway_factory, package_store |  |
| [revoke_plugin](../harness/deploy/migration/legacy/isolated_native.py#L185) | self, principal_id, plugin_id | HTTP removes selection first; failed Stops remain tracked for retry. |
| [_selection](../harness/deploy/migration/legacy/isolated_native.py#L199) | self, scope |  |
| [lease](../harness/deploy/migration/legacy/isolated_native.py#L211) | self, scope, run_id, workspace_binding |  |

### harness/deploy/migration/legacy/isolated_turn.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [isolated_instructions](../harness/deploy/migration/legacy/isolated_turn.py#L36) | product |  |
| [portable_input](../harness/deploy/migration/legacy/isolated_turn.py#L47) | content, state | Embed only already-authorized attachment bytes; expose no host paths. |
| [public_continuation](../harness/deploy/migration/legacy/isolated_turn.py#L64) | record | The native homes differ. Carry public messages once, never private state. |
| [__init__](../harness/deploy/migration/legacy/isolated_turn.py#L81) | self, agent, chat_id, dataset, run, connection, session, root_thread |  |
| [admit](../harness/deploy/migration/legacy/isolated_turn.py#L98) | self, native_id, seen |  |
| [child_event](../harness/deploy/migration/legacy/isolated_turn.py#L140) | self, identity |  |
| [record_child](../harness/deploy/migration/legacy/isolated_turn.py#L146) | self, identity, event |  |
| [retire_questions](../harness/deploy/migration/legacy/isolated_turn.py#L157) | self, reason |  |
| [tool](../harness/deploy/migration/legacy/isolated_turn.py#L170) | self, item, actor |  |
| [event](../harness/deploy/migration/legacy/isolated_turn.py#L210) | self, item | Project one native event after independently admitting its actor. |
| [settling](../harness/deploy/migration/legacy/isolated_turn.py#L311) | self |  |
| [settled](../harness/deploy/migration/legacy/isolated_turn.py#L315) | self |  |
| [expire_questions](../harness/deploy/migration/legacy/isolated_turn.py#L324) | self |  |
| [active](../harness/deploy/migration/legacy/isolated_turn.py#L328) |  |  |
| [deliver](../harness/deploy/migration/legacy/isolated_turn.py#L330) | native_id, response |  |
| [stream](../harness/deploy/migration/legacy/isolated_turn.py#L336) | self |  |
| [close](../harness/deploy/migration/legacy/isolated_turn.py#L381) | self |  |
| [cleanup_tracked_lease](../harness/deploy/migration/legacy/isolated_turn.py#L395) | launcher, scope, run | Record the launcher's confirmed broker cleanup independently of readiness. |
| [run_isolated](../harness/deploy/migration/legacy/isolated_turn.py#L425) | agent, message, chat_id, dataset, attachments, clip_attachments, resolved_skills, model_context |  |
| [timing](../harness/deploy/migration/legacy/isolated_turn.py#L445) |  |  |

### harness/deploy/migration/legacy/managed_executor.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_identifier](../harness/deploy/migration/legacy/managed_executor.py#L30) | value |  |
| [__post_init__](../harness/deploy/migration/legacy/managed_executor.py#L41) | self |  |
| [key](../harness/deploy/migration/legacy/managed_executor.py#L46) | self |  |
| [__post_init__](../harness/deploy/migration/legacy/managed_executor.py#L56) | self |  |
| [container_name](../harness/deploy/migration/legacy/managed_executor.py#L73) | self |  |
| [volume_name](../harness/deploy/migration/legacy/managed_executor.py#L77) | self |  |
| [binding_hash](../harness/deploy/migration/legacy/managed_executor.py#L81) | self |  |
| [inspect](../harness/deploy/migration/legacy/managed_executor.py#L86) | self, spec |  |
| [start](../harness/deploy/migration/legacy/managed_executor.py#L87) | self, spec |  |
| [stop](../harness/deploy/migration/legacy/managed_executor.py#L88) | self, spec |  |
| [__init__](../harness/deploy/migration/legacy/managed_executor.py#L100) | self, state, backend, max_active, idle_grace_seconds, clock |  |
| [_locked](../harness/deploy/migration/legacy/managed_executor.py#L114) | self |  |
| [_save](../harness/deploy/migration/legacy/managed_executor.py#L132) | self, data |  |
| [_view](../harness/deploy/migration/legacy/managed_executor.py#L149) | entry |  |
| [_spec](../harness/deploy/migration/legacy/managed_executor.py#L155) | key, entry |  |
| [snapshot](../harness/deploy/migration/legacy/managed_executor.py#L158) | self, scope |  |
| [begin_work](../harness/deploy/migration/legacy/managed_executor.py#L162) | self, scope, binding, work_id, resume |  |
| [complete_work](../harness/deploy/migration/legacy/managed_executor.py#L210) | self, scope, work_id, all_children_terminal |  |
| [stop](../harness/deploy/migration/legacy/managed_executor.py#L227) | self, scope |  |
| [reap_idle](../harness/deploy/migration/legacy/managed_executor.py#L243) | self, scope, expected_generation |  |
| [__post_init__](../harness/deploy/migration/legacy/managed_executor.py#L270) | self |  |
| [__init__](../harness/deploy/migration/legacy/managed_executor.py#L289) | self, config, environment_key, provision_workspace, run |  |
| [_command](../harness/deploy/migration/legacy/managed_executor.py#L294) | self, args, key |  |
| [_json](../harness/deploy/migration/legacy/managed_executor.py#L307) | self, args, **kwargs |  |
| [_key](../harness/deploy/migration/legacy/managed_executor.py#L313) | self |  |
| [preflight](../harness/deploy/migration/legacy/managed_executor.py#L319) | self |  |
| [check_workspace](../harness/deploy/migration/legacy/managed_executor.py#L333) | self, spec |  |
| [_container](../harness/deploy/migration/legacy/managed_executor.py#L344) | self, spec |  |
| [inspect](../harness/deploy/migration/legacy/managed_executor.py#L362) | self, spec |  |
| [start](../harness/deploy/migration/legacy/managed_executor.py#L366) | self, spec |  |
| [stop](../harness/deploy/migration/legacy/managed_executor.py#L395) | self, spec |  |

### harness/deploy/migration/legacy/native_api_smoke.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [smoke](../harness/deploy/migration/legacy/native_api_smoke.py#L25) | state, executable |  |
| [main](../harness/deploy/migration/legacy/native_api_smoke.py#L102) |  |  |

### harness/deploy/migration/legacy/native_files.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [output_path](../harness/deploy/migration/legacy/native_files.py#L25) | value |  |
| [__init__](../harness/deploy/migration/legacy/native_files.py#L46) | self, files, company_id, owner_principal_id, root_chat_id, dataset, timeout_seconds |  |
| [_active](../harness/deploy/migration/legacy/native_files.py#L53) | self, session, actor_chat_id |  |
| [publish](../harness/deploy/migration/legacy/native_files.py#L68) | self, session, actor_chat_id, path, title |  |
| [_publish](../harness/deploy/migration/legacy/native_files.py#L76) | self, session, actor_chat_id, path, title | Return metadata for the standard artifact event. Parent dispatch only. |

### harness/deploy/migration/legacy/native_policy.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [cli_args](../harness/deploy/migration/legacy/native_policy.py#L39) | config |  |
| [thread_params](../harness/deploy/migration/legacy/native_policy.py#L45) | state, instructions, tools |  |
| [isolated_thread_params](../harness/deploy/migration/legacy/native_policy.py#L51) | instructions, tools, plugins, provider_approvals | For a verified gVisor broker process only; never use on the host profile. |
| [policy_digest](../harness/deploy/migration/legacy/native_policy.py#L75) | params | Persist permissions with tools so old permissive sessions are migrated. |
| [startup_policy](../harness/deploy/migration/legacy/native_policy.py#L80) | executable, state, env | Remove native file tools from the installed model catalogue before launch. |
| [provider_approval_policy](../harness/deploy/migration/legacy/native_policy.py#L148) |  | Native MCP approval UI only; outer worker permissions remain unchanged. |

### harness/deploy/migration/legacy/native_thread_tools.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [open_native_thread](../harness/deploy/migration/legacy/native_thread_tools.py#L11) | connection, existing_id, known_toolset, toolset_digest, start_params, migration_export | Open current tools, or copy bounded public context into a new native thread. |

### harness/deploy/native-executor/broker_service.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [configure_installer](../harness/deploy/native-executor/broker_service.py#L19) | broker, directory |  |
| [configure_custom](../harness/deploy/native-executor/broker_service.py#L42) | broker, directory |  |
| [main](../harness/deploy/native-executor/broker_service.py#L63) |  |  |

### harness/deploy/native-executor/relay.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [copy_stream](../harness/deploy/native-executor/relay.py#L9) | reader, writer |  |
| [connection](../harness/deploy/native-executor/relay.py#L17) | reader, writer, socket_path |  |
| [main](../harness/deploy/native-executor/relay.py#L49) |  |  |
| [connected](../harness/deploy/native-executor/relay.py#L52) | reader, writer, selected |  |

### harness/deploy/native-executor/test_relay.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [asyncSetUp](../harness/deploy/native-executor/test_relay.py#L11) | self |  |
| [asyncTearDown](../harness/deploy/native-executor/test_relay.py#L20) | self |  |
| [listen](../harness/deploy/native-executor/test_relay.py#L31) | self, handler |  |
| [captured](../harness/deploy/native-executor/test_relay.py#L32) | reader, writer |  |
| [forward](../harness/deploy/native-executor/test_relay.py#L40) | reader, writer |  |
| [client](../harness/deploy/native-executor/test_relay.py#L47) | self, port |  |
| [test_large_bidirectional_payload_and_half_close](../harness/deploy/native-executor/test_relay.py#L52) | self |  |
| [echo](../harness/deploy/native-executor/test_relay.py#L53) | reader, writer |  |
| [send](../harness/deploy/native-executor/test_relay.py#L60) |  |  |
| [test_excess_connections_are_closed_without_waiting_queue](../harness/deploy/native-executor/test_relay.py#L71) | self |  |
| [wait](../harness/deploy/native-executor/test_relay.py#L74) | reader, writer |  |
| [test_absent_socket_returns_eof_without_destination_fallback](../harness/deploy/native-executor/test_relay.py#L87) | self |  |
| [forward](../harness/deploy/native-executor/test_relay.py#L88) | reader, writer |  |

### harness/deploy/quality/prove_managed_protocol.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [private_json](../harness/deploy/quality/prove_managed_protocol.py#L53) | path, value |  |
| [configuration](../harness/deploy/quality/prove_managed_protocol.py#L64) | limit, nonce, spending_mode |  |
| [private_bytes](../harness/deploy/quality/prove_managed_protocol.py#L90) | path |  |
| [exclusive_bytes](../harness/deploy/quality/prove_managed_protocol.py#L100) | path, data |  |
| [approved_time](../harness/deploy/quality/prove_managed_protocol.py#L113) | value |  |
| [read_approval](../harness/deploy/quality/prove_managed_protocol.py#L123) | args |  |
| [rejected_evidence](../harness/deploy/quality/prove_managed_protocol.py#L143) | args, approval, usage | Only this definite admission rejection can reuse an unspent original hold. |
| [validate_hold](../harness/deploy/quality/prove_managed_protocol.py#L193) | usage, receipt, args, recover |  |
| [prepare_attempt](../harness/deploy/quality/prove_managed_protocol.py#L213) | args, pool, usage |  |
| [protocol_shape](../harness/deploy/quality/prove_managed_protocol.py#L274) | session | Small state projection: credentials, instructions and arguments stay private. |
| [known](../harness/deploy/quality/prove_managed_protocol.py#L278) | value, choices, fallback |  |
| [failure_details](../harness/deploy/quality/prove_managed_protocol.py#L296) | error, stage | Retain source literals and location, never dynamic upstream error contents. |
| [_check](../harness/deploy/quality/prove_managed_protocol.py#L315) | self, response |  |
| [artifacts](../harness/deploy/quality/prove_managed_protocol.py#L320) | self, session_id |  |
| [fetch](../harness/deploy/quality/prove_managed_protocol.py#L321) | **params |  |
| [artifact_bytes](../harness/deploy/quality/prove_managed_protocol.py#L325) | self, session_id, artifact_id |  |
| [wait_for_action](../harness/deploy/quality/prove_managed_protocol.py#L337) | client, session_id, name, deadline, prior_turns, diagnostics |  |
| [wait_for_terminal](../harness/deploy/quality/prove_managed_protocol.py#L358) | client, session_id, deadline |  |
| [cleanup](../harness/deploy/quality/prove_managed_protocol.py#L370) | client, session_id, key | Stop known work and request sandbox deletion within a fixed 90 seconds. |
| [run](../harness/deploy/quality/prove_managed_protocol.py#L399) | args |  |
| [checkpoint](../harness/deploy/quality/prove_managed_protocol.py#L429) | value, session |  |
| [persist_monitor](../harness/deploy/quality/prove_managed_protocol.py#L440) | value |  |
| [stop](../harness/deploy/quality/prove_managed_protocol.py#L444) | reason |  |
| [execute](../harness/deploy/quality/prove_managed_protocol.py#L485) | name, arguments |  |
| [main](../harness/deploy/quality/prove_managed_protocol.py#L608) |  |  |

### harness/layout.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [selected_vertical](../harness/layout.py#L29) | vertical_id | Validate the explicit selection or the primary and legacy environment settings. |
| [vertical_root](../harness/layout.py#L44) | vertical_id, root |  |
| [code_directories](../harness/layout.py#L52) | vertical_id, root | Import priority; root contains entry commands and optional deployment launchers. |
| [_root_module](../harness/layout.py#L62) | base, name |  |
| [modules](../harness/layout.py#L68) | vertical_id, root | Unique flat modules and package files in this selected source tree, without imports. |
| [source](../harness/layout.py#L90) | module_name, vertical_id, root | Resolve a flat or package-qualified source file without loading customer code. |
| [shared_asset](../harness/layout.py#L110) | relative_path | A repository-relative shared asset in either checkout or repo-shaped artifact. |
| [install](../harness/layout.py#L121) | vertical_id | Install one vertical's paths before application imports; repeat calls are idempotent. |

### harness/mechanics/access.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [page_request](../harness/mechanics/access.py#L16) | headers | Admit one browser page marker; the canonical header takes precedence. |
| [digest](../harness/mechanics/access.py#L24) | value |  |
| [__init__](../harness/mechanics/access.py#L28) | self, state |  |
| [connect](../harness/mechanics/access.py#L64) | self |  |
| [create_environment](../harness/mechanics/access.py#L69) | self, key, name |  |
| [issue](../harness/mechanics/access.py#L77) | self, environment, owner, now, principal_id, display_name |  |
| [login](../harness/mechanics/access.py#L101) | self, code, now, can_query |  |
| [session](../harness/mechanics/access.py#L122) | self, token, now |  |
| [switch](../harness/mechanics/access.py#L145) | self, token, environment |  |
| [principals](../harness/mechanics/access.py#L154) | self, token |  |
| [observe](../harness/mechanics/access.py#L166) | self, token, environment_id, principal_id |  |
| [clear_observer](../harness/mechanics/access.py#L177) | self, token |  |
| [logout](../harness/mechanics/access.py#L187) | self, token |  |

### harness/mechanics/agent_bridge.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [system_instructions](../harness/mechanics/agent_bridge.py#L24) |  | Compose product instructions from the current vertical for each managed turn. |
| [__getattr__](../harness/mechanics/agent_bridge.py#L33) | name |  |
| [participant_turn](../harness/mechanics/agent_bridge.py#L48) | agent, chat_id | The participant whose own message started this conversation's turn, else None. |
| [tool_specs](../harness/mechanics/agent_bridge.py#L69) | children, agent |  |
| [workspace_registry](../harness/mechanics/agent_bridge.py#L76) | agent |  |
| [__init__](../harness/mechanics/agent_bridge.py#L88) | self, state, retrieval, corpus, tool_only |  |
| [result_fields](../harness/mechanics/agent_bridge.py#L146) | self, name, content, success |  |
| [tool_result_fields](../harness/mechanics/agent_bridge.py#L151) | self, name, content, success |  |
| [_plans](../harness/mechanics/agent_bridge.py#L155) | self |  |
| [_business](../harness/mechanics/agent_bridge.py#L158) | self |  |
| [_skills](../harness/mechanics/agent_bridge.py#L164) | self |  |
| [_native_skills](../harness/mechanics/agent_bridge.py#L170) | self |  |
| [_connections](../harness/mechanics/agent_bridge.py#L184) | self |  |
| [_files](../harness/mechanics/agent_bridge.py#L195) | self |  |
| [_business_maps](../harness/mechanics/agent_bridge.py#L201) | self |  |
| [_custom_connectors](../harness/mechanics/agent_bridge.py#L207) | self |  |
| [_custom_execution](../harness/mechanics/agent_bridge.py#L213) | self |  |
| [_custom_setup](../harness/mechanics/agent_bridge.py#L219) | self |  |
| [_storage_runtime](../harness/mechanics/agent_bridge.py#L223) | self |  |
| [_publish_credential](../harness/mechanics/agent_bridge.py#L229) | self, chat_id, record |  |
| [refresh_credential_requests](../harness/mechanics/agent_bridge.py#L245) | self, chat_id |  |
| [_cancel_credential_waits](../harness/mechanics/agent_bridge.py#L252) | self, chat_id, reason |  |
| [resolve_credential_request](../harness/mechanics/agent_bridge.py#L261) | self, chat_id, request_id, owner, action, values, reason |  |
| [_wait_for_credentials](../harness/mechanics/agent_bridge.py#L282) | self, chat_id, connector_id, reason, scope |  |
| [resolve_skills](../harness/mechanics/agent_bridge.py#L310) | self, skill_ids, chat_id, owner_principal_id |  |
| [_skill_input](../harness/mechanics/agent_bridge.py#L338) | content, resolved |  |
| [_remember_usage](../harness/mechanics/agent_bridge.py#L343) | self, chat_id, event |  |
| [_is_child](../harness/mechanics/agent_bridge.py#L352) | self, chat_id |  |
| [_save_child](../harness/mechanics/agent_bridge.py#L355) | self, child |  |
| [_record_event](../harness/mechanics/agent_bridge.py#L363) | answer, event |  |
| [_complete_answer_timing](../harness/mechanics/agent_bridge.py#L456) | answer |  |
| [_remember](../harness/mechanics/agent_bridge.py#L464) | self, chat_id, thread_id |  |
| [_remember_toolset](../harness/mechanics/agent_bridge.py#L471) | self, thread_id, digest, opened |  |
| [status](../harness/mechanics/agent_bridge.py#L479) | self |  |
| [_clip_attachments](../harness/mechanics/agent_bridge.py#L484) | self, ids, dataset |  |
| [_input](../harness/mechanics/agent_bridge.py#L489) | self, message, attachments, clip_attachments, dataset |  |
| [capability_snapshot](../harness/mechanics/agent_bridge.py#L503) | self, chat_id, scope |  |
| [agent_setup_context](../harness/mechanics/agent_bridge.py#L513) | self, chat_id |  |
| [current_agent_setup](../harness/mechanics/agent_bridge.py#L531) | self, chat_id |  |
| [_approval_history_scope](../harness/mechanics/agent_bridge.py#L544) | self, root_chat_id, owner |  |
| [refresh_native_approvals](../harness/mechanics/agent_bridge.py#L550) | self, chat_id |  |
| [revoke_provider_approvals](../harness/mechanics/agent_bridge.py#L568) | self, provider, owner |  |
| [resolve_native_approval](../harness/mechanics/agent_bridge.py#L587) | self, chat_id, request_id, owner, action |  |
| [refresh_native_questions](../harness/mechanics/agent_bridge.py#L612) | self, chat_id |  |
| [_publish_question](../harness/mechanics/agent_bridge.py#L628) | self, chat_id, record |  |
| [_deliver_clarification](../harness/mechanics/agent_bridge.py#L640) | self, chat_id, request_id, waiter, run, response |  |
| [_wait_for_clarification](../harness/mechanics/agent_bridge.py#L646) | self, chat_id, arguments, scope |  |
| [deliver](../harness/mechanics/agent_bridge.py#L659) | native_id, response |  |
| [resolve_native_question](../harness/mechanics/agent_bridge.py#L684) | self, chat_id, request_id, owner, action, answers |  |
| [deliver_host](../harness/mechanics/agent_bridge.py#L695) | native_id, response |  |
| [deliver](../harness/mechanics/agent_bridge.py#L710) | native_id, payload |  |
| [active](../harness/mechanics/agent_bridge.py#L711) |  |  |
| [control](../harness/mechanics/agent_bridge.py#L721) | self, chat_id, operation, message, attachments, clip_attachments, skill_ids, sender |  |
| [turn](../harness/mechanics/agent_bridge.py#L752) | self, message, chat_id, dataset, attachments, clip_attachments, skill_ids, model_context, sender |  |
| [_recorded_turn](../harness/mechanics/agent_bridge.py#L762) | self, message, chat_id, dataset, attachments, clip_attachments, skill_ids, model_context, sender |  |
| [_turn](../harness/mechanics/agent_bridge.py#L832) | self, message, chat_id, dataset, attachments, clip_attachments, resolved_skills, model_context |  |
| [_public_clip](../harness/mechanics/agent_bridge.py#L857) | self, record |  |
| [_inspection_metadata](../harness/mechanics/agent_bridge.py#L860) | self, record, frames, include_observations |  |
| [_guest](../harness/mechanics/agent_bridge.py#L863) | self, child, sender | This sender as a participant other than the conversation's creator, else None. |
| [_authority_principal](../harness/mechanics/agent_bridge.py#L870) | self, chat_id | Separate the live human authority from the conversation's data owner. |
| [_tool](../harness/mechanics/agent_bridge.py#L883) | self, name, args, scope, chat_id |  |
| [_scoped_tool](../harness/mechanics/agent_bridge.py#L891) | self, name, args, scope, chat_id |  |
| [_common_tool](../harness/mechanics/agent_bridge.py#L916) | self, name, args, scope, chat_id |  |
| [cover_current](../harness/mechanics/agent_bridge.py#L1048) |  |  |
| [current](../harness/mechanics/agent_bridge.py#L1067) |  |  |

### harness/mechanics/agent_catalogue.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [available](../harness/mechanics/agent_catalogue.py#L24) |  |  |
| [retired](../harness/mechanics/agent_catalogue.py#L28) |  |  |
| [template](../harness/mechanics/agent_catalogue.py#L32) | template_id | The template with this id, or None. |
| [draft](../harness/mechanics/agent_catalogue.py#L37) | template_id, dataset, profiles | The definition a draft agent takes from one available template, for one business collection. |
| [catalogue](../harness/mechanics/agent_catalogue.py#L63) |  |  |

### harness/mechanics/agent_invocation.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [invoke](../harness/mechanics/agent_invocation.py#L12) | agent, chat_id, arguments, now |  |

### harness/mechanics/agent_kind_policy.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [messaging_channels](../harness/mechanics/agent_kind_policy.py#L11) | agent |  |
| [declared_class_authority](../harness/mechanics/agent_kind_policy.py#L18) | store, definition |  |
| [has_participant_reach_context](../harness/mechanics/agent_kind_policy.py#L26) | agent, chat_id | An ancestor's declared restrictions survive both descendant mechanisms. |
| [participant_recipient](../harness/mechanics/agent_kind_policy.py#L58) | agent, chat_id, sender | Resolve the one member a participant-reach context may message: the turn's own participant. |

### harness/mechanics/agent_wakes.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/mechanics/agent_wakes.py#L16) | self, store |  |
| [_input_allowed](../harness/mechanics/agent_wakes.py#L25) | self, record, definition |  |
| [enqueue](../harness/mechanics/agent_wakes.py#L28) | self, agent_id, owner, expected_revision, provider, connection_id, event_id, kind, sender_id, channel_id, text, now, requires_input, source_scope, chain, payload | Accept an already-authenticated, owner-bound event, never new authority. |
| [_get](../harness/mechanics/agent_wakes.py#L99) | db, key |  |
| [_write](../harness/mechanics/agent_wakes.py#L105) | db, record |  |
| [get](../harness/mechanics/agent_wakes.py#L109) | self, wake_id, owner |  |
| [pending](../harness/mechanics/agent_wakes.py#L116) | self, agent_id, owner, now |  |
| [_eligible](../harness/mechanics/agent_wakes.py#L134) | self, record, definition, now |  |
| [for_claim](../harness/mechanics/agent_wakes.py#L142) | self, db, wake_id, definition, now |  |
| [claimed](../harness/mechanics/agent_wakes.py#L152) | self, db, record, run_id |  |
| [_retire](../harness/mechanics/agent_wakes.py#L156) | self, db, record, status, reason, now |  |
| [cancel_pending](../harness/mechanics/agent_wakes.py#L160) | self, db, agent_id, reason, now |  |
| [get_for_run](../harness/mechanics/agent_wakes.py#L167) | self, db, run_id |  |
| [finish](../harness/mechanics/agent_wakes.py#L174) | self, db, run_id, status, now |  |
| [enqueue_chat](../harness/mechanics/agent_wakes.py#L180) | self, chat_id, collection, owner, actor, provider, connection_id, event_id, text, sender, chain, payload, expires_at, now, source_id | Host-bound ordinary messages enter the same chain without a saved-agent definition. |
| [enqueue_job](../harness/mechanics/agent_wakes.py#L219) | self, producer, producer_id, owner, actor, collection, event_id, payload, source_scope, chain, destination, chat_id, kind, expires_at, now | Persist host-authorized work whose calculation may be the complete job. |
| [signal_current](../harness/mechanics/agent_wakes.py#L269) | self, key |  |
| [chat_in_flight](../harness/mechanics/agent_wakes.py#L274) | db | A lost admitted turn holds the workspace until provider reconciliation. |
| [claim_chat](../harness/mechanics/agent_wakes.py#L281) | self, wake_id, owner, now |  |
| [finish_chat](../harness/mechanics/agent_wakes.py#L298) | self, wake_id, claim_id, owner, status, admitted |  |

### harness/mechanics/attachments.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/mechanics/attachments.py#L8) | self, state |  |
| [save_attachment](../harness/mechanics/attachments.py#L11) | self, data, name |  |

### harness/mechanics/background_agents.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/mechanics/background_agents.py#L24) | self, state, input_provider, wake_authorizer, agent_classes, authority |  |
| [definition_model](../harness/mechanics/background_agents.py#L64) | self |  |
| [install_inputs](../harness/mechanics/background_agents.py#L67) | self, provider, wake_authorizer |  |
| [install_classes](../harness/mechanics/background_agents.py#L76) | self, declarations |  |
| [class_allowed](../harness/mechanics/background_agents.py#L91) | self, definition |  |
| [validate_class](../harness/mechanics/background_agents.py#L94) | self, definition |  |
| [install_authority](../harness/mechanics/background_agents.py#L98) | self, authority |  |
| [standing](../harness/mechanics/background_agents.py#L104) | record |  |
| [grant_current](../harness/mechanics/background_agents.py#L107) | self, record, now |  |
| [run_current](../harness/mechanics/background_agents.py#L126) | self, run, now |  |
| [seal_inputs](../harness/mechanics/background_agents.py#L134) | self |  |
| [connect](../harness/mechanics/background_agents.py#L137) | self |  |
| [_read](../harness/mechanics/background_agents.py#L142) | self, db, table, key |  |
| [_save](../harness/mechanics/background_agents.py#L151) | db, table, data |  |
| [_audit](../harness/mechanics/background_agents.py#L155) | db, agent_id, event, body, run_id |  |
| [create](../harness/mechanics/background_agents.py#L159) | self, definition, datasets, owner_principal_id, input_context, conversation_chat_id |  |
| [get](../harness/mechanics/background_agents.py#L198) | self, key |  |
| [list](../harness/mechanics/background_agents.py#L210) | self, owner_principal_id |  |
| [run_report](../harness/mechanics/background_agents.py#L216) | self, agent_id, run_id |  |
| [mark_conversation_run](../harness/mechanics/background_agents.py#L223) | self, run_id, message_start | Pin the run's report boundary before appending to its shared chat. |
| [pin_skills](../harness/mechanics/background_agents.py#L236) | self, run_id, snapshots | Pin the host's resolved skill revisions once, before native execution. |
| [_snapshot_report](../harness/mechanics/background_agents.py#L265) | run, messages |  |
| [freeze_report](../harness/mechanics/background_agents.py#L270) | self, run_id, messages | Migrate earlier terminal reports once; later chat changes cannot alter them. |
| [update](../harness/mechanics/background_agents.py#L280) | self, key, definition, datasets, expected_revision, input_context |  |
| [activate](../harness/mechanics/background_agents.py#L310) | self, key, expires_at, once, now, expected_revision, standing, actor_principal_id |  |
| [active_since](../harness/mechanics/background_agents.py#L345) | self, key | When this agent's latest activation began, from its audit trail; None before the first one. |
| [pause](../harness/mechanics/background_agents.py#L356) | self, key |  |
| [recover](../harness/mechanics/background_agents.py#L368) | self, now | Keep standing grants; reconcile admitted work before another wake. |
| [input_optional_wake](../harness/mechanics/background_agents.py#L420) | self, definition, wake, admit | An adapter may admit its own signal without a fresh input batch. |
| [claim](../harness/mechanics/background_agents.py#L435) | self, key, sources, now, source_records, screening, wake_id |  |
| [defer_unstarted_run](../harness/mechanics/background_agents.py#L508) | self, run_id | A manual turn winning the dispatch race leaves the wake and allowance pending. |
| [schedule_signal](../harness/mechanics/background_agents.py#L533) | self, definition, now |  |
| [advance_filtered_schedule](../harness/mechanics/background_agents.py#L543) | self, signal |  |
| [hold](../harness/mechanics/background_agents.py#L552) | self, run_id, error |  |
| [resume_recovery](../harness/mechanics/background_agents.py#L560) | self, run_id |  |
| [execution_current](../harness/mechanics/background_agents.py#L572) | self, run_id |  |
| [admit_resource](../harness/mechanics/background_agents.py#L577) | self, run_id, maximum_usd |  |
| [finish](../harness/mechanics/background_agents.py#L600) | self, run_id, status, error, now, report_messages |  |
| [ensure_agent_conversation](../harness/mechanics/background_agents.py#L631) | store, agent, definition, briefing | Materialize only the host-bound chat; preserve its messages and native ID. |
| [__init__](../harness/mechanics/background_agents.py#L662) | self, store, agent, slots |  |
| [ensure_conversation](../harness/mechanics/background_agents.py#L682) | self, definition, briefing |  |
| [recover_pending](../harness/mechanics/background_agents.py#L685) | self |  |
| [tick](../harness/mechanics/background_agents.py#L722) | self |  |
| [_finished](../harness/mechanics/background_agents.py#L778) | self, run_id, task |  |
| [_execute](../harness/mechanics/background_agents.py#L786) | self, run, input_snapshot |  |
| [pause](../harness/mechanics/background_agents.py#L870) | self, key |  |
| [close](../harness/mechanics/background_agents.py#L880) | self |  |

### harness/mechanics/builtin_capabilities.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [default_factory](../harness/mechanics/builtin_capabilities.py#L15) | name |  |
| [__init__](../harness/mechanics/builtin_capabilities.py#L24) | self, state, environment_id, selected, factories, spending, host_ready |  |
| [enabled](../harness/mechanics/builtin_capabilities.py#L34) | self, name |  |
| [provider](../harness/mechanics/builtin_capabilities.py#L39) | self, name |  |
| [pollers](../harness/mechanics/builtin_capabilities.py#L51) | self | Only explicitly installed providers contribute host polling callbacks. |
| [status](../harness/mechanics/builtin_capabilities.py#L61) | self |  |

### harness/mechanics/business_context.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [public_url](../harness/mechanics/business_context.py#L32) | value | Accept public reference URLs, never credential or private service URLs. |
| [_public_text](../harness/mechanics/business_context.py#L65) | value |  |
| [reference_data](../harness/mechanics/business_context.py#L85) | self |  |
| [_validate](../harness/mechanics/business_context.py#L96) | model, body |  |
| [_now](../harness/mechanics/business_context.py#L104) |  |  |
| [__init__](../harness/mechanics/business_context.py#L109) | self, state, collections |  |
| [connect](../harness/mechanics/business_context.py#L123) | self |  |
| [_collection_exists](../harness/mechanics/business_context.py#L128) | self, collection |  |
| [_scope](../harness/mechanics/business_context.py#L131) | self, db, collection |  |
| [_initial](../harness/mechanics/business_context.py#L138) | self, collection |  |
| [_current](../harness/mechanics/business_context.py#L147) | self, db, collection |  |
| [_present](../harness/mechanics/business_context.py#L151) | self, record |  |
| [get](../harness/mechanics/business_context.py#L156) | self, collection |  |
| [history](../harness/mechanics/business_context.py#L161) | self, collection, limit |  |
| [_mutate](../harness/mechanics/business_context.py#L169) | self, collection, expected_revision, kind, origin, change |  |
| [update](../harness/mechanics/business_context.py#L186) | self, collection, expected_revision, profile, origin |  |
| [change](../harness/mechanics/business_context.py#L192) | current, revision, timestamp |  |

### harness/mechanics/business_maps.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [format_guide](../harness/mechanics/business_maps.py#L103) | business |  |
| [_fail](../harness/mechanics/business_maps.py#L113) |  |  |
| [_text](../harness/mechanics/business_maps.py#L117) | value, limit, empty |  |
| [_number](../harness/mechanics/business_maps.py#L124) | value, minimum, maximum |  |
| [_timestamp](../harness/mechanics/business_maps.py#L130) | value |  |
| [_url](../harness/mechanics/business_maps.py#L141) | value |  |
| [_pairs](../harness/mechanics/business_maps.py#L162) | items |  |
| [decode](../harness/mechanics/business_maps.py#L171) | raw |  |
| [validate](../harness/mechanics/business_maps.py#L181) | raw |  |
| [coordinate](../harness/mechanics/business_maps.py#L202) | value |  |
| [line](../harness/mechanics/business_maps.py#L210) | values, ring |  |
| [polygon](../harness/mechanics/business_maps.py#L217) | values |  |
| [geometry](../harness/mechanics/business_maps.py#L222) | value, allowed, empty |  |
| [current_member](../harness/mechanics/business_maps.py#L353) | access_path, environment, owner | Cheap host-selected membership fence; logout leaves durable ownership intact. |
| [__init__](../harness/mechanics/business_maps.py#L372) | self, state |  |
| [metadata](../harness/mechanics/business_maps.py#L388) | row, stale |  |
| [publish](../harness/mechanics/business_maps.py#L394) | self, files, business, file_id, expected_profile_revision, owner, chat_id, collection, current, created |  |
| [discard](../harness/mechanics/business_maps.py#L441) | self, ids, owner, chat_id, collection | Remove only this interrupted publication's newly inserted rows. |
| [get](../harness/mechanics/business_maps.py#L447) | self, business, owner, collection, map_id |  |

### harness/mechanics/business_scope.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [need](../harness/mechanics/business_scope.py#L13) | value, code |  |
| [identifier](../harness/mechanics/business_scope.py#L16) | value |  |
| [label](../harness/mechanics/business_scope.py#L20) | value, maximum, empty |  |
| [ids](../harness/mechanics/business_scope.py#L25) | value, maximum |  |
| [__post_init__](../harness/mechanics/business_scope.py#L35) | self |  |
| [__init__](../harness/mechanics/business_scope.py#L40) | self, state, company_id, member, members |  |
| [authority](../harness/mechanics/business_scope.py#L46) | self, actor, write |  |

### harness/mechanics/capability_providers.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [email_address](../harness/mechanics/capability_providers.py#L40) | value |  |
| [body_bytes](../harness/mechanics/capability_providers.py#L47) | raw |  |
| [json_body](../harness/mechanics/capability_providers.py#L53) | raw |  |
| [signature_header](../harness/mechanics/capability_providers.py#L63) | headers, name |  |
| [empty_events](../harness/mechanics/capability_providers.py#L70) |  |  |
| [message](../harness/mechanics/capability_providers.py#L74) | identifier, address, text, sent_at, context, payload |  |
| [__post_init__](../harness/mechanics/capability_providers.py#L97) | self |  |
| [__init__](../harness/mechanics/capability_providers.py#L122) | self, config, credentials, transport |  |
| [credentials](../harness/mechanics/capability_providers.py#L129) | self |  |
| [readiness](../harness/mechanics/capability_providers.py#L140) | self |  |
| [otp_hash](../harness/mechanics/capability_providers.py#L152) | self, challenge_id, code |  |
| [text](../harness/mechanics/capability_providers.py#L157) | self, kind, text, code |  |
| [preview](../harness/mechanics/capability_providers.py#L169) | self, kind, text, alert |  |
| [send](../harness/mechanics/capability_providers.py#L172) | self, prepared, current |  |
| [before](../harness/mechanics/capability_providers.py#L177) | request |  |
| [endpoint](../harness/mechanics/capability_providers.py#L227) | self |  |
| [address](../harness/mechanics/capability_providers.py#L230) | self, value |  |
| [prepare](../harness/mechanics/capability_providers.py#L233) | self, kind, address, text, code, alert, reference |  |
| [prepare_reply](../harness/mechanics/capability_providers.py#L237) | self, prepared, provider_message_id, message_id |  |
| [request](../harness/mechanics/capability_providers.py#L243) | self, prepared |  |
| [identifier](../harness/mechanics/capability_providers.py#L246) | self, value |  |
| [verify](../harness/mechanics/capability_providers.py#L252) | self, raw_body, headers |  |
| [events](../harness/mechanics/capability_providers.py#L261) | self, raw_body |  |
| [email_text](../harness/mechanics/capability_providers.py#L312) | body | Bounded ordinary text from the provider's HTML body; scripts/styles stay out. |
| [__init__](../harness/mechanics/capability_providers.py#L317) | self |  |
| [handle_starttag](../harness/mechanics/capability_providers.py#L320) | self, tag, attrs |  |
| [handle_endtag](../harness/mechanics/capability_providers.py#L325) | self, tag |  |
| [handle_data](../harness/mechanics/capability_providers.py#L330) | self, value |  |
| [endpoint](../harness/mechanics/capability_providers.py#L345) | self |  |
| [prepare](../harness/mechanics/capability_providers.py#L348) | self, kind, address, text, code, alert, reference |  |
| [units](../harness/mechanics/capability_providers.py#L360) | self, prepared |  |
| [request](../harness/mechanics/capability_providers.py#L363) | self, prepared |  |
| [identifier](../harness/mechanics/capability_providers.py#L366) | self, value |  |
| [form](../harness/mechanics/capability_providers.py#L372) | self, raw_body |  |
| [verify](../harness/mechanics/capability_providers.py#L381) | self, raw_body, headers |  |
| [events](../harness/mechanics/capability_providers.py#L388) | self, raw_body |  |
| [address](../harness/mechanics/capability_providers.py#L412) | self, value |  |
| [prepare](../harness/mechanics/capability_providers.py#L417) | self, kind, address, text, code, alert, reference |  |
| [request](../harness/mechanics/capability_providers.py#L426) | self, prepared |  |
| [identifier](../harness/mechanics/capability_providers.py#L429) | self, value |  |
| [verify](../harness/mechanics/capability_providers.py#L434) | self, raw_body, headers |  |
| [events](../harness/mechanics/capability_providers.py#L439) | self, raw_body |  |
| [provider_for](../harness/mechanics/capability_providers.py#L464) | name, state, environment_id | Read one selected capability; absent host configuration installs nothing. |
| [credentials](../harness/mechanics/capability_providers.py#L507) |  |  |

### harness/mechanics/capability_spend.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/mechanics/capability_spend.py#L30) | self |  |
| [__init__](../harness/mechanics/capability_spend.py#L35) | self, state, environment_id, company_id, reader |  |
| [_read](../harness/mechanics/capability_spend.py#L39) | self |  |
| [grant](../harness/mechanics/capability_spend.py#L52) | self, provider, now |  |
| [ready](../harness/mechanics/capability_spend.py#L77) | self, provider, now |  |
| [reserve](../harness/mechanics/capability_spend.py#L84) | self, db, row, provider, prepared, now |  |
| [release](../harness/mechanics/capability_spend.py#L117) | db, outbox |  |

### harness/mechanics/catalogue_providers.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_fail](../harness/mechanics/catalogue_providers.py#L25) |  |  |
| [_digest](../harness/mechanics/catalogue_providers.py#L28) | value |  |
| [_url](../harness/mechanics/catalogue_providers.py#L31) | value, origin |  |
| [_entries](../harness/mechanics/catalogue_providers.py#L46) |  |  |
| [remote_entries](../harness/mechanics/catalogue_providers.py#L64) |  |  |
| [pending_policies](../harness/mechanics/catalogue_providers.py#L67) |  |  |
| [__post_init__](../harness/mechanics/catalogue_providers.py#L92) | self |  |
| [from_dict](../harness/mechanics/catalogue_providers.py#L122) | cls, value |  |
| [fingerprint](../harness/mechanics/catalogue_providers.py#L133) | self |  |
| [policy](../harness/mechanics/catalogue_providers.py#L137) | self |  |
| [__post_init__](../harness/mechanics/catalogue_providers.py#L158) | self |  |
| [load](../harness/mechanics/catalogue_providers.py#L168) | cls, path, company_scope, public_origin |  |

### harness/mechanics/chat_files.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_spreadsheet_cell](../harness/mechanics/chat_files.py#L40) | value |  |
| [_spreadsheet_download](../harness/mechanics/chat_files.py#L54) | content, suffix, legacy |  |
| [__init__](../harness/mechanics/chat_files.py#L79) | self, state, exports |  |
| [connect](../harness/mechanics/chat_files.py#L116) | self |  |
| [_scope](../harness/mechanics/chat_files.py#L120) | owner_principal_id, chat_id, dataset |  |
| [create](../harness/mechanics/chat_files.py#L127) | self, document, owner_principal_id, chat_id, dataset |  |
| [native_name](../harness/mechanics/chat_files.py#L184) | name, title |  |
| [_native_preview](../harness/mechanics/chat_files.py#L196) | name, prefix, size |  |
| [import_native](../harness/mechanics/chat_files.py#L226) | self, stream, name, title, size_bytes, sha256, publication_key, provenance, owner_principal_id, chat_id, dataset | Host-only exact-byte import from a verified private broker buffer. |
| [import_provider_resource](../harness/mechanics/chat_files.py#L277) | self, resource, provider, provider_name, publication_key, provenance, owner_principal_id, chat_id, dataset, guard, created | Host-only provider metadata and returned text; this performs no URL fetch. |
| [discard_provider_publications](../harness/mechanics/chat_files.py#L324) | self, created, owner_principal_id, chat_id, dataset | Remove only this admission's new rows when its post-commit fence closes. |
| [link_export](../harness/mechanics/chat_files.py#L338) | self, export_id, owner_principal_id, chat_id, dataset |  |
| [_export](../harness/mechanics/chat_files.py#L353) | record, chat_id |  |
| [list](../harness/mechanics/chat_files.py#L363) | self, owner_principal_id, chat_id, dataset |  |
| [_preferences](../harness/mechanics/chat_files.py#L382) | record, preferences |  |
| [get](../harness/mechanics/chat_files.py#L390) | self, file_id, owner_principal_id, chat_id, dataset |  |
| [rename](../harness/mechanics/chat_files.py#L412) | self, file_id, title, owner_principal_id |  |
| [opened](../harness/mechanics/chat_files.py#L423) | self, file_id, owner_principal_id |  |
| [content](../harness/mechanics/chat_files.py#L431) | self, file_id, owner_principal_id, chat_id, dataset |  |
| [download](../harness/mechanics/chat_files.py#L439) | self, file_id, owner_principal_id, chat_id, dataset |  |

### harness/mechanics/chat_permissions.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [workspace_writable](../harness/mechanics/chat_permissions.py#L17) | session |  |
| [__init__](../harness/mechanics/chat_permissions.py#L23) | self, state, organization |  |
| [connect](../harness/mechanics/chat_permissions.py#L48) | self |  |
| [principal](../harness/mechanics/chat_permissions.py#L53) | session |  |
| [_owned](../harness/mechanics/chat_permissions.py#L63) | self, record, session |  |
| [participant](../harness/mechanics/chat_permissions.py#L70) | self, record, session | The selected person reads this Tracking Agent's own conversation as one of its participants. |
| [can_read](../harness/mechanics/chat_permissions.py#L88) | self, record, session |  |
| [can_write](../harness/mechanics/chat_permissions.py#L91) | self, record, session | Owner authority: the definition, its controls and every host interaction of the conversation. |
| [can_converse](../harness/mechanics/chat_permissions.py#L95) | self, record, session | Write a message in the conversation: its owner, or a participant of a Tracking Agent's own chat. |
| [_attachment_digest](../harness/mechanics/chat_permissions.py#L99) | self, attachment_id |  |
| [_register_attachment](../harness/mechanics/chat_permissions.py#L108) | self, db, attachment_id, principal, origin, authorization_note |  |
| [register_attachment](../harness/mechanics/chat_permissions.py#L118) | self, attachment_id, session |  |
| [can_read_attachment](../harness/mechanics/chat_permissions.py#L125) | self, attachment_id, session |  |
| [validate_attachments](../harness/mechanics/chat_permissions.py#L132) | self, attachment_ids, session, write |  |
| [_metadata](../harness/mechanics/chat_permissions.py#L140) | self, db, record, session |  |
| [get](../harness/mechanics/chat_permissions.py#L150) | self, record, session |  |
| [visible_records](../harness/mechanics/chat_permissions.py#L154) | self, records, session, include_archived |  |
| [update](../harness/mechanics/chat_permissions.py#L160) | self, record, session, pinned, archived, expected_revision |  |
| [assign_founder_history](../harness/mechanics/chat_permissions.py#L175) | self, records, owner_session, chat_ids, authorization_note | Host-only, explicitly authorized migration of enumerated Demo history. |
| [assign_founder_attachments](../harness/mechanics/chat_permissions.py#L217) | self, records, owner_session, chat_ids, authorization_note | Host-only migration of images actually referenced by assigned Demo chats. |

### harness/mechanics/chat_stream.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/mechanics/chat_stream.py#L7) | self, events, capacity |  |
| [_publish](../harness/mechanics/chat_stream.py#L13) | self, event |  |
| [_run](../harness/mechanics/chat_stream.py#L21) | self, events |  |
| [subscribe](../harness/mechanics/chat_stream.py#L33) | self |  |

### harness/mechanics/company_usage.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_read_private](../harness/mechanics/company_usage.py#L25) | path |  |
| [_money](../harness/mechanics/company_usage.py#L31) | value |  |
| [_usd](../harness/mechanics/company_usage.py#L43) | value |  |
| [_provider_money](../harness/mechanics/company_usage.py#L47) | value | Provider reports can exceed six decimals; reserve the next micro-dollar. |
| [_digest](../harness/mechanics/company_usage.py#L57) | value |  |
| [_openai_pricing](../harness/mechanics/company_usage.py#L61) | value |  |
| [__init__](../harness/mechanics/company_usage.py#L96) | self, state, provider |  |
| [openai_pool](../harness/mechanics/company_usage.py#L149) | cls, parent_state | Host-selected API pool; its funds never share the Modal trial ledger. |
| [native_agent_pool](../harness/mechanics/company_usage.py#L154) | cls, parent_state | Separate host-commissioned native chat allowance; image workers never use it. |
| [agent_pool_path](../harness/mechanics/company_usage.py#L159) | parent_state |  |
| [agent_pool](../harness/mechanics/company_usage.py#L166) | cls, parent_state |  |
| [_bound_openai_pool](../harness/mechanics/company_usage.py#L170) | cls, parent_state, pool_name |  |
| [_openai_binding](../harness/mechanics/company_usage.py#L192) | db |  |
| [connect](../harness/mechanics/company_usage.py#L198) | self |  |
| [_now](../harness/mechanics/company_usage.py#L203) |  |  |
| [_append](../harness/mechanics/company_usage.py#L206) | self, db, key, kind, amount, reservation_id, **data |  |
| [_state](../harness/mechanics/company_usage.py#L210) | self, db |  |
| [_operator_authorization](../harness/mechanics/company_usage.py#L230) | self, db, events | Return the current immutable total allowance, including legacy funding. |
| [renew_operator_budget](../harness/mechanics/company_usage.py#L237) | self, path, lifecycle, environment_id, expected_prior_record_sha256 | Host-only replacement of an expired, fully reconciled total allowance. |
| [_summary](../harness/mechanics/company_usage.py#L303) | self, db |  |
| [summary](../harness/mechanics/company_usage.py#L338) | self |  |
| [reconcile_local](../harness/mechanics/company_usage.py#L343) | self | Mirror already-recorded provider evidence without querying a provider. |
| [set_monthly_limit](../harness/mechanics/company_usage.py#L351) | self, expected_revision, monthly_limit_usd, retail_multiplier |  |
| [_fund](../harness/mechanics/company_usage.py#L368) | self, db, record_id, amount, kind, digest, **provenance |  |
| [import_operator_budget](../harness/mechanics/company_usage.py#L381) | self, path, lifecycle, environment_id | Host-only internal demo allocation; neither deposit nor provider credit. |
| [import_funding_record](../harness/mechanics/company_usage.py#L423) | self, path | Host-only import of an actual owner-verified settled deposit receipt. |
| [_provider](../harness/mechanics/company_usage.py#L444) | self, approval_path |  |
| [import_demo_allowance](../harness/mechanics/company_usage.py#L449) | self, approval_path, query_ledger_path | Host-only Demo setup; mirrors existing owner-authorized free credit. |
| [reserve](../harness/mechanics/company_usage.py#L483) | self, maximum_usd, idempotency_key |  |
| [_reserve_in_transaction](../harness/mechanics/company_usage.py#L492) | self, db, provider_maximum, idempotency_key | Share the same atomic funded balance with provider-specific admissions. |
| [_public_reservation](../harness/mechanics/company_usage.py#L512) | record |  |
| [_reservation](../harness/mechanics/company_usage.py#L515) | self, db, rid |  |
| [mark_started](../harness/mechanics/company_usage.py#L519) | self, reservation_id |  |
| [bind_openai_request](../harness/mechanics/company_usage.py#L539) | self, reservation_id, request_id, model, pricing | Pin the host's request identity and verified rate snapshot before sending. |
| [settle_openai](../harness/mechanics/company_usage.py#L564) | self, reservation_id, receipt_path | Settle measured completed Responses usage from a private gateway receipt. |
| [release_before_remote](../harness/mechanics/company_usage.py#L649) | self, reservation_id |  |
| [_provider_key](../harness/mechanics/company_usage.py#L663) | path, rid |  |
| [link_provider](../harness/mechanics/company_usage.py#L666) | self, reservation_id, approval_path, provider_reservation_id |  |
| [_apply_provider](../harness/mechanics/company_usage.py#L684) | self, db, rid, entry |  |
| [sync_query_reservation](../harness/mechanics/company_usage.py#L724) | self, reservation_id, query_approval_path, provider_reservation_id |  |
| [settle](../harness/mechanics/company_usage.py#L731) | self, reservation_id, actual_usd, source |  |

### harness/mechanics/conversation_tools.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [conversation_specs](../harness/mechanics/conversation_tools.py#L5) | children, definition_model |  |
| [__init__](../harness/mechanics/conversation_tools.py#L144) | self, definition_model |  |
| [specs](../harness/mechanics/conversation_tools.py#L149) | self, write |  |
| [aread](../harness/mechanics/conversation_tools.py#L152) | self, context, name, arguments |  |
| [acall](../harness/mechanics/conversation_tools.py#L160) | self, context, name, arguments |  |
| [local_call](../harness/mechanics/conversation_tools.py#L164) | self, context, name, arguments |  |

### harness/mechanics/custom_connectors.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [now](../harness/mechanics/custom_connectors.py#L31) |  |  |
| [text](../harness/mechanics/custom_connectors.py#L35) | value, limit, label, optional |  |
| [contains_secret](../harness/mechanics/custom_connectors.py#L42) | value, secret |  |
| [__init__](../harness/mechanics/custom_connectors.py#L50) | self, state |  |
| [register_extension](../harness/mechanics/custom_connectors.py#L84) | self, name, initialize, public_values |  |
| [db](../harness/mechanics/custom_connectors.py#L91) | self |  |
| [identity](../harness/mechanics/custom_connectors.py#L97) | value |  |
| [_row](../harness/mechanics/custom_connectors.py#L102) | self, db, key, owner |  |
| [_public](../harness/mechanics/custom_connectors.py#L108) | self, db, record |  |
| [create](../harness/mechanics/custom_connectors.py#L116) | self, name, description, kind, collection, owner, chat_id |  |
| [get](../harness/mechanics/custom_connectors.py#L134) | self, key, owner |  |
| [list](../harness/mechanics/custom_connectors.py#L137) | self, owner, collection |  |
| [_cipher](../harness/mechanics/custom_connectors.py#L144) | self, db |  |
| [_validate_package](../harness/mechanics/custom_connectors.py#L166) | package |  |
| [save_package](../harness/mechanics/custom_connectors.py#L205) | self, key, package, expected_revision, owner |  |
| [source](../harness/mechanics/custom_connectors.py#L237) | self, key, owner |  |
| [_set_secret](../harness/mechanics/custom_connectors.py#L242) | self, db, key, name, value, record, package |  |
| [set_secret](../harness/mechanics/custom_connectors.py#L259) | self, key, name, value, owner |  |
| [_request_row](../harness/mechanics/custom_connectors.py#L265) | db, request_id, owner, chat_id |  |
| [_save_request](../harness/mechanics/custom_connectors.py#L272) | db, record |  |
| [_cancel_requests](../harness/mechanics/custom_connectors.py#L276) | self, db, reason, chat_id, owner, connector_id |  |
| [cancel_credential_requests](../harness/mechanics/custom_connectors.py#L289) | self, reason, chat_id, owner |  |
| [_check_request_current](../harness/mechanics/custom_connectors.py#L296) | self, db, record, owner |  |
| [credential_request](../harness/mechanics/custom_connectors.py#L306) | self, request_id, owner, chat_id |  |
| [credential_requests](../harness/mechanics/custom_connectors.py#L311) | self, owner, chat_id |  |
| [_public_text](../harness/mechanics/custom_connectors.py#L318) | self, db, key, value |  |
| [request_credentials](../harness/mechanics/custom_connectors.py#L324) | self, key, owner, chat_id, collection, reason, expires_in |  |
| [resolve_credential_request](../harness/mechanics/custom_connectors.py#L351) | self, request_id, owner, chat_id, action, values, reason |  |
| [remove_secret](../harness/mechanics/custom_connectors.py#L380) | self, key, name, owner |  |
| [package](../harness/mechanics/custom_connectors.py#L389) | self, key, owner |  |
| [write](../harness/mechanics/custom_connectors.py#L395) | name, content |  |

### harness/mechanics/custom_coordinator.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [require](../harness/mechanics/custom_coordinator.py#L32) | value, code |  |
| [drain](../harness/mechanics/custom_coordinator.py#L35) | task | Cleanup/admission remain owned through repeated caller cancellation. |
| [offload](../harness/mechanics/custom_coordinator.py#L43) | fn, *args, **kwargs |  |
| [_private_dir](../harness/mechanics/custom_coordinator.py#L51) | path |  |
| [__init__](../harness/mechanics/custom_coordinator.py#L57) | self, root |  |
| [close](../harness/mechanics/custom_coordinator.py#L78) | self |  |
| [db](../harness/mechanics/custom_coordinator.py#L82) | self |  |
| [insert_batch](../harness/mechanics/custom_coordinator.py#L87) | self, batch |  |
| [pending](../harness/mechanics/custom_coordinator.py#L93) | self, key, owner, collection |  |
| [request_stop](../harness/mechanics/custom_coordinator.py#L97) | self, key, owner, collection |  |
| [allows_current](../harness/mechanics/custom_coordinator.py#L99) | self, batch |  |
| [state](../harness/mechanics/custom_coordinator.py#L110) | self, batch, state |  |
| [finish](../harness/mechanics/custom_coordinator.py#L112) | self, batch, state, current |  |
| [add_job](../harness/mechanics/custom_coordinator.py#L117) | self, batch, job |  |
| [jobs](../harness/mechanics/custom_coordinator.py#L119) | self, batch |  |
| [job_state](../harness/mechanics/custom_coordinator.py#L121) | self, job, state, broker, receipt, check |  |
| [__init__](../harness/mechanics/custom_coordinator.py#L127) | self, gateway, directory |  |
| [start](../harness/mechanics/custom_coordinator.py#L128) | self |  |
| [capture_signals](../harness/mechanics/custom_coordinator.py#L141) | self |  |
| [close](../harness/mechanics/custom_coordinator.py#L152) | self |  |
| [ensure_current](../harness/mechanics/custom_coordinator.py#L178) | self |  |
| [current](../harness/mechanics/custom_coordinator.py#L180) | self |  |
| [__init__](../harness/mechanics/custom_coordinator.py#L183) | self, manager, gateway, client, root, max_batches, batch_seconds, invoke_seconds, poll_seconds, socket_factory |  |
| [_scope](../harness/mechanics/custom_coordinator.py#L191) | self, batch |  |
| [_lock](../harness/mechanics/custom_coordinator.py#L193) | self, key, owner, collection, wait |  |
| [status](../harness/mechanics/custom_coordinator.py#L205) | self, key, owner, collection |  |
| [test](../harness/mechanics/custom_coordinator.py#L210) | self, key, owner, collection, expected_revision, cancelled |  |
| [invoke](../harness/mechanics/custom_coordinator.py#L212) | self, key, tool, arguments, owner, collection, cancelled |  |
| [_entry](../harness/mechanics/custom_coordinator.py#L214) | self, key, owner, collection, kind, parent_cancelled, **options |  |
| [_watch](../harness/mechanics/custom_coordinator.py#L231) | self, batch |  |
| [_begin](../harness/mechanics/custom_coordinator.py#L236) | self, batch, options |  |
| [_execute](../harness/mechanics/custom_coordinator.py#L246) | self, batch, options |  |
| [_job](../harness/mechanics/custom_coordinator.py#L281) | self, batch, tool_name, arguments |  |
| [_cleanup_job](../harness/mechanics/custom_coordinator.py#L346) | self, batch, job, lease, grant, listener |  |
| [_retire_batch](../harness/mechanics/custom_coordinator.py#L385) | self, batch, reason |  |
| [_maintenance](../harness/mechanics/custom_coordinator.py#L393) | self, operation |  |
| [stop](../harness/mechanics/custom_coordinator.py#L401) | self, key, owner, collection |  |
| [_stop](../harness/mechanics/custom_coordinator.py#L403) | self, key, owner, collection |  |
| [revoke](../harness/mechanics/custom_coordinator.py#L417) | self, key, owner, collection |  |
| [_revoke](../harness/mechanics/custom_coordinator.py#L419) | self, key, owner, collection |  |
| [reconcile](../harness/mechanics/custom_coordinator.py#L423) | self, key, owner, collection |  |
| [_reconcile](../harness/mechanics/custom_coordinator.py#L425) | self, key, owner, collection |  |
| [_reconcile_row](../harness/mechanics/custom_coordinator.py#L438) | self, row |  |
| [close](../harness/mechanics/custom_coordinator.py#L474) | self |  |

### harness/mechanics/custom_execution.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [require](../harness/mechanics/custom_execution.py#L36) | value, message |  |
| [encoded](../harness/mechanics/custom_execution.py#L40) | value |  |
| [digest](../harness/mechanics/custom_execution.py#L45) | value |  |
| [exact](../harness/mechanics/custom_execution.py#L48) | value, keys |  |
| [name](../harness/mechanics/custom_execution.py#L50) | value |  |
| [_validation](../harness/mechanics/custom_execution.py#L53) | function |  |
| [checked](../harness/mechanics/custom_execution.py#L55) | *args, **kwargs |  |
| [schema](../harness/mechanics/custom_execution.py#L63) | value | A bounded, fully expanded JSON-schema subset; no regex/remote resolution. |
| [walk](../harness/mechanics/custom_execution.py#L68) | node, depth |  |
| [validate_manifest](../harness/mechanics/custom_execution.py#L91) | value, files |  |
| [authentication_fields](../harness/mechanics/custom_execution.py#L119) | auth |  |
| [validate_target](../harness/mechanics/custom_execution.py#L126) | value, declared |  |
| [initialize_schema](../harness/mechanics/custom_execution.py#L166) | db |  |
| [authority](../harness/mechanics/custom_execution.py#L187) | db, key |  |
| [retained_fields](../harness/mechanics/custom_execution.py#L193) | db, key |  |
| [invalidate](../harness/mechanics/custom_execution.py#L198) | db, key, kind |  |
| [public_projection](../harness/mechanics/custom_execution.py#L208) | db, key |  |
| [public_values](../harness/mechanics/custom_execution.py#L217) | db, key, readers |  |
| [__post_init__](../harness/mechanics/custom_execution.py#L228) | self |  |
| [document](../harness/mechanics/custom_execution.py#L229) | self |  |
| [__post_init__](../harness/mechanics/custom_execution.py#L236) | self |  |
| [__post_init__](../harness/mechanics/custom_execution.py#L244) | self |  |
| [metadata](../harness/mechanics/custom_execution.py#L254) | self |  |
| [sha256](../harness/mechanics/custom_execution.py#L256) | self |  |
| [as_mapping](../harness/mechanics/custom_execution.py#L266) | self |  |
| [__post_init__](../harness/mechanics/custom_execution.py#L274) | self |  |
| [__init__](../harness/mechanics/custom_execution.py#L281) | self, store, runtime, clock |  |
| [_owned](../harness/mechanics/custom_execution.py#L287) | self, db, key, owner, collection |  |
| [status](../harness/mechanics/custom_execution.py#L292) | self, key, owner, collection |  |
| [grant_target](../harness/mechanics/custom_execution.py#L297) | self, key, target, owner, collection, expected_generation, expected_revision | Called only from authenticated owner target selection, never save/tools. |
| [_snapshot](../harness/mechanics/custom_execution.py#L318) | self, db, key, owner, collection, revision |  |
| [snapshot](../harness/mechanics/custom_execution.py#L351) | self, key, owner, collection, expected_revision |  |
| [_validate](../harness/mechanics/custom_execution.py#L357) | self, db, snapshot, owner, collection, draft |  |
| [validate_snapshot](../harness/mechanics/custom_execution.py#L371) | self, snapshot, owner, collection |  |
| [authority_current](../harness/mechanics/custom_execution.py#L375) | self, snapshot, owner, collection |  |
| [authority_probe](../harness/mechanics/custom_execution.py#L378) | self, snapshot, owner, collection | Cheap host-only wire fence after full off-thread snapshot validation. |
| [host_credentials](../harness/mechanics/custom_execution.py#L411) | self, snapshot, owner, collection | Host gateway only; hold its admission fence and recheck before I/O. |
| [active_snapshot](../harness/mechanics/custom_execution.py#L429) | self, key, owner, collection |  |
| [admit_job](../harness/mechanics/custom_execution.py#L439) | self, job_id, snapshot, owner, collection | Host coordinator only: persist before any broker admission/network. |
| [_owned_job](../harness/mechanics/custom_execution.py#L454) | self, db, job_id, owner, collection |  |
| [job_cleanup_state](../harness/mechanics/custom_execution.py#L461) | self, job_id, owner, collection |  |
| [mark_job_uncertain](../harness/mechanics/custom_execution.py#L466) | self, job_id, owner, collection |  |
| [confirm_job_cleanup](../harness/mechanics/custom_execution.py#L472) | self, job_id, receipt, owner, collection | Trusted exact-job recovery; source changes never establish cleanup. |
| [_cleanup_fence](../harness/mechanics/custom_execution.py#L487) | db, key |  |
| [begin_test](../harness/mechanics/custom_execution.py#L493) | self, key, owner, collection, expected_revision |  |
| [_test](../harness/mechanics/custom_execution.py#L506) | self, db, lease, owner, collection |  |
| [test_snapshot](../harness/mechanics/custom_execution.py#L517) | self, lease, owner, collection |  |
| [test_result](../harness/mechanics/custom_execution.py#L521) | self, test_id, owner, collection |  |
| [fail_test](../harness/mechanics/custom_execution.py#L534) | self, lease, owner, collection, reason |  |
| [confirm_test_cleanup](../harness/mechanics/custom_execution.py#L552) | self, lease, receipt, owner, collection | Trusted coordinator only, after reconciling that exact broker job. |
| [complete_test](../harness/mechanics/custom_execution.py#L572) | self, lease, evidence, owner, collection, current | Host coordinator only, after verified worker output and actual cleanup. |
| [activate](../harness/mechanics/custom_execution.py#L597) | self, test_id, owner, collection, expected_active_generation |  |
| [revoke](../harness/mechanics/custom_execution.py#L612) | self, key, owner, collection | Immediately closes new authority; caller then drains future runtime Stop. |

### harness/mechanics/custom_http.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [require](../harness/mechanics/custom_http.py#L42) | value, category |  |
| [_drain](../harness/mechanics/custom_http.py#L46) | task |  |
| [_offload](../harness/mechanics/custom_http.py#L54) | fn, *args |  |
| [_callback](../harness/mechanics/custom_http.py#L61) | fn, *args |  |
| [public_addresses](../harness/mechanics/custom_http.py#L68) | host |  |
| [validated_addresses](../harness/mechanics/custom_http.py#L73) | values |  |
| [_credential_echo](../harness/mechanics/custom_http.py#L89) | raw, content_type, secrets_ |  |
| [__init__](../harness/mechanics/custom_http.py#L111) | self, stream, current |  |
| [read](../harness/mechanics/custom_http.py#L112) | self, max_bytes, timeout |  |
| [write](../harness/mechanics/custom_http.py#L113) | self, buffer, timeout |  |
| [aclose](../harness/mechanics/custom_http.py#L116) | self |  |
| [start_tls](../harness/mechanics/custom_http.py#L117) | self, ssl_context, server_hostname, timeout |  |
| [get_extra_info](../harness/mechanics/custom_http.py#L121) | self, info |  |
| [__init__](../harness/mechanics/custom_http.py#L126) | self, host, addresses, current, backend |  |
| [connect_tcp](../harness/mechanics/custom_http.py#L129) | self, host, port, timeout, local_address, socket_options |  |
| [connect_unix_socket](../harness/mechanics/custom_http.py#L136) | self, *args, **kwargs |  |
| [sleep](../harness/mechanics/custom_http.py#L137) | self, seconds |  |
| [document](../harness/mechanics/custom_http.py#L153) | self |  |
| [__init__](../harness/mechanics/custom_http.py#L184) | self, company_id, max_calls, per_job_calls, request_seconds, resolver, network_backend, ssl_context, clock |  |
| [issue](../harness/mechanics/custom_http.py#L195) | self, snapshot, tool, validate, credentials, current, cancelled, ttl_seconds |  |
| [_issue](../harness/mechanics/custom_http.py#L206) | self, snapshot, tool, validate, credentials, current, cancelled, ttl_seconds |  |
| [_alive](../harness/mechanics/custom_http.py#L232) | self, job |  |
| [_job](../harness/mechanics/custom_http.py#L237) | self, token |  |
| [_request](../harness/mechanics/custom_http.py#L243) | self, job, document |  |
| [_headers](../harness/mechanics/custom_http.py#L263) | self, job, values |  |
| [value](../harness/mechanics/custom_http.py#L267) | field |  |
| [request](../harness/mechanics/custom_http.py#L284) | self, token, document |  |
| [_execute](../harness/mechanics/custom_http.py#L303) | self, job, operation, url |  |
| [observations](../harness/mechanics/custom_http.py#L349) | self, grant_id | Host-only journal; caller binds grant ID to its admitted worker/test. |
| [revoke](../harness/mechanics/custom_http.py#L355) | self, grant_id |  |
| [close](../harness/mechanics/custom_http.py#L367) | self |  |
| [__call__](../harness/mechanics/custom_http.py#L375) | self, scope, receive, send |  |

### harness/mechanics/custom_routes.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [body](../harness/mechanics/custom_routes.py#L14) | request, fields |  |
| [register_custom_routes](../harness/mechanics/custom_routes.py#L30) | app, identity, owner_for_connector |  |
| [selected](../harness/mechanics/custom_routes.py#L31) | request, key, write |  |
| [execution](../harness/mechanics/custom_routes.py#L41) | connector_id, request |  |
| [target](../harness/mechanics/custom_routes.py#L49) | connector_id, request |  |
| [activate](../harness/mechanics/custom_routes.py#L61) | connector_id, request |  |
| [test](../harness/mechanics/custom_routes.py#L78) | connector_id, request |  |
| [revoke](../harness/mechanics/custom_routes.py#L98) | connector_id, request |  |
| [stop](../harness/mechanics/custom_routes.py#L109) | connector_id, request |  |

### harness/mechanics/custom_runtime.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/mechanics/custom_runtime.py#L13) | self, store, client, coordinator_factory |  |
| [_initialize](../harness/mechanics/custom_runtime.py#L25) | self |  |
| [ready](../harness/mechanics/custom_runtime.py#L38) | self |  |
| [test](../harness/mechanics/custom_runtime.py#L50) | self, *args, **kwargs |  |
| [invoke](../harness/mechanics/custom_runtime.py#L54) | self, *args, **kwargs |  |
| [status](../harness/mechanics/custom_runtime.py#L58) | self, *args, **kwargs |  |
| [stop](../harness/mechanics/custom_runtime.py#L62) | self, *args, **kwargs |  |
| [revoke](../harness/mechanics/custom_runtime.py#L66) | self, *args, **kwargs |  |
| [close](../harness/mechanics/custom_runtime.py#L70) | self |  |

### harness/mechanics/custom_setup.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/mechanics/custom_setup.py#L12) | self, manager |  |
| [propose](../harness/mechanics/custom_setup.py#L16) | self, key, target, reason, expected_revision, owner, collection |  |
| [approve](../harness/mechanics/custom_setup.py#L47) | self, key, proposal_id, owner, collection |  |
| [describe](../harness/mechanics/custom_setup.py#L59) | self, key, owner, collection |  |

### harness/mechanics/custom_tool_contracts.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [object_schema](../harness/mechanics/custom_tool_contracts.py#L29) | properties, required |  |
| [execution_schema](../harness/mechanics/custom_tool_contracts.py#L34) |  |  |
| [target_schema](../harness/mechanics/custom_tool_contracts.py#L47) |  |  |
| [tool_specs](../harness/mechanics/custom_tool_contracts.py#L56) |  |  |

### harness/mechanics/custom_worker.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [need](../harness/mechanics/custom_worker.py#L29) | value |  |
| [canonical](../harness/mechanics/custom_worker.py#L31) | value |  |
| [digest](../harness/mechanics/custom_worker.py#L32) | value |  |
| [path_parts](../harness/mechanics/custom_worker.py#L33) | value |  |
| [request](../harness/mechanics/custom_worker.py#L39) | value |  |
| [bundle](../harness/mechanics/custom_worker.py#L48) | value, expected, company, owner, image, worker_sha256 |  |
| [read_regular](../harness/mechanics/custom_worker.py#L72) | path, limit |  |
| [run](../harness/mechanics/custom_worker.py#L80) | source, config, workspace, execute |  |

### harness/mechanics/delegated_jobs.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [specs](../harness/mechanics/delegated_jobs.py#L21) | write |  |
| [role_plan](../harness/mechanics/delegated_jobs.py#L30) | agent, chat_id |  |
| [role](../harness/mechanics/delegated_jobs.py#L47) | self |  |
| [current](../harness/mechanics/delegated_jobs.py#L50) | self |  |
| [configuration](../harness/mechanics/delegated_jobs.py#L70) | self, tools |  |
| [__init__](../harness/mechanics/delegated_jobs.py#L81) | self, state |  |
| [claim](../harness/mechanics/delegated_jobs.py#L91) | self, context, role, task, call |  |
| [save](../harness/mechanics/delegated_jobs.py#L128) | self, job |  |
| [children](../harness/mechanics/delegated_jobs.py#L132) | self, binding_id |  |
| [execute](../harness/mechanics/delegated_jobs.py#L137) | self, context, role, task, call |  |
| [result](../harness/mechanics/delegated_jobs.py#L173) | job, child |  |
| [_run](../harness/mechanics/delegated_jobs.py#L178) | self, context, job, child, grant |  |
| [acall](../harness/mechanics/delegated_jobs.py#L212) | context, name, arguments |  |
| [withdraw_children](../harness/mechanics/delegated_jobs.py#L223) | runtime, agent, parent_binding | Cancellation uses original saved IDs and needs no renewed tool authority. |

### harness/mechanics/document_preview_contract.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__post_init__](../harness/mechanics/document_preview_contract.py#L22) | self |  |
| [parse](../harness/mechanics/document_preview_contract.py#L27) | cls, value |  |
| [validate_manifest](../harness/mechanics/document_preview_contract.py#L31) | manifest, files, request, original_sha256, original_bytes |  |
| [require](../harness/mechanics/document_preview_contract.py#L32) | condition |  |

### harness/mechanics/document_preview_readiness.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [root_bytes](../harness/mechanics/document_preview_readiness.py#L21) | path, uid |  |
| [__init__](../harness/mechanics/document_preview_readiness.py#L37) | self, enabled, receipt_sha256, receipt_path, reader |  |
| [ready](../harness/mechanics/document_preview_readiness.py#L42) | self |  |

### harness/mechanics/document_preview_routes.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [deny](../harness/mechanics/document_preview_routes.py#L17) | status, code |  |
| [identity](../harness/mechanics/document_preview_routes.py#L19) | request, write |  |
| [empty_body](../harness/mechanics/document_preview_routes.py#L37) | request |  |
| [register_document_preview_routes](../harness/mechanics/document_preview_routes.py#L52) | app, previews_for_workspace, owner_for_file |  |
| [selected](../harness/mechanics/document_preview_routes.py#L53) | request, file_id, write |  |
| [metadata](../harness/mechanics/document_preview_routes.py#L65) | file_id, request |  |
| [prepare](../harness/mechanics/document_preview_routes.py#L71) | file_id, request |  |
| [disconnected](../harness/mechanics/document_preview_routes.py#L78) |  |  |
| [page](../harness/mechanics/document_preview_routes.py#L101) | file_id, page, request |  |

### harness/mechanics/document_preview_worker.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [regular](../harness/mechanics/document_preview_worker.py#L38) | path, maximum |  |
| [checksum](../harness/mechanics/document_preview_worker.py#L44) | path |  |
| [tree_bytes](../harness/mechanics/document_preview_worker.py#L50) | root |  |
| [run](../harness/mechanics/document_preview_worker.py#L63) | argv, work, limits, deadline, capture |  |
| [check_ooxml](../harness/mechanics/document_preview_worker.py#L88) | path, format |  |
| [png_dimensions](../harness/mechanics/document_preview_worker.py#L119) | path |  |
| [prepare](../harness/mechanics/document_preview_worker.py#L125) | file_id, format, source, output, limits |  |
| [main](../harness/mechanics/document_preview_worker.py#L176) |  |  |

### harness/mechanics/document_previews.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [require](../harness/mechanics/document_previews.py#L24) | value, code |  |
| [digest](../harness/mechanics/document_previews.py#L27) | raw |  |
| [canonical](../harness/mechanics/document_previews.py#L28) | value |  |
| [offload](../harness/mechanics/document_previews.py#L30) | function, *args, **kwargs |  |
| [__init__](../harness/mechanics/document_previews.py#L39) | self, files, client, enabled, cache_bytes |  |
| [db](../harness/mechanics/document_previews.py#L58) | self, write |  |
| [original](../harness/mechanics/document_previews.py#L74) | self, file_id, owner |  |
| [row](../harness/mechanics/document_previews.py#L91) | self, key |  |
| [_status](../harness/mechanics/document_previews.py#L94) | self, key, status |  |
| [content](../harness/mechanics/document_previews.py#L97) | self, file_id, owner |  |
| [_body](../harness/mechanics/document_previews.py#L116) | self, key, name |  |
| [page](../harness/mechanics/document_previews.py#L121) | self, file_id, page, owner |  |
| [lock](../harness/mechanics/document_previews.py#L130) | self, key |  |
| [_begin](../harness/mechanics/document_previews.py#L141) | self, key, record, owner, generation |  |
| [_save](../harness/mechanics/document_previews.py#L148) | self, key, record, owner, manifest, contents |  |
| [prepare](../harness/mechanics/document_previews.py#L158) | self, file_id, owner |  |
| [cleanup](../harness/mechanics/document_previews.py#L224) |  |  |

### harness/mechanics/document_rendering.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [render](../harness/mechanics/document_rendering.py#L26) | suffix, title, content |  |
| [_inline](../harness/mechanics/document_rendering.py#L53) | tokens |  |
| [_blocks](../harness/mechanics/document_rendering.py#L70) | content |  |
| [_docx](../harness/mechanics/document_rendering.py#L115) | title, content |  |
| [add_runs](../harness/mechanics/document_rendering.py#L132) | paragraph, runs |  |
| [_pdf](../harness/mechanics/document_rendering.py#L158) | title, content |  |
| [text](../harness/mechanics/document_rendering.py#L180) | runs |  |
| [footer](../harness/mechanics/document_rendering.py#L202) | canvas, document |  |
| [_xlsx](../harness/mechanics/document_rendering.py#L218) | title, content |  |
| [_worker](../harness/mechanics/document_rendering.py#L260) |  |  |

### harness/mechanics/harness_routes.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [shell](../harness/mechanics/harness_routes.py#L25) | selected, session, collection, guards | The active template's shell with the reader's fixed conversation ids for one collection. |
| [register_harness_routes](../harness/mechanics/harness_routes.py#L49) | app |  |
| [harness](../harness/mechanics/harness_routes.py#L51) | request, collection |  |

### harness/mechanics/harness_tools.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_listed](../harness/mechanics/harness_tools.py#L318) | names |  |
| [source_reference](../harness/mechanics/harness_tools.py#L323) | name | Repository documentation references follow the selected source layout. |
| [capability_rows](../harness/mechanics/harness_tools.py#L345) | template | The table for one template: its own rows first, then the harness rows with the sentences it adds. |
| [capability_problems](../harness/mechanics/harness_tools.py#L369) | template | What keeps a vertical's rows from joining the table, as sentences. Empty means the table is whole. |
| [capabilities](../harness/mechanics/harness_tools.py#L388) | template | The table as rows an agent reads: id, title, state and the three statements that hold words. |
| [capability_table](../harness/mechanics/harness_tools.py#L394) | template | The table as README.md prints it: the rows of the default vertical, one markdown row each with its files. |
| [write_readme](../harness/mechanics/harness_tools.py#L404) | path | Put the table into the front door, in place of the one it holds. |
| [developer_prompt](../harness/mechanics/harness_tools.py#L418) | template | The paragraph that tells an agent what it is part of and that get_harness answers the rest. |
| [specs](../harness/mechanics/harness_tools.py#L442) | write |  |
| [read](../harness/mechanics/harness_tools.py#L448) | context, name, args |  |
| [call](../harness/mechanics/harness_tools.py#L457) | context, name, args |  |
| [registry](../harness/mechanics/harness_tools.py#L463) | agent | Report the selected workspace registry used by its live tool transports. |
| [serve](../harness/mechanics/harness_tools.py#L476) | context, name, arguments |  |
| [_tools](../harness/mechanics/harness_tools.py#L498) | live |  |
| [_problems](../harness/mechanics/harness_tools.py#L527) | template, live | What the manifest names and the running service lacks, as sentences. Empty means they agree. |
| [_layers](../harness/mechanics/harness_tools.py#L547) | template |  |
| [_built_with](../harness/mechanics/harness_tools.py#L574) | template |  |
| [_fixed_conversations](../harness/mechanics/harness_tools.py#L583) | template |  |
| [_agents](../harness/mechanics/harness_tools.py#L588) | context, kind, default | The reader's own agents of one class in this collection, where the surface holds the agent store. |
| [_agent_classes](../harness/mechanics/harness_tools.py#L609) | context, template |  |
| [_ready_agents](../harness/mechanics/harness_tools.py#L615) | template |  |
| [_channels](../harness/mechanics/harness_tools.py#L620) | context, template |  |
| [_tile_sets](../harness/mechanics/harness_tools.py#L631) | template |  |
| [_vocabulary](../harness/mechanics/harness_tools.py#L638) | template |  |
| [_skills](../harness/mechanics/harness_tools.py#L645) | context, template, live | The skills of the company where the surface holds its stores; the vertical's seeds everywhere. |
| [_count](../harness/mechanics/harness_tools.py#L667) | result | How many rows a listing read returned, by the name of each list it holds. |
| [_connected](../harness/mechanics/harness_tools.py#L676) | context, source, live | Whether the company has rows in one data source today, from the reads the registry serves. |
| [_data_sources](../harness/mechanics/harness_tools.py#L698) | context, template, live |  |
| [describe](../harness/mechanics/harness_tools.py#L709) | context, section, template | The answer of get_harness for one reader: `context` is the ReadContext the registry hands a read. |
| [main](../harness/mechanics/harness_tools.py#L742) | arguments |  |

### harness/mechanics/intake_instructions.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__getattr__](../harness/mechanics/intake_instructions.py#L15) | name |  |
| [for_chat](../harness/mechanics/intake_instructions.py#L23) | agent, chat_id, base | Attach only host-authenticated purpose instructions, including on resume. |

### harness/mechanics/local_workspace.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [local_services](../harness/mechanics/local_workspace.py#L5) | state, principal_id, dataset, derivatives_enabled |  |
| [local_authority](../harness/mechanics/local_workspace.py#L14) | self, actor, collection |  |
| [read_admission](../harness/mechanics/local_workspace.py#L17) | self, actor, collection |  |

### harness/mechanics/managed_connections.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/mechanics/managed_connections.py#L20) | self, store, scope, relay, run, current |  |
| [deliver](../harness/mechanics/managed_connections.py#L26) | self, item, guard |  |
| [request](../harness/mechanics/managed_connections.py#L32) | self, server, tool, arguments, identity |  |
| [__init__](../harness/mechanics/managed_connections.py#L63) | self, agent, chat_id, run, relay |  |
| [current](../harness/mechanics/managed_connections.py#L72) | self |  |
| [execute](../harness/mechanics/managed_connections.py#L83) | self, provider, tool, arguments, identity |  |
| [close](../harness/mechanics/managed_connections.py#L106) | self |  |
| [write_connection](../harness/mechanics/managed_connections.py#L111) | agent, chat_id, arguments |  |

### harness/mechanics/managed_mcp.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_identity](../harness/mechanics/managed_mcp.py#L37) | value |  |
| [_private_file](../harness/mechanics/managed_mcp.py#L43) | path, create |  |
| [id](../harness/mechanics/managed_mcp.py#L80) | self |  |
| [current](../harness/mechanics/managed_mcp.py#L82) | self |  |
| [close](../harness/mechanics/managed_mcp.py#L96) | self |  |
| [admit](../harness/mechanics/managed_mcp.py#L103) | self, grant |  |
| [__init__](../harness/mechanics/managed_mcp.py#L119) | self, host, row, services |  |
| [session_id](../harness/mechanics/managed_mcp.py#L126) | self |  |
| [tools](../harness/mechanics/managed_mcp.py#L129) | self | Send this only in the provider credential field, never a chat or receipt. |
| [record_current](../harness/mechanics/managed_mcp.py#L136) | self |  |
| [created](../harness/mechanics/managed_mcp.py#L144) | self, provider_session_id | Bind the API-issued session once; a conflicting response cannot adopt it. |
| [begin](../harness/mechanics/managed_mcp.py#L155) | self, actor, admission, cancel, deadline, current_run, quiesced, run, request_id, recovering | Host-only: quiesced certifies reconciled root and inherited children. |
| [current](../harness/mechanics/managed_mcp.py#L193) | self |  |
| [end](../harness/mechanics/managed_mcp.py#L197) | self, generation, disconnected | Withdraw immediately; closing an old generation cannot stop its successor. |
| [revoke](../harness/mechanics/managed_mcp.py#L212) | self, generation |  |
| [_pending_reads](../harness/mechanics/managed_mcp.py#L222) | self |  |
| [drain](../harness/mechanics/managed_mcp.py#L226) | self | Retain captured snapshots while the transport drains actual worker reads. |
| [__init__](../harness/mechanics/managed_mcp.py#L238) | self, state, public_origin, clock, monotonic |  |
| [_initialize](../harness/mechanics/managed_mcp.py#L248) | self |  |
| [_db](../harness/mechanics/managed_mcp.py#L275) | self |  |
| [_require_epoch](../harness/mechanics/managed_mcp.py#L283) | self, db |  |
| [_row](../harness/mechanics/managed_mcp.py#L288) | self, binding_id |  |
| [_token](../harness/mechanics/managed_mcp.py#L295) | self, key |  |
| [bind_session](../harness/mechanics/managed_mcp.py#L299) | self, binding_id, company_id, data_owner, root_chat, collection, services |  |
| [revoke_binding](../harness/mechanics/managed_mcp.py#L329) | self, binding_id | Withdraw a saved session even when restart has no live generation. |
| [_current_generation](../harness/mechanics/managed_mcp.py#L343) | self, generation |  |
| [authenticate](../harness/mechanics/managed_mcp.py#L351) | self, token |  |
| [active](../harness/mechanics/managed_mcp.py#L364) | self, key |  |
| [resolve](../harness/mechanics/managed_mcp.py#L369) | self, grant |  |
| [lifespan](../harness/mechanics/managed_mcp.py#L375) | self |  |

### harness/mechanics/managed_sessions.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [identity](../harness/mechanics/managed_sessions.py#L26) | value |  |
| [encoded](../harness/mechanics/managed_sessions.py#L32) | value |  |
| [digest](../harness/mechanics/managed_sessions.py#L36) | value |  |
| [new_key](../harness/mechanics/managed_sessions.py#L40) |  |  |
| [__init__](../harness/mechanics/managed_sessions.py#L47) | self, state |  |
| [_private_file](../harness/mechanics/managed_sessions.py#L89) | self, create |  |
| [transaction](../harness/mechanics/managed_sessions.py#L103) | self |  |
| [_migrate](../harness/mechanics/managed_sessions.py#L118) | self |  |
| [fingerprint](../harness/mechanics/managed_sessions.py#L169) | configuration, capabilities |  |
| [_binding_record](../harness/mechanics/managed_sessions.py#L174) | row |  |
| [_insert](../harness/mechanics/managed_sessions.py#L182) | self, db, values, configuration, capabilities, generation |  |
| [binding](../harness/mechanics/managed_sessions.py#L192) | self, company_id, chat_id, owner, collection, configuration, capabilities |  |
| [rollover](../harness/mechanics/managed_sessions.py#L206) | self, company_id, chat_id, owner, collection, configuration, previous_id, quiesced, capabilities |  |
| [retire](../harness/mechanics/managed_sessions.py#L223) | self, binding_id, reason |  |
| [retired](../harness/mechanics/managed_sessions.py#L228) | self, binding_id |  |
| [for_owner](../harness/mechanics/managed_sessions.py#L233) | self, company_id, owner |  |
| [generations](../harness/mechanics/managed_sessions.py#L239) | self, company_id, chat_id |  |
| [artifact](../harness/mechanics/managed_sessions.py#L245) | self, binding_id, artifact_id, metadata, file_id |  |
| [request_binding](../harness/mechanics/managed_sessions.py#L258) | self, company_id, chat_id, logical_id |  |
| [pending_binding](../harness/mechanics/managed_sessions.py#L265) | self, company_id, chat_id |  |
| [get](../harness/mechanics/managed_sessions.py#L273) | self, binding_id |  |
| [created](../harness/mechanics/managed_sessions.py#L280) | self, binding_id, session_id |  |
| [submission](../harness/mechanics/managed_sessions.py#L287) | self, binding_id, logical_id, kind, payload |  |
| [claim](../harness/mechanics/managed_sessions.py#L301) | self, binding_id, action, generation, actor_chat, write, recoverable |  |
| [completed](../harness/mechanics/managed_sessions.py#L332) | self, binding_id, call_id, generation, receipt |  |
| [save_delivery_boundary](../harness/mechanics/managed_sessions.py#L346) | self, binding_id, request_id, call_id, delivery | Stop recovery at the original durable send, even after a lost result reply. |
| [delivery_boundary](../harness/mechanics/managed_sessions.py#L366) | self, binding_id, request_id |  |
| [turn](../harness/mechanics/managed_sessions.py#L372) | self, binding_id, turn, actor_chat |  |
| [turns](../harness/mechanics/managed_sessions.py#L393) | self, binding_id |  |
| [_request_record](../harness/mechanics/managed_sessions.py#L399) | row |  |
| [request](../harness/mechanics/managed_sessions.py#L407) | self, binding_id, logical_id, input_value | A pending outbox keeps exact input until its provider turn is terminal. |
| [request_record](../harness/mechanics/managed_sessions.py#L439) | self, binding_id, logical_id | Read one original input without admitting or changing it. |
| [pending](../harness/mechanics/managed_sessions.py#L446) | self, binding_id |  |
| [for_chat](../harness/mechanics/managed_sessions.py#L451) | self, company_id, chat_id |  |
| [request_state](../harness/mechanics/managed_sessions.py#L457) | self, request_id, status, baseline, turn_id |  |

### harness/mechanics/managed_usage.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [identity](../harness/mechanics/managed_usage.py#L16) | value |  |
| [__init__](../harness/mechanics/managed_usage.py#L23) | self, pool |  |
| [_request](../harness/mechanics/managed_usage.py#L50) | self, db, request_id |  |
| [request](../harness/mechanics/managed_usage.py#L55) | self, request_id |  |
| [monitor](../harness/mechanics/managed_usage.py#L58) | self, request_id, initial | Persist the original target/deadline beside its existing funding hold. |
| [save_monitor](../harness/mechanics/managed_usage.py#L73) | self, request_id, receipt |  |
| [capacity](../harness/mechanics/managed_usage.py#L88) | self, binding_id, session_id |  |
| [reserve](../harness/mechanics/managed_usage.py#L96) | self, **arguments |  |
| [_reserve](../harness/mechanics/managed_usage.py#L101) | self, db, binding_id, request_id, actor, model, limit_cents, session_id, recovering |  |
| [role_plan](../harness/mechanics/managed_usage.py#L146) | self, parent_request |  |
| [reserve_parent](../harness/mechanics/managed_usage.py#L152) | self, roles, **arguments |  |
| [activate_role](../harness/mechanics/managed_usage.py#L193) | self, parent_request, role_id, ordinal, binding_id, request_id, actor, model, limit_cents, session_id, recovering |  |
| [release_unused_roles](../harness/mechanics/managed_usage.py#L230) | self, parent_request |  |
| [created](../harness/mechanics/managed_usage.py#L246) | self, binding_id, session_id |  |
| [finish](../harness/mechanics/managed_usage.py#L256) | self, request_id, snapshot, terminal_status |  |
| [settle_closed](../harness/mechanics/managed_usage.py#L276) | self, binding_id, receipt_path | Operator-only, provider-final reconciliation; estimates cannot call this. |

### harness/mechanics/mcp_access.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [public](../harness/mechanics/mcp_access.py#L31) | self |  |
| [__init__](../harness/mechanics/mcp_access.py#L39) | self, state, clock |  |
| [_db](../harness/mechanics/mcp_access.py#L56) | self |  |
| [_scope](../harness/mechanics/mcp_access.py#L63) | company_id, owner_principal_id, dataset |  |
| [_row](../harness/mechanics/mcp_access.py#L70) | row |  |
| [issue](../harness/mechanics/mcp_access.py#L72) | self, company_id, owner_principal_id, dataset, label, ttl_seconds | Host-only: authenticate and authorize the requested scope before calling. |
| [list](../harness/mechanics/mcp_access.py#L86) | self, company_id, owner_principal_id |  |
| [get](../harness/mechanics/mcp_access.py#L90) | self, key, company_id, owner_principal_id |  |
| [revoke](../harness/mechanics/mcp_access.py#L96) | self, key, company_id, owner_principal_id |  |
| [authenticate](../harness/mechanics/mcp_access.py#L105) | self, token |  |
| [active](../harness/mechanics/mcp_access.py#L110) | self, key |  |

### harness/mechanics/mcp_connections.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_now](../harness/mechanics/mcp_connections.py#L56) |  |  |
| [_hash](../harness/mechanics/mcp_connections.py#L60) | value |  |
| [_identity](../harness/mechanics/mcp_connections.py#L64) | value |  |
| [_binding](../harness/mechanics/mcp_connections.py#L70) | value |  |
| [_provider](../harness/mechanics/mcp_connections.py#L76) | value |  |
| [validate_provider_url](../harness/mechanics/mcp_connections.py#L81) | url, hosts |  |
| [filter](../harness/mechanics/mcp_connections.py#L94) | self, record |  |
| [__init__](../harness/mechanics/mcp_connections.py#L107) | self, stream |  |
| [__aiter__](../harness/mechanics/mcp_connections.py#L108) | self |  |
| [aclose](../harness/mechanics/mcp_connections.py#L114) | self |  |
| [__init__](../harness/mechanics/mcp_connections.py#L118) | self, hosts |  |
| [handle_async_request](../harness/mechanics/mcp_connections.py#L121) | self, request |  |
| [public](../harness/mechanics/mcp_connections.py#L126) | value |  |
| [aclose](../harness/mechanics/mcp_connections.py#L143) | self |  |
| [__init__](../harness/mechanics/mcp_connections.py#L147) | self, broker, principal, provider, generation |  |
| [get_tokens](../harness/mechanics/mcp_connections.py#L150) | self |  |
| [set_tokens](../harness/mechanics/mcp_connections.py#L154) | self, tokens |  |
| [get_client_info](../harness/mechanics/mcp_connections.py#L168) | self |  |
| [set_client_info](../harness/mechanics/mcp_connections.py#L171) | self, client_info |  |
| [__init__](../harness/mechanics/mcp_connections.py#L187) | self, requested_scopes, token_auth_method, allow_authorization, refresh_token_endpoint, registered_policy, current, *args, **kwargs |  |
| [_initialize](../harness/mechanics/mcp_connections.py#L194) | self |  |
| [_refresh_token](../harness/mechanics/mcp_connections.py#L198) | self |  |
| [_clamp](../harness/mechanics/mcp_connections.py#L209) | self |  |
| [_perform_authorization_code_grant](../harness/mechanics/mcp_connections.py#L230) | self |  |
| [_auth_flow](../harness/mechanics/mcp_connections.py#L235) | self, request |  |
| [__post_init__](../harness/mechanics/mcp_connections.py#L314) | self |  |
| [__init__](../harness/mechanics/mcp_connections.py#L323) | self, token, endpoint, current |  |
| [auth_flow](../harness/mechanics/mcp_connections.py#L324) | self, request |  |
| [__init__](../harness/mechanics/mcp_connections.py#L332) | self, state, public_origin, flow_timeout, write_providers, registered_clients, remote_providers |  |
| [_revoke_configuration](../harness/mechanics/mcp_connections.py#L419) | db, provider |  |
| [_provider](../harness/mechanics/mcp_connections.py#L424) | self, provider |  |
| [provider_policy](../harness/mechanics/mcp_connections.py#L428) | self, provider | Host-only defensive copy; request data cannot modify broker authority. |
| [provider_policies](../harness/mechanics/mcp_connections.py#L433) | self |  |
| [_client](../harness/mechanics/mcp_connections.py#L436) | self, provider |  |
| [_configured](../harness/mechanics/mcp_connections.py#L439) | self, provider |  |
| [_configuration_current](../harness/mechanics/mcp_connections.py#L443) | self, db, provider |  |
| [provider_available](../harness/mechanics/mcp_connections.py#L455) | self, provider | Host-only configured authority, distinct from customer consent. |
| [provider_policy_revision](../harness/mechanics/mcp_connections.py#L460) | self, provider |  |
| [_db](../harness/mechanics/mcp_connections.py#L468) | self |  |
| [write_providers](../harness/mechanics/mcp_connections.py#L483) | self |  |
| [recover](../harness/mechanics/mcp_connections.py#L486) | self |  |
| [_record](../harness/mechanics/mcp_connections.py#L492) | self, provider, principal |  |
| [_check](../harness/mechanics/mcp_connections.py#L504) | self, provider, principal, generation, connected |  |
| [_update](../harness/mechanics/mcp_connections.py#L511) | self, provider, principal, generation, **changes |  |
| [_begin](../harness/mechanics/mcp_connections.py#L523) | self, provider, principal, access_mode |  |
| [_invalidate](../harness/mechanics/mcp_connections.py#L544) | self, provider, principal, generation |  |
| [_flow_state](../harness/mechanics/mcp_connections.py#L550) | self, flow, status |  |
| [catalogue](../harness/mechanics/mcp_connections.py#L555) | self, principal_id |  |
| [read_generation](../harness/mechanics/mcp_connections.py#L580) | self, provider, principal_id | Host-only connection identity, excluding OAuth material. |
| [capabilities](../harness/mechanics/mcp_connections.py#L591) | self, principal_id | Host-only capability summary from the last successful tool discovery. |
| [start](../harness/mechanics/mcp_connections.py#L603) | self, provider, principal_id, session_binding, access_mode |  |
| [connect_bearer](../harness/mechanics/mcp_connections.py#L608) | self, provider, credential, principal_id, session_binding, access_mode |  |
| [_start](../harness/mechanics/mcp_connections.py#L615) | self, provider, principal_id, session_binding, access_mode, credential |  |
| [_connect](../harness/mechanics/mcp_connections.py#L648) | self, flow |  |
| [_failed](../harness/mechanics/mcp_connections.py#L671) | self, flow, status |  |
| [_redirect](../harness/mechanics/mcp_connections.py#L676) | self, flow, url |  |
| [flow_status](../harness/mechanics/mcp_connections.py#L698) | self, flow_id, principal_id, session_binding |  |
| [oauth_callback](../harness/mechanics/mcp_connections.py#L709) | self, state, code, principal_id, session_binding, error |  |
| [_session](../harness/mechanics/mcp_connections.py#L732) | self, provider, principal, generation, flow |  |
| [redirect](../harness/mechanics/mcp_connections.py#L739) | url |  |
| [callback](../harness/mechanics/mcp_connections.py#L742) |  |  |
| [_listed](../harness/mechanics/mcp_connections.py#L765) | self, session, provider |  |
| [review](../harness/mechanics/mcp_connections.py#L777) | value, depth |  |
| [_scope_fence](../harness/mechanics/mcp_connections.py#L796) | self, provider, principal |  |
| [admission](../harness/mechanics/mcp_connections.py#L816) | self, provider, principal_id, expected_generation | Host-only dispatch fence; no OAuth, effects, retry, or approval claim. |
| [dispatch_admission](../harness/mechanics/mcp_connections.py#L832) | self, provider, principal_id, expected_generation | Shared provider capacity plus the current-account dispatch fence. |
| [dispatch_credentials](../harness/mechanics/mcp_connections.py#L838) | self, provider, principal_id, expected_generation, minimum_validity_seconds | Fixed credential snapshot only inside admission; never starts OAuth. |
| [_operation](../harness/mechanics/mcp_connections.py#L853) | self, provider, principal, expected_generation |  |
| [public_error](../harness/mechanics/mcp_connections.py#L873) | error |  |
| [tools](../harness/mechanics/mcp_connections.py#L883) | self, provider, principal_id, expected_generation |  |
| [_write_enabled](../harness/mechanics/mcp_connections.py#L897) | self, provider, config, row |  |
| [execution_binding](../harness/mechanics/mcp_connections.py#L904) | self, provider, tool, principal_id, expected_generation |  |
| [_redact_credentials](../harness/mechanics/mcp_connections.py#L917) | self, value, provider, principal, generation |  |
| [call](../harness/mechanics/mcp_connections.py#L929) | self, provider, tool, arguments, principal_id, expected_generation |  |
| [deny_schema_io](../harness/mechanics/mcp_connections.py#L940) | uri |  |
| [_cancel_flows](../harness/mechanics/mcp_connections.py#L954) | self, provider, principal |  |
| [disconnect](../harness/mechanics/mcp_connections.py#L959) | self, provider, principal_id |  |
| [finish](../harness/mechanics/mcp_connections.py#L970) |  |  |
| [close](../harness/mechanics/mcp_connections.py#L989) | self |  |

### harness/mechanics/mcp_host.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_read](../harness/mechanics/mcp_host.py#L22) | function, *args, **kwargs | Retain the transport's admission until a cancelled host read finishes. |
| [__init__](../harness/mechanics/mcp_host.py#L48) | self, state, access, services_for_environment, public_origin |  |
| [_environment](../harness/mechanics/mcp_host.py#L56) | self, company_id, principal |  |
| [resolve](../harness/mechanics/mcp_host.py#L71) | self, grant |  |
| [register_routes](../harness/mechanics/mcp_host.py#L84) | self, app |  |
| [actor](../harness/mechanics/mcp_host.py#L85) | request, writable |  |
| [connections](../harness/mechanics/mcp_host.py#L98) | request |  |
| [create_connection](../harness/mechanics/mcp_host.py#L106) | request |  |
| [revoke_connection](../harness/mechanics/mcp_host.py#L136) | key, request |  |

### harness/mechanics/mcp_server.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/mechanics/mcp_server.py#L21) | self, services, principal, collection |  |
| [visible_names](../harness/mechanics/mcp_server.py#L27) | self |  |
| [list_tools](../harness/mechanics/mcp_server.py#L35) | self |  |
| [call_tool](../harness/mechanics/mcp_server.py#L40) | self, name, arguments |  |
| [_read](../harness/mechanics/mcp_server.py#L48) | self, name, arguments |  |
| [make_server](../harness/mechanics/mcp_server.py#L71) | state, principal_id, dataset, derivatives_enabled, services |  |

### harness/mechanics/messaging.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [require](../harness/mechanics/messaging.py#L59) | value, message |  |
| [__post_init__](../harness/mechanics/messaging.py#L72) | self |  |
| [upgrade](../harness/mechanics/messaging.py#L116) | db | Bring an existing store to SCHEMA_VERSION inside the caller's transaction. |
| [columns](../harness/mechanics/messaging.py#L129) | table |  |
| [__init__](../harness/mechanics/messaging.py#L156) | self, state, company_id, provider, adapters, authorized, clock, spend, send_admission, channel_names, capability_spend |  |
| [_install](../harness/mechanics/messaging.py#L185) | self, adapter, replace | One adapter per channel, for this company, each with its own sender account. |
| [provider](../harness/mechanics/messaging.py#L200) | self | The WhatsApp adapter, the first built transport. |
| [provider](../harness/mechanics/messaging.py#L205) | self, value |  |
| [adapter](../harness/mechanics/messaging.py#L212) | self, channel |  |
| [channels](../harness/mechanics/messaging.py#L216) | self | Selected channels, each with its adapter and spending readiness. |
| [member_channels](../harness/mechanics/messaging.py#L234) | self, db, member | This member's verified addresses on the current sender accounts, by channel. |
| [eligible](../harness/mechanics/messaging.py#L246) | self, db, member | (channel, address generation) in channel order: verified, opted in, on a commissioned channel. |
| [_default_channel](../harness/mechanics/messaging.py#L253) | self, member | The channel a send uses when its caller names none: channel order, then the built transport. |
| [return_replies](../harness/mechanics/messaging.py#L261) | self, db, member, chat | Unadmitted replies of a member who left a Tracking Agent's participants continue their setup chat. |
| [_spend_open](../harness/mechanics/messaging.py#L273) | self, channel | The host's Stop and an unreadable spend record hold every provider-bound send of the company. |
| [host_actor](../harness/mechanics/messaging.py#L282) | self, member, collection, chat | The member themself in one conversation, for host work addressed to them. |
| [_auth](../harness/mechanics/messaging.py#L286) | self, actor, self_only |  |
| [_db](../harness/mechanics/messaging.py#L297) | self, write, before_commit |  |
| [connect](../harness/mechanics/messaging.py#L312) |  |  |
| [_ready](../harness/mechanics/messaging.py#L350) | self, kind, channel |  |
| [_account](../harness/mechanics/messaging.py#L358) | self, channel |  |
| [_contact](../harness/mechanics/messaging.py#L361) | self, db, member, channel |  |
| [_public_contact](../harness/mechanics/messaging.py#L370) | row |  |
| [_public_challenge](../harness/mechanics/messaging.py#L376) | row |  |
| [_public_outbox](../harness/mechanics/messaging.py#L382) | row |  |
| [describe](../harness/mechanics/messaging.py#L388) | self, actor |  |
| [_run](../harness/mechanics/messaging.py#L412) | self, operation, cancelled |  |
| [watch](../harness/mechanics/messaging.py#L415) |  |  |
| [_current](../harness/mechanics/messaging.py#L444) | self, actor, outbox_id, stop |  |
| [_settle](../harness/mechanics/messaging.py#L474) | self, identifier, status, provider_id |  |
| [_capability_admission](../harness/mechanics/messaging.py#L505) | self, actor, row, prepared, stop |  |
| [fence](../harness/mechanics/messaging.py#L511) |  |  |
| [_dispatch](../harness/mechanics/messaging.py#L522) | self, actor, row, prepared, stop, still |  |
| [current](../harness/mechanics/messaging.py#L524) |  |  |
| [send_prepared](../harness/mechanics/messaging.py#L560) | self, actor, row, prepared, still, cancelled | One provider request for a host delivery whose outbox row its claim already wrote. |
| [operation](../harness/mechanics/messaging.py#L568) | stop |  |
| [_replay](../harness/mechanics/messaging.py#L572) | self, db, actor, request_id, intent |  |
| [_insert](../harness/mechanics/messaging.py#L579) | self, db, actor, identifier, channel, address, kind, text, request_id, intent, generation |  |
| [request_code](../harness/mechanics/messaging.py#L590) | self, actor, phone, request_id, channel, cancelled | Send a security code over the channel it proves. `phone` is that channel's address. |
| [operation](../harness/mechanics/messaging.py#L601) | stop |  |
| [prepare](../harness/mechanics/messaging.py#L602) |  |  |
| [read](../harness/mechanics/messaging.py#L638) |  |  |
| [verify_code](../harness/mechanics/messaging.py#L647) | self, actor, challenge_id, code | Confirm a security code. The challenge carries its channel. |
| [revoke](../harness/mechanics/messaging.py#L691) | self, actor, channel | Explicit authenticated contact removal, for one channel or all; accepted sends still drain. |
| [bind_conversation](../harness/mechanics/messaging.py#L708) | self, actor, channel |  |
| [send_hello](../harness/mechanics/messaging.py#L719) | self, actor, request_id, channel, cancelled |  |
| [send_message](../harness/mechanics/messaging.py#L722) | self, actor, text, request_id, channel, cancelled |  |
| [send_alert](../harness/mechanics/messaging.py#L726) | self, actor, alert, request_id, channel, cancelled |  |
| [_send](../harness/mechanics/messaging.py#L734) | self, actor, kind, text, request_id, cancelled, channel |  |
| [operation](../harness/mechanics/messaging.py#L737) | stop |  |
| [prepare](../harness/mechanics/messaging.py#L738) |  |  |
| [_reply_target](../harness/mechanics/messaging.py#L801) | self, db, provider, contact, reply_to, now, reply_kind | Which conversation a reply continues, by the channel's own rule (CHANNELS.md). |
| [handle_webhook](../harness/mechanics/messaging.py#L832) | self, raw_body, signature, channel | Admit one signed provider request. `signature` is the header value or the request headers. |
| [_reply](../harness/mechanics/messaging.py#L941) | self, row |  |
| [_admissible](../harness/mechanics/messaging.py#L949) | self, db, row | A reply is admitted for a current member, on their current address, into a chat that takes them. |
| [pending_replies](../harness/mechanics/messaging.py#L957) | self, limit |  |
| [signal_reply_current](../harness/mechanics/messaging.py#L990) | self, event_id, signal | Recheck the exact verified provider event at each signal admission. |
| [unsettled_replies](../harness/mechanics/messaging.py#L1014) | self, limit | Receipts needing reconciliation only; they never authorize new work. |
| [claim_reply](../harness/mechanics/messaging.py#L1034) | self, event_id |  |
| [finish_reply](../harness/mechanics/messaging.py#L1045) | self, event_id, claim_id, admitted |  |
| [recover](../harness/mechanics/messaging.py#L1056) | self | Call after prior workers drain. Uncertain work is never replayed. |
| [close](../harness/mechanics/messaging.py#L1067) | self |  |

### harness/mechanics/messaging_composition.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [compose_messaging](../harness/mechanics/messaging_composition.py#L10) | capabilities, authorized, clock, spend, send_admission, capability_spend |  |
| [callback_response](../harness/mechanics/messaging_composition.py#L26) | channel | Use only after signature verification and durable ingress acknowledgement. |

### harness/mechanics/messaging_config.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_fail](../harness/mechanics/messaging_config.py#L32) |  |  |
| [_absolute_path](../harness/mechanics/messaging_config.py#L36) | value |  |
| [_read](../harness/mechanics/messaging_config.py#L45) | path |  |
| [_template](../harness/mechanics/messaging_config.py#L52) | value, category |  |
| [provider_for](../harness/mechanics/messaging_config.py#L65) | state, environment_id | Build the provider for the selected workspace, or leave other environments alone. |
| [credentials](../harness/mechanics/messaging_config.py#L106) |  |  |
| [spend_for](../harness/mechanics/messaging_config.py#L120) | state, environment_id | The reader of the host's spend record for participant phone chat. |
| [read](../harness/mechanics/messaging_config.py#L131) |  |  |

### harness/mechanics/messaging_provider.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [e164](../harness/mechanics/messaging_provider.py#L45) | value |  |
| [digest](../harness/mechanics/messaging_provider.py#L51) | value |  |
| [bounded](../harness/mechanics/messaging_provider.py#L55) | value, maximum |  |
| [__post_init__](../harness/mechanics/messaging_provider.py#L67) | self |  |
| [__post_init__](../harness/mechanics/messaging_provider.py#L82) | self |  |
| [__post_init__](../harness/mechanics/messaging_provider.py#L102) | self |  |
| [__new__](../harness/mechanics/messaging_provider.py#L127) | cls, identifier, message_id |  |
| [readiness](../harness/mechanics/messaging_provider.py#L169) | self |  |
| [otp_hash](../harness/mechanics/messaging_provider.py#L172) | self, challenge_id, code | Hash a security code under a secret only the host holds. |
| [address](../harness/mechanics/messaging_provider.py#L176) | self, value | Validate one recipient address for this channel; E.164 for sms and whatsapp. |
| [prepare](../harness/mechanics/messaging_provider.py#L180) | self, kind, address, text, code, alert, reference | kind is 'otp', 'hello', 'text' or 'utility'; `reference` is the outbox ID. |
| [prepare_reply](../harness/mechanics/messaging_provider.py#L184) | self, prepared, provider_message_id, message_id | Attach a previously admitted incoming message when the channel supports threads. |
| [preview](../harness/mechanics/messaging_provider.py#L188) | self, kind, text, alert | The text the member reads, saved with the outbox row. |
| [units](../harness/mechanics/messaging_provider.py#L192) | self, prepared | Billable units, read ahead of the send. |
| [send](../harness/mechanics/messaging_provider.py#L196) | self, prepared, current | One provider request. Calls `current` immediately before it leaves and sends only on True. |
| [verify](../harness/mechanics/messaging_provider.py#L200) | self, raw_body, headers | Raise ProviderError on an invalid signature, ahead of any parsing. |
| [events](../harness/mechanics/messaging_provider.py#L204) | self, raw_body |  |
| [__init__](../harness/mechanics/messaging_provider.py#L214) | self, config, credentials, transport |  |
| [company_id](../harness/mechanics/messaging_provider.py#L220) | self |  |
| [account_id](../harness/mechanics/messaging_provider.py#L224) | self |  |
| [commissioned](../harness/mechanics/messaging_provider.py#L228) | self |  |
| [credentials](../harness/mechanics/messaging_provider.py#L231) | self |  |
| [readiness](../harness/mechanics/messaging_provider.py#L240) | self |  |
| [otp_hash](../harness/mechanics/messaging_provider.py#L260) | self, challenge_id, code |  |
| [prepare](../harness/mechanics/messaging_provider.py#L267) | self, kind, address, text, code, alert, reference |  |
| [preview](../harness/mechanics/messaging_provider.py#L295) | self, kind, text, alert |  |
| [utility_message](../harness/mechanics/messaging_provider.py#L302) | self, alert |  |
| [send](../harness/mechanics/messaging_provider.py#L324) | self, prepared, current |  |
| [before](../harness/mechanics/messaging_provider.py#L329) | request |  |
| [verify_subscription](../harness/mechanics/messaging_provider.py#L365) | self, mode, token, challenge |  |
| [verify](../harness/mechanics/messaging_provider.py#L377) | self, raw_body, headers | Meta signs the raw body with the app secret; nothing is parsed before this passes. |
| [webhook](../harness/mechanics/messaging_provider.py#L390) | self, raw, signature | The Meta payload of one verified request: its messages and its statuses. |
| [events](../harness/mechanics/messaging_provider.py#L395) | self, raw_body | Meta's messages and statuses in the neutral shape. WhatsApp sends no opt-out or subscription here. |
| [_parse](../harness/mechanics/messaging_provider.py#L425) | self, raw |  |

### harness/mechanics/messaging_signals.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [reserve_send](../harness/mechanics/messaging_signals.py#L13) | store, actor, row | One stable outgoing effect unit in the same workspace-wide signal ledger. |
| [__init__](../harness/mechanics/messaging_signals.py#L24) | self, messaging, store, agent, member, answered |  |
| [current](../harness/mechanics/messaging_signals.py#L28) | self, signal |  |
| [_admitted](../harness/mechanics/messaging_signals.py#L32) | self, reply |  |
| [_queued](../harness/mechanics/messaging_signals.py#L37) | self, reply, owner, connection |  |
| [tick](../harness/mechanics/messaging_signals.py#L44) | self |  |
| [_finish](../harness/mechanics/messaging_signals.py#L87) | self, reply, admitted |  |

### harness/mechanics/native_custom_broker.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [drain](../harness/mechanics/native_custom_broker.py#L30) | task |  |
| [silent_command](../harness/mechanics/native_custom_broker.py#L36) | timeout, *argv | Untrusted container console is discarded; all retained output has quota. |
| [__init__](../harness/mechanics/native_custom_broker.py#L58) | self, broker, worker_path, backend |  |
| [live_count](../harness/mechanics/native_custom_broker.py#L72) | self |  |
| [_row](../harness/mechanics/native_custom_broker.py#L73) | self, key |  |
| [_status](../harness/mechanics/native_custom_broker.py#L74) | self, key, status, result |  |
| [_socket_dir](../harness/mechanics/native_custom_broker.py#L75) | self, key |  |
| [_lease](../harness/mechanics/native_custom_broker.py#L76) | self, row |  |
| [_validate](../harness/mechanics/native_custom_broker.py#L77) | self, scope, lease |  |
| [_public](../harness/mechanics/native_custom_broker.py#L82) | self, row |  |
| [prepare](../harness/mechanics/native_custom_broker.py#L84) | self, scope, request_id, document |  |
| [upload](../harness/mechanics/native_custom_broker.py#L103) | self, scope, lease, reader, writer |  |
| [_freeze_socket](../harness/mechanics/native_custom_broker.py#L139) | self, key |  |
| [start](../harness/mechanics/native_custom_broker.py#L148) | self, scope, lease, capability |  |
| [_run](../harness/mechanics/native_custom_broker.py#L164) | self, key |  |
| [_freeze_output](../harness/mechanics/native_custom_broker.py#L172) | self, key, request |  |
| [_finish](../harness/mechanics/native_custom_broker.py#L180) | self, key, succeeded |  |
| [stop](../harness/mechanics/native_custom_broker.py#L205) | self, scope, lease |  |
| [_discard](../harness/mechanics/native_custom_broker.py#L216) | self, key |  |
| [release](../harness/mechanics/native_custom_broker.py#L224) | self, scope, lease |  |
| [read](../harness/mechanics/native_custom_broker.py#L229) | self, scope, lease, writer |  |
| [reconcile](../harness/mechanics/native_custom_broker.py#L242) | self |  |
| [expire](../harness/mechanics/native_custom_broker.py#L252) | self |  |
| [handle](../harness/mechanics/native_custom_broker.py#L267) | self, operation, scope, request, reader, writer |  |
| [__init__](../harness/mechanics/native_custom_broker.py#L299) | self, root, script |  |
| [volume_key](../harness/mechanics/native_custom_broker.py#L303) | key |  |
| [name](../harness/mechanics/native_custom_broker.py#L305) | key |  |
| [volume_path](../harness/mechanics/native_custom_broker.py#L306) | self, key |  |
| [run](../harness/mechanics/native_custom_broker.py#L307) | self, key, root, sockets |  |
| [stop](../harness/mechanics/native_custom_broker.py#L316) | self, key |  |
| [present](../harness/mechanics/native_custom_broker.py#L317) |  |  |
| [unmount](../harness/mechanics/native_custom_broker.py#L320) | self, key |  |

### harness/mechanics/native_custom_client.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__post_init__](../harness/mechanics/native_custom_client.py#L19) | self |  |
| [request_for](../harness/mechanics/native_custom_client.py#L26) | snapshot, tool, arguments |  |
| [__init__](../harness/mechanics/native_custom_client.py#L33) | self, socket_path |  |
| [_connect](../harness/mechanics/native_custom_client.py#L34) | self, operation, scope, **values |  |
| [_request](../harness/mechanics/native_custom_client.py#L44) | self, operation, scope, **values |  |
| [capabilities](../harness/mechanics/native_custom_client.py#L47) | self, scope |  |
| [prepare](../harness/mechanics/native_custom_client.py#L48) | self, scope, request_id, snapshot, tool, arguments |  |
| [recover](../harness/mechanics/native_custom_client.py#L51) | self, scope, request_id, retire |  |
| [status](../harness/mechanics/native_custom_client.py#L54) | self, scope, lease |  |
| [stop](../harness/mechanics/native_custom_client.py#L55) | self, scope, lease |  |
| [release](../harness/mechanics/native_custom_client.py#L56) | self, scope, lease |  |
| [start](../harness/mechanics/native_custom_client.py#L57) | self, scope, lease, gateway_token |  |
| [upload](../harness/mechanics/native_custom_client.py#L58) | self, scope, lease, snapshot, tool, arguments |  |
| [result](../harness/mechanics/native_custom_client.py#L72) | self, scope, lease, snapshot, tool, arguments |  |

### harness/mechanics/organization_chats.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__getattr__](../harness/mechanics/organization_chats.py#L18) | name |  |
| [__init__](../harness/mechanics/organization_chats.py#L27) | self, state, environment_id, member, records |  |
| [_hash](../harness/mechanics/organization_chats.py#L40) | *parts |  |
| [_collection](../harness/mechanics/organization_chats.py#L44) | collection |  |
| [identity](../harness/mechanics/organization_chats.py#L49) | self, collection, purpose |  |
| [canonical](../harness/mechanics/organization_chats.py#L56) | self, record |  |
| [owns](../harness/mechanics/organization_chats.py#L67) | self, record |  |
| [can_read](../harness/mechanics/organization_chats.py#L91) | self, record, session |  |
| [ensure](../harness/mechanics/organization_chats.py#L110) | self, agent, collection, purpose |  |
| [setup_identity](../harness/mechanics/organization_chats.py#L126) | self, member, collection |  |
| [member_setup](../harness/mechanics/organization_chats.py#L132) | self, agent, member, collection |  |

### harness/mechanics/phone_chat.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [card_text](../harness/mechanics/phone_chat.py#L42) | status, title, name, channel | The chat entry of a contact card says what its state is. |
| [__init__](../harness/mechanics/phone_chat.py#L74) | self, message, status |  |
| [_identity](../harness/mechanics/phone_chat.py#L79) | value, maximum |  |
| [chat_admits](../harness/mechanics/phone_chat.py#L83) | db, chat, member | A participant-reach agent's chat takes messages from its current participants. |
| [resolve_member](../harness/mechanics/phone_chat.py#L98) | db, member, now, eligible | Resolve one member's bindings against their current verified addresses. |
| [__init__](../harness/mechanics/phone_chat.py#L136) | self, messaging, agents, member, post, clock |  |
| [_saved](../harness/mechanics/phone_chat.py#L144) | self, agent_id |  |
| [_member](../harness/mechanics/phone_chat.py#L156) | self, member_id |  |
| [_caller](../harness/mechanics/phone_chat.py#L163) | self, by |  |
| [_manager](../harness/mechanics/phone_chat.py#L167) | self, policy, by, company_owner |  |
| [_expected](../harness/mechanics/phone_chat.py#L173) | policy, expected_generation |  |
| [_ensure](../harness/mechanics/phone_chat.py#L180) | self, db, record, now | The default at promotion: policy on, the creator, their enabled binding, their card. |
| [_admit](../harness/mechanics/phone_chat.py#L195) | self, db, record, member, role, by, now, requested_by |  |
| [_request](../harness/mechanics/phone_chat.py#L209) | self, db, record, member, requested_by, now |  |
| [_expire](../harness/mechanics/phone_chat.py#L222) | db, now |  |
| [_revoke](../harness/mechanics/phone_chat.py#L225) | self, db, agent, member, now | End one participant's phone reach. Their unadmitted replies return to their own setup chat. |
| [_refresh](../harness/mechanics/phone_chat.py#L237) | self, db, record, now | Apply what changed outside this store: verified addresses, opt-outs and expiry. |
| [_bump](../harness/mechanics/phone_chat.py#L250) | db, agent, by, now |  |
| [_participant](../harness/mechanics/phone_chat.py#L254) | db, agent, member |  |
| [public_request](../harness/mechanics/phone_chat.py#L263) | row |  |
| [_snapshot](../harness/mechanics/phone_chat.py#L269) | self, db, record |  |
| [_result](../harness/mechanics/phone_chat.py#L296) | self, record |  |
| [state](../harness/mechanics/phone_chat.py#L304) | self, agent_id | Read one participant-reach agent's phone records, creating the default ones on first read. |
| [add_participant](../harness/mechanics/phone_chat.py#L315) | self, agent_id, member_id, by, company_owner, expected_generation |  |
| [remove_participant](../harness/mechanics/phone_chat.py#L338) | self, agent_id, member_id, by, company_owner, expected_generation |  |
| [update_binding](../harness/mechanics/phone_chat.py#L356) | self, agent_id, member_id, by, enabled, channel, expected_generation, company_owner |  |
| [set_delivery](../harness/mechanics/phone_chat.py#L400) | self, agent_id, state, by, company_owner, expected_generation |  |
| [request_contact](../harness/mechanics/phone_chat.py#L419) | self, agent_id, member_id, by, company_owner | Raise the contact card in the agent's chat, or return the open one. |
| [recipient](../harness/mechanics/phone_chat.py#L437) | self, agent_id, chat_id, member_id, channel, host | The gate's answer: the one member this participant-reach agent's turn may message. |
| [participant_chat](../harness/mechanics/phone_chat.py#L468) | self, chat_id, member_id | True when this chat is a participant-reach agent's and the member is one of its current participants. |
| [publish](../harness/mechanics/phone_chat.py#L480) | self, agent_id, member_id | Mirror each contact card's state into its chat entry, outside the store's transaction. |

### harness/mechanics/phone_delivery.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/mechanics/phone_delivery.py#L82) | self, reason |  |
| [delivery_id](../harness/mechanics/phone_delivery.py#L87) | company_id, agent_id, member_id, alert_id, alert_revision | The same ID after a retry, a restart, a duplicate outbox claim and a channel fallback. |
| [clean](../harness/mechanics/phone_delivery.py#L93) | value, limit | One line of plain text within its limit. |
| [alert_lead](../harness/mechanics/phone_delivery.py#L99) | title, revision | The agent's title; a later revision names the alert it updates. |
| [alert_text](../harness/mechanics/phone_delivery.py#L105) | title, summary, revision | The agent's title and the alert's summary in at most 600 characters. |
| [alert_link](../harness/mechanics/phone_delivery.py#L110) | origin, chat_id, alert_id | One link into Rocoto. It opens the alert after the member's ordinary sign-in and carries no token. |
| [mask](../harness/mechanics/phone_delivery.py#L117) | address | An E.164 number keeps its first four characters and last two digits; another address its last four. |
| [public](../harness/mechanics/phone_delivery.py#L126) | row |  |
| [_update](../harness/mechanics/phone_delivery.py#L139) | db, row, now, **changes |  |
| [settle](../harness/mechanics/phone_delivery.py#L147) | db, outbox, status, provider_id, now, returned | The provider's answer to one attempt sets the delivery's status. |
| [stopped](../harness/mechanics/phone_delivery.py#L179) | db, row | The agent's policy is paused, or this participant switched their alerts off or left. |
| [receipt](../harness/mechanics/phone_delivery.py#L188) | db, outbox, status, now | A provider receipt moves a delivery forward in the built order sent, failed, delivered, read. |
| [restart](../harness/mechanics/phone_delivery.py#L195) | db, now | A restart moves every dispatching delivery to uncertain; it is reconciled before any retry. |
| [cancel_queued](../harness/mechanics/phone_delivery.py#L203) | db, agent, now, member | Stop reaches the queued deliveries of one agent, or of one of its participants. |
| [window_lane](../harness/mechanics/phone_delivery.py#L212) | ingestion, event | The lane of the stream window that carried a committed tracker event. |
| [alert_lane](../harness/mechanics/phone_delivery.py#L237) | ingestion, event | The lane a committed tracker event arrived in: 'live', 'replay' or 'unknown'. |
| [__init__](../harness/mechanics/phone_delivery.py#L259) | self, messaging, phone, origin, post, concurrency |  |
| [lane](../harness/mechanics/phone_delivery.py#L266) | self, alert_id, decide | The lane of one observation, decided once and kept: 'live', 'replay' or 'unknown'. |
| [_prune](../harness/mechanics/phone_delivery.py#L299) | db, now | Remove what retention has released: deliveries, their outbox rows, then receipts and lanes. |
| [prune](../harness/mechanics/phone_delivery.py#L315) | self, force | One retention pass, at most once a minute. Returns the deliveries removed. |
| [history_full](../harness/mechanics/phone_delivery.py#L331) | self | True while retained history is at its bound, so a new alert writes nothing. |
| [unread](../harness/mechanics/phone_delivery.py#L340) | self, agent_id, alert_ids, alert_revision | The alerts of this list that hold no fan-out receipt and no kept replay lane, for the catch-up pass. |
| [fan_out](../harness/mechanics/phone_delivery.py#L357) | self, agent_id, alert_id, summary, alert_revision, lane, committed_at, since | Write one delivery per participant whose binding is enabled, and return the ones written. |
| [full](../harness/mechanics/phone_delivery.py#L390) |  |  |
| [_entry](../harness/mechanics/phone_delivery.py#L427) | self, db, alert |  |
| [sync_entries](../harness/mechanics/phone_delivery.py#L436) | self, limit | Append each alert to its chat in arrival order, then keep its delivery states current. |
| [_current](../harness/mechanics/phone_delivery.py#L468) | self, db, row, now | The agent is a Tracking Agent with its policy on; the member is a current participant with alerts on. |
| [_prepare](../harness/mechanics/phone_delivery.py#L484) | self, provider, contact, alert, row, reference, now | The provider request for one channel, or the reason this channel holds the alert. |
| [_claim](../harness/mechanics/phone_delivery.py#L512) | self, identifier | Repeat the admission checks, reserve the units and mark one queued delivery dispatching. |
| [close](../harness/mechanics/phone_delivery.py#L520) | status, reason |  |
| [_still](../harness/mechanics/phone_delivery.py#L577) | self, identifier, outbox_id | The admission checks again, immediately before the provider call. |
| [_deliver](../harness/mechanics/phone_delivery.py#L591) | self, identifier |  |
| [_sweep](../harness/mechanics/phone_delivery.py#L605) | self, limit | Expire what stayed unsent for 900 seconds and list the queued deliveries, oldest first. |
| [tick](../harness/mechanics/phone_delivery.py#L629) | self, limit | One pass of the worker: expire, claim and dispatch, then bring the chat entries up to date. |
| [drain](../harness/mechanics/phone_delivery.py#L645) | self | Wait for the sends in flight, then record their states in the chat entries. |
| [close](../harness/mechanics/phone_delivery.py#L652) | self | Stop the sends still in flight. A finished send needs nothing more. |
| [reconcile](../harness/mechanics/phone_delivery.py#L663) | self, identifier, outcome, reviewed_by | Record the host's review of an uncertain send. It is reconciled before any retry. |
| [deliveries](../harness/mechanics/phone_delivery.py#L691) | self, agent_id, alert_id |  |
| [answered](../harness/mechanics/phone_delivery.py#L702) | self, reply | The alert a participant's phone reply answers, as host-supplied context for the turn it starts. |
| [block](../harness/mechanics/phone_delivery.py#L726) | self, agent_id, reader, company_owner, writable, members, admitted | The phone block of CHANNELS.md for one reader: a current participant or the company owner. |
| [main](../harness/mechanics/phone_delivery.py#L775) | argv | The host operator's entry point for an uncertain send. |

### harness/mechanics/phone_routes.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [register_phone_routes](../harness/mechanics/phone_routes.py#L21) | app, member, members | `member(selected, principal)` answers a current owner or operator; `members(selected)` lists them. |
| [reader](../harness/mechanics/phone_routes.py#L24) | request, agent_id | The caller as a current company member, and this Tracking Agent's chat within their scope. |
| [covered](../harness/mechanics/phone_routes.py#L39) |  |  |
| [block](../harness/mechanics/phone_routes.py#L48) | request, selected, agent_id, principal, owner, admitted |  |
| [body](../harness/mechanics/phone_routes.py#L59) | request, shape, required | A JSON object of the named fields, each of its declared type, in at most 8192 bytes. |
| [change](../harness/mechanics/phone_routes.py#L77) | request, agent_id, shape, required, operation | Authorize the caller, apply one change as that caller and answer with the fresh block. |
| [phone_block](../harness/mechanics/phone_routes.py#L95) | agent_id, request |  |
| [phone_add](../harness/mechanics/phone_routes.py#L100) | agent_id, request |  |
| [phone_remove](../harness/mechanics/phone_routes.py#L106) | agent_id, member_id, request |  |
| [phone_participant](../harness/mechanics/phone_routes.py#L112) | agent_id, member_id, request |  |
| [phone_delivery_state](../harness/mechanics/phone_routes.py#L119) | agent_id, request |  |
| [phone_contact_request](../harness/mechanics/phone_routes.py#L125) | agent_id, request |  |

### harness/mechanics/phone_spend.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/mechanics/phone_spend.py#L41) | self, reason |  |
| [record](../harness/mechanics/phone_spend.py#L46) | reader | The host's spend record, validated. Anything else is unreadable. |
| [admit](../harness/mechanics/phone_spend.py#L58) | reader | The host's answer ahead of any provider-bound phone send of the company. |
| [day](../harness/mechanics/phone_spend.py#L71) | now |  |
| [resets_at](../harness/mechanics/phone_spend.py#L75) | now | The next UTC midnight. |
| [_used](../harness/mechanics/phone_spend.py#L81) | db, today, scope |  |
| [reserve](../harness/mechanics/phone_spend.py#L92) | db, reader, agent, units, now, outbox | Add one message's units to the agent's and the company's counters for the current UTC day. |
| [release](../harness/mechanics/phone_spend.py#L113) | db, outbox | Return the units of a send that provably stayed inside Rocoto. Sent, failed and uncertain keep theirs. |
| [usage](../harness/mechanics/phone_spend.py#L124) | db, reader, agent, now | The phone block's spend object: units used today against each cap, and the state they give. |

### harness/mechanics/private_records.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [read_private](../harness/mechanics/private_records.py#L11) | path, code_root |  |

### harness/mechanics/profile_activity.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [reader](../harness/mechanics/profile_activity.py#L25) | path |  |
| [_agent_pool_path](../harness/mechanics/profile_activity.py#L37) | state |  |
| [bind_model_run](../harness/mechanics/profile_activity.py#L42) | state, run_id, owner | Host-only forward attribution before dispatch; the model supplies neither ID. |
| [_attribution](../harness/mechanics/profile_activity.py#L82) | state, owner |  |
| [stamp](../harness/mechanics/profile_activity.py#L97) | value | Known persisted seconds or explicitly zoned ISO timestamps, normalized UTC. |
| [access_scope](../harness/mechanics/profile_activity.py#L110) | access_path, session, scope | Fresh membership for the selected host company, including owner observation. |
| [member](../harness/mechanics/profile_activity.py#L123) | principal |  |
| [_json](../harness/mechanics/profile_activity.py#L140) | value |  |
| [_sum](../harness/mechanics/profile_activity.py#L147) | rows |  |
| [activity](../harness/mechanics/profile_activity.py#L153) | state, scope, principal_id, identity, organisation_allowed, chats, days, now |  |
| [owned](../harness/mechanics/profile_activity.py#L172) | row |  |
| [day](../harness/mechanics/profile_activity.py#L175) | value |  |

### harness/mechanics/profile_cover_generation.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [canonical](../harness/mechanics/profile_cover_generation.py#L44) | value |  |
| [digest](../harness/mechanics/profile_cover_generation.py#L45) | value |  |
| [brief](../harness/mechanics/profile_cover_generation.py#L48) | profile, member, target, direction |  |
| [__init__](../harness/mechanics/profile_cover_generation.py#L67) | self, state, api_key, pool, transport |  |
| [connect](../harness/mechanics/profile_cover_generation.py#L82) | self |  |
| [_review](../harness/mechanics/profile_cover_generation.py#L85) | self, value |  |
| [_emit](../harness/mechanics/profile_cover_generation.py#L89) | self, emit, event |  |
| [_discard_file](../harness/mechanics/profile_cover_generation.py#L95) | files, publication_key, file_id, scope |  |
| [generate](../harness/mechanics/profile_cover_generation.py#L104) | self, scope, store, files, business, member, target, expected_profile_revision, direction, current, emit |  |
| [check](../harness/mechanics/profile_cover_generation.py#L108) |  |  |
| [prepare](../harness/mechanics/profile_cover_generation.py#L113) |  |  |
| [admit](../harness/mechanics/profile_cover_generation.py#L145) |  |  |
| [start](../harness/mechanics/profile_cover_generation.py#L164) |  |  |
| [receive](../harness/mechanics/profile_cover_generation.py#L181) |  |  |
| [publish](../harness/mechanics/profile_cover_generation.py#L212) |  |  |
| [cleanup](../harness/mechanics/profile_cover_generation.py#L233) |  |  |

### harness/mechanics/profile_cover_host.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [tool_specs](../harness/mechanics/profile_cover_host.py#L15) |  |  |
| [__init__](../harness/mechanics/profile_cover_host.py#L19) | self, selected, access, transport |  |
| [member](../harness/mechanics/profile_cover_host.py#L24) | self, actor_id |  |
| [authorize](../harness/mechanics/profile_cover_host.py#L34) | self, actor_id, target, target_id, collection, write |  |
| [business](../harness/mechanics/profile_cover_host.py#L42) | self, actor_id, collection, data |  |
| [members](../harness/mechanics/profile_cover_host.py#L49) | self, actor_id, collection, rows |  |
| [tool](../harness/mechanics/profile_cover_host.py#L57) | self, name, args, owner, actor_id, chat_id, collection, turn_id, current, emit |  |
| [guard](../harness/mechanics/profile_cover_host.py#L63) |  |  |
| [install_profile_covers](../harness/mechanics/profile_cover_host.py#L94) | selected, access, transport |  |
| [register_routes](../harness/mechanics/profile_cover_host.py#L101) | app |  |
| [context](../harness/mechanics/profile_cover_host.py#L102) | request, cover_id |  |

### harness/mechanics/profile_cover_routes.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [register_profile_cover_routes](../harness/mechanics/profile_cover_routes.py#L13) | app, context_for_request | context_for_request(request, cover_id) -> (store, actor_id, collection). |
| [cover](../harness/mechanics/profile_cover_routes.py#L22) | cover_id, request |  |

### harness/mechanics/profile_covers.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [image_bytes](../harness/mechanics/profile_covers.py#L40) | raw | Decode bounded raster bytes, orient them, and strip embedded metadata. |
| [__init__](../harness/mechanics/profile_covers.py#L75) | self, state, authorize |  |
| [connect](../harness/mechanics/profile_covers.py#L93) | self |  |
| [_access](../harness/mechanics/profile_covers.py#L98) | self, actor_id, target, target_id, collection, write |  |
| [metadata](../harness/mechanics/profile_covers.py#L110) | row |  |
| [publish](../harness/mechanics/profile_covers.py#L117) | self, files, business, file_id, target, owner, actor_id, chat_id, collection, current, created, expected_profile_revision |  |
| [get](../harness/mechanics/profile_covers.py#L175) | self, actor_id, target, target_id, collection |  |
| [download](../harness/mechanics/profile_covers.py#L182) | self, cover_id, actor_id, collection |  |
| [discard](../harness/mechanics/profile_covers.py#L195) | self, ids, owner, chat_id, collection | Host cleanup for newly published artifacts in an interrupted turn. |

### harness/mechanics/profile_image_usage.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [measured_usage](../harness/mechanics/profile_image_usage.py#L24) | value |  |
| [actual_cost](../harness/mechanics/profile_image_usage.py#L37) | usage |  |
| [bind](../harness/mechanics/profile_image_usage.py#L43) | pool, reservation_id, request_id |  |
| [settle](../harness/mechanics/profile_image_usage.py#L47) | pool, reservation_id, receipt_path |  |

### harness/mechanics/provider_configuration.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [commissioned_writes_for](../harness/mechanics/provider_configuration.py#L15) | requested, registered_clients, remote_providers | Apply a host's write selection to this company's available provider policies. |
| [_company_configuration](../harness/mechanics/provider_configuration.py#L32) | state, public_origin, environment, loader |  |
| [registered_clients_for](../harness/mechanics/provider_configuration.py#L61) | state, public_origin |  |
| [remote_providers_for](../harness/mechanics/provider_configuration.py#L67) | state, public_origin |  |

### harness/mechanics/provider_credentials.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [private_file](../harness/mechanics/provider_credentials.py#L42) | fd |  |
| [directory](../harness/mechanics/provider_credentials.py#L49) | state |  |
| [locked](../harness/mechanics/provider_credentials.py#L61) | root, exclusive |  |
| [__init__](../harness/mechanics/provider_credentials.py#L70) | self, root, company |  |
| [key](../harness/mechanics/provider_credentials.py#L71) | self, create |  |
| [binding](../harness/mechanics/provider_credentials.py#L90) | self, principal, provider, generation, field |  |
| [seal](../harness/mechanics/provider_credentials.py#L94) | self, value, principal, provider, generation, field |  |
| [open](../harness/mechanics/provider_credentials.py#L102) | self, value, principal, provider, generation, field |  |
| [_bounded_database](../harness/mechanics/provider_credentials.py#L114) | path, legacy |  |
| [configure_database](../harness/mechanics/provider_credentials.py#L129) | db | SQLite's pager limit belongs to this connection, not to the DB file. |
| [_tables](../harness/mechanics/provider_credentials.py#L139) | db |  |
| [_format](../harness/mechanics/provider_credentials.py#L142) | db, company |  |
| [initialize](../harness/mechanics/provider_credentials.py#L153) | root, company | Fast fresh initialization; historical migration is an explicit host operation. |
| [migrate_connections](../harness/mechanics/provider_credentials.py#L173) | state | Explicit, synchronous migration; stop all old/new users of this DB first. |

### harness/mechanics/provider_outputs.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [canonical](../harness/mechanics/provider_outputs.py#L18) | value |  |
| [digest](../harness/mechanics/provider_outputs.py#L19) | value |  |
| [label](../harness/mechanics/provider_outputs.py#L21) | value, fallback, limit |  |
| [external_url](../harness/mechanics/provider_outputs.py#L27) | value | Only navigable public HTTPS links; no host/network resolution is performed. |
| [_google_created_file](../harness/mechanics/provider_outputs.py#L43) | result | Drive create_file's documented File result, not arbitrary JSON URLs. |
| [resources](../harness/mechanics/provider_outputs.py#L66) | result, provider, tool | Standard MCP blocks plus the reviewed, host-bound Drive create_file shape. |
| [__init__](../harness/mechanics/provider_outputs.py#L111) | self, files, relay, owner, root_chat_id, dataset, company_id, current |  |
| [event](../harness/mechanics/provider_outputs.py#L116) | self, method, params, actor_chat_id |  |
| [guard](../harness/mechanics/provider_outputs.py#L149) |  |  |

### harness/mechanics/provider_policy.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [selected_scopes](../harness/mechanics/provider_policy.py#L98) | config, mode |  |
| [scopes](../harness/mechanics/provider_policy.py#L103) | value |  |
| [provider_read_only](../harness/mechanics/provider_policy.py#L112) | config, row |  |
| [read_authorized](../harness/mechanics/provider_policy.py#L117) | config, row, name |  |
| [visible_tools](../harness/mechanics/provider_policy.py#L121) | config, row, inventory |  |
| [digest](../harness/mechanics/provider_policy.py#L126) | value |  |
| [effective_policies](../harness/mechanics/provider_policy.py#L130) | remote_providers | Host configuration projection shared by broker and deployment filtering. |

### harness/mechanics/public_mcp.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__getattr__](../harness/mechanics/public_mcp.py#L38) | name |  |
| [registry](../harness/mechanics/public_mcp.py#L51) | self |  |
| [admit](../harness/mechanics/public_mcp.py#L55) | self, grant |  |
| [_public](../harness/mechanics/public_mcp.py#L66) | value, depth |  |
| [__init__](../harness/mechanics/public_mcp.py#L80) | self, services |  |
| [call](../harness/mechanics/public_mcp.py#L83) | self, grant, name, args, scope_guards |  |
| [invoke](../harness/mechanics/public_mcp.py#L88) |  |  |
| [__init__](../harness/mechanics/public_mcp.py#L111) | self, store, resolve_scope, resource_url, call_timeout, recheck_seconds, max_sessions, max_calls, max_calls_per_key, idle_timeout, resource_path, permission |  |
| [listing](../harness/mechanics/public_mcp.py#L132) |  |  |
| [call](../harness/mechanics/public_mcp.py#L136) | name, arguments |  |
| [_resolve](../harness/mechanics/public_mcp.py#L143) | self, grant |  |
| [_authorization](../harness/mechanics/public_mcp.py#L156) | self, lookup, value |  |
| [resolve](../harness/mechanics/public_mcp.py#L160) |  |  |
| [finished](../harness/mechanics/public_mcp.py#L167) | task |  |
| [verify_token](../harness/mechanics/public_mcp.py#L176) | self, token |  |
| [_current](../harness/mechanics/public_mcp.py#L187) | self, key |  |
| [_request_scope](../harness/mechanics/public_mcp.py#L190) | self |  |
| [error](../harness/mechanics/public_mcp.py#L196) |  |  |
| [_call](../harness/mechanics/public_mcp.py#L198) | self, name, args |  |
| [changed](../harness/mechanics/public_mcp.py#L212) |  |  |
| [drain](../harness/mechanics/public_mcp.py#L223) |  |  |
| [_read](../harness/mechanics/public_mcp.py#L239) | self, grant, services, name, args |  |
| [_endpoint](../harness/mechanics/public_mcp.py#L250) | self, scope, receive, send |  |
| [replay](../harness/mechanics/public_mcp.py#L280) |  |  |
| [scope_current](../harness/mechanics/public_mcp.py#L290) |  |  |
| [binding_current](../harness/mechanics/public_mcp.py#L294) |  |  |
| [guarded](../harness/mechanics/public_mcp.py#L299) | message |  |
| [__call__](../harness/mechanics/public_mcp.py#L320) | self, scope, receive, send |  |
| [lifespan](../harness/mechanics/public_mcp.py#L328) | self |  |

### harness/mechanics/public_urls.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [require](../harness/mechanics/public_urls.py#L9) | value |  |
| [validate_url](../harness/mechanics/public_urls.py#L12) | value |  |

### harness/mechanics/recipe_runs.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [specs](../harness/mechanics/recipe_runs.py#L20) | write |  |
| [__init__](../harness/mechanics/recipe_runs.py#L43) | self, state |  |
| [connect](../harness/mechanics/recipe_runs.py#L57) | self |  |
| [scope](../harness/mechanics/recipe_runs.py#L63) | context |  |
| [_get](../harness/mechanics/recipe_runs.py#L69) | self, db, context, run_id |  |
| [get](../harness/mechanics/recipe_runs.py#L76) | self, context, run_id |  |
| [list](../harness/mechanics/recipe_runs.py#L80) | self, context |  |
| [begin](../harness/mechanics/recipe_runs.py#L86) | self, context, recipe |  |
| [update](../harness/mechanics/recipe_runs.py#L107) | self, context, run_id, expected_revision, step_id, status, note, evidence |  |
| [_store](../harness/mechanics/recipe_runs.py#L133) | context |  |
| [read](../harness/mechanics/recipe_runs.py#L138) | context, name, arguments |  |
| [call](../harness/mechanics/recipe_runs.py#L149) | context, name, arguments |  |

### harness/mechanics/registered_oauth.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_fail](../harness/mechanics/registered_oauth.py#L33) |  |  |
| [_object](../harness/mechanics/registered_oauth.py#L37) | pairs |  |
| [_callback](../harness/mechanics/registered_oauth.py#L45) | origin |  |
| [read_private_configuration](../harness/mechanics/registered_oauth.py#L55) | path, max_bytes |  |
| [__post_init__](../harness/mechanics/registered_oauth.py#L93) | self |  |
| [fingerprint](../harness/mechanics/registered_oauth.py#L112) | self |  |
| [policy_fingerprint](../harness/mechanics/registered_oauth.py#L118) | self |  |
| [client_info](../harness/mechanics/registered_oauth.py#L125) | self, requested_scopes |  |
| [__post_init__](../harness/mechanics/registered_oauth.py#L139) | self |  |
| [get](../harness/mechanics/registered_oauth.py#L148) | self, provider |  |
| [load](../harness/mechanics/registered_oauth.py#L152) | cls, path, company_scope, public_origin | Read one bounded private file; token/grant fields are rejected. |

### harness/mechanics/scope_host.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [current_admission](../harness/mechanics/scope_host.py#L13) |  |  |
| [bind_admission](../harness/mechanics/scope_host.py#L17) | admission |  |
| [setup_scope](../harness/mechanics/scope_host.py#L26) | selected, member, members |  |
| [scope_current](../harness/mechanics/scope_host.py#L37) | value |  |
| [conversation_root](../harness/mechanics/scope_host.py#L43) | agent, record | Resolve saved descendants through a bounded, same-owner ancestry chain. |
| [history_allowed](../harness/mechanics/scope_host.py#L72) | selected, record, principal |  |
| [turn_actor](../harness/mechanics/scope_host.py#L83) | agent, chat_id, sender |  |
| [_conversation_authority](../harness/mechanics/scope_host.py#L93) | agent, chat_id, dataset, sender |  |
| [current](../harness/mechanics/scope_host.py#L117) |  |  |
| [agent_scope](../harness/mechanics/scope_host.py#L140) | agent, chat_id, dataset, sender, admit |  |
| [empty](../harness/mechanics/scope_host.py#L153) |  |  |
| [active_scope_current](../harness/mechanics/scope_host.py#L177) | agent, chat_id |  |
| [filter_view](../harness/mechanics/scope_host.py#L188) | selected, view, principal, collection, chat_id, observer |  |
| [_owned_views](../harness/mechanics/scope_host.py#L194) | selected, principal, collection |  |
| [history_within_view](../harness/mechanics/scope_host.py#L199) | selected, record, view |  |

### harness/mechanics/signal_chain.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [bounded](../harness/mechanics/signal_chain.py#L35) | value |  |
| [__init__](../harness/mechanics/signal_chain.py#L47) | self, store |  |
| [recover](../harness/mechanics/signal_chain.py#L64) | self, db |  |
| [reserve](../harness/mechanics/signal_chain.py#L74) | self, db, kind, reservation, target, amount, target_limit, now |  |
| [release_unstarted](../harness/mechanics/signal_chain.py#L93) | self, db, reservation |  |
| [usage](../harness/mechanics/signal_chain.py#L96) | self, now |  |
| [validate_payload](../harness/mechanics/signal_chain.py#L104) | payload |  |
| [validate_chain](../harness/mechanics/signal_chain.py#L110) | chain |  |
| [register](../harness/mechanics/signal_chain.py#L141) | self, name, handler, kind, timeout_seconds, cleanup_seconds, cancel, reconcile, metered, config_schema, description | Install a host adapter, including its cleanup and reconciliation contract. |
| [declarations](../harness/mechanics/signal_chain.py#L167) | self |  |
| [reviewed_chain](../harness/mechanics/signal_chain.py#L172) | self, chain | Person-facing chain selection uses explicit host declarations only. |
| [register_producer](../harness/mechanics/signal_chain.py#L183) | self, name, authorized |  |
| [_rules](../harness/mechanics/signal_chain.py#L189) | step, payload |  |
| [matches](../harness/mechanics/signal_chain.py#L190) | clause |  |
| [producer_current](../harness/mechanics/signal_chain.py#L204) | self, record |  |
| [_current](../harness/mechanics/signal_chain.py#L211) | self, record |  |
| [_context](../harness/mechanics/signal_chain.py#L225) | self, record, receipt, cancelled |  |
| [external](../harness/mechanics/signal_chain.py#L226) | identity |  |
| [_output](../harness/mechanics/signal_chain.py#L249) | output, payload |  |
| [_invoke](../harness/mechanics/signal_chain.py#L261) | self, registered, payload, config, context, receipt |  |
| [cleanup](../harness/mechanics/signal_chain.py#L277) |  |  |
| [process](../harness/mechanics/signal_chain.py#L295) | self, signal | Advance one saved chain; immutable ingress remains its authority evidence. |
| [_chain_status](../harness/mechanics/signal_chain.py#L359) | self, record, receipt |  |
| [reconcile](../harness/mechanics/signal_chain.py#L367) | self, signal_id, owner |  |
| [_save_step](../harness/mechanics/signal_chain.py#L386) | self, receipt |  |
| [receipts](../harness/mechanics/signal_chain.py#L392) | self, signal_id, owner |  |

### harness/mechanics/signal_dispatcher.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/mechanics/signal_dispatcher.py#L10) | self, store, agent, scheduler, slots, sources |  |
| [tick](../harness/mechanics/signal_dispatcher.py#L14) | self |  |
| [_finished](../harness/mechanics/signal_dispatcher.py#L48) | self, task |  |
| [_execute](../harness/mechanics/signal_dispatcher.py#L52) | self, signal |  |
| [recover_pending](../harness/mechanics/signal_dispatcher.py#L85) | self |  |
| [close](../harness/mechanics/signal_dispatcher.py#L126) | self |  |

### harness/mechanics/signal_endpoints.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [target_url](../harness/mechanics/signal_endpoints.py#L20) | value |  |
| [canonical](../harness/mechanics/signal_endpoints.py#L41) | value |  |
| [digest](../harness/mechanics/signal_endpoints.py#L42) | value |  |
| [__init__](../harness/mechanics/signal_endpoints.py#L46) | self, store, authorized, owner_authorized, resolver, network_backend, ssl_context |  |
| [public](../harness/mechanics/signal_endpoints.py#L63) | record |  |
| [_write](../harness/mechanics/signal_endpoints.py#L68) | db, record |  |
| [get](../harness/mechanics/signal_endpoints.py#L72) | self, key |  |
| [current](../harness/mechanics/signal_endpoints.py#L77) | self, record |  |
| [register](../harness/mechanics/signal_endpoints.py#L81) | self, context, label, url, daily_sends |  |
| [list](../harness/mechanics/signal_endpoints.py#L103) | self, actor, chat_id |  |
| [reveal](../harness/mechanics/signal_endpoints.py#L107) | self, key, actor, chat_id |  |
| [revoke](../harness/mechanics/signal_endpoints.py#L117) | self, key, actor, chat_id |  |
| [_producer_current](../harness/mechanics/signal_endpoints.py#L126) | self, signal |  |
| [send](../harness/mechanics/signal_endpoints.py#L135) | self, context, endpoint_id, event, payload, call_identity |  |
| [_send](../harness/mechanics/signal_endpoints.py#L167) | self, payload, config, context |  |
| [current](../harness/mechanics/signal_endpoints.py#L177) |  |  |

### harness/mechanics/signal_screening.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [canonical](../harness/mechanics/signal_screening.py#L38) | value |  |
| [private_json](../harness/mechanics/signal_screening.py#L40) | path, value |  |
| [__init__](../harness/mechanics/signal_screening.py#L50) | self, store, pool, api_key, transport, clock |  |
| [_prerequisites](../harness/mechanics/signal_screening.py#L65) | self |  |
| [request](../harness/mechanics/signal_screening.py#L84) | payload, config |  |
| [run](../harness/mechanics/signal_screening.py#L101) | self, payload, config, context |  |
| [_finish](../harness/mechanics/signal_screening.py#L140) | self, admission |  |
| [reconcile](../harness/mechanics/signal_screening.py#L169) | self, context |  |

### harness/mechanics/signal_sources.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/mechanics/signal_sources.py#L15) | self, store, public_origin, environment |  |
| [_write](../harness/mechanics/signal_sources.py#L25) | db, record |  |
| [_get](../harness/mechanics/signal_sources.py#L30) | db, key |  |
| [get](../harness/mechanics/signal_sources.py#L35) | self, key |  |
| [current](../harness/mechanics/signal_sources.py#L38) | self, record, now |  |
| [_create](../harness/mechanics/signal_sources.py#L46) | self, kind, owner, actor, chat_id, collection, label, chain, authority_until, now, **fields |  |
| [create_hook](../harness/mechanics/signal_sources.py#L64) | self, days, signature, authority_until, **identity |  |
| [set_timer](../harness/mechanics/signal_sources.py#L71) | self, note, delay_seconds, every_seconds, fires, authority_until, **identity |  |
| [public](../harness/mechanics/signal_sources.py#L83) | self, record |  |
| [list](../harness/mechanics/signal_sources.py#L91) | self, actor, chat_id, collection |  |
| [reveal](../harness/mechanics/signal_sources.py#L97) | self, key, actor, chat_id |  |
| [cancel](../harness/mechanics/signal_sources.py#L106) | self, key, actor, chat_id |  |
| [_deliver](../harness/mechanics/signal_sources.py#L116) | self, record, event_id, text, payload, now |  |
| [receive](../harness/mechanics/signal_sources.py#L128) | self, key, raw, signature, event_id, now |  |
| [tick](../harness/mechanics/signal_sources.py#L159) | self, now |  |

### harness/mechanics/skills.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__getattr__](../harness/mechanics/skills.py#L32) | name |  |
| [_json](../harness/mechanics/skills.py#L40) | value |  |
| [_hash](../harness/mechanics/skills.py#L44) | value |  |
| [_text](../harness/mechanics/skills.py#L48) | value, maximum |  |
| [_names](../harness/mechanics/skills.py#L55) | value, pattern, maximum |  |
| [_connections](../harness/mechanics/skills.py#L63) | value |  |
| [_definition](../harness/mechanics/skills.py#L80) | body, previous |  |
| [_revision](../harness/mechanics/skills.py#L94) | value |  |
| [_seeds](../harness/mechanics/skills.py#L99) | template | A template's skill seeds as this store saves them: (id, definition), each through `_definition`. |
| [__init__](../harness/mechanics/skills.py#L118) | self, state |  |
| [connect](../harness/mechanics/skills.py#L159) | self |  |
| [_append](../harness/mechanics/skills.py#L166) | db, skill_id, revision, fields, origin, publisher |  |
| [_read](../harness/mechanics/skills.py#L174) | row |  |
| [_current](../harness/mechanics/skills.py#L186) | self, db, skill_id |  |
| [_installed](../harness/mechanics/skills.py#L193) | db, skill_id |  |
| [_decorate](../harness/mechanics/skills.py#L197) | self, db, record |  |
| [catalogue](../harness/mechanics/skills.py#L206) | self |  |
| [list](../harness/mechanics/skills.py#L213) | self |  |
| [install](../harness/mechanics/skills.py#L221) | self, skill_id, expected_revision |  |
| [create](../harness/mechanics/skills.py#L235) | self, body, origin |  |
| [update](../harness/mechanics/skills.py#L244) | self, skill_id, expected_revision, body, origin |  |
| [history](../harness/mechanics/skills.py#L259) | self, skill_id |  |
| [resolve](../harness/mechanics/skills.py#L266) | self, ids, capabilities, available_tools, max_count | Snapshot installed instructions using capabilities supplied by trusted host code. |

### harness/mechanics/source_icons.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [normalized_host](../harness/mechanics/source_icons.py#L22) | host |  |
| [raster_icon](../harness/mechanics/source_icons.py#L29) | body |  |
| [__init__](../harness/mechanics/source_icons.py#L43) | self, resolver, network_backend, ssl_context, clock |  |
| [get](../harness/mechanics/source_icons.py#L51) | self, host |  |
| [_fetch](../harness/mechanics/source_icons.py#L76) | self, url |  |

### harness/mechanics/source_media.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_require](../harness/mechanics/source_media.py#L62) | condition, code |  |
| [_identifier](../harness/mechanics/source_media.py#L67) | value, pattern |  |
| [_number](../harness/mechanics/source_media.py#L71) | value |  |
| [_json](../harness/mechanics/source_media.py#L75) | value |  |
| [__post_init__](../harness/mechanics/source_media.py#L86) | self |  |
| [key](../harness/mechanics/source_media.py#L94) | self |  |
| [__post_init__](../harness/mechanics/source_media.py#L104) | self |  |
| [__post_init__](../harness/mechanics/source_media.py#L118) | self |  |
| [parse](../harness/mechanics/source_media.py#L134) | cls, value |  |
| [manifest_request](../harness/mechanics/source_media.py#L139) | self, scope, collection, checksum |  |
| [wall_seconds](../harness/mechanics/source_media.py#L157) | self |  |
| [image](../harness/mechanics/source_media.py#L161) | self |  |
| [arguments](../harness/mechanics/source_media.py#L165) | self |  |
| [name](../harness/mechanics/source_media.py#L175) | self |  |
| [original](../harness/mechanics/source_media.py#L179) | self |  |
| [output](../harness/mechanics/source_media.py#L183) | self |  |
| [__init__](../harness/mechanics/source_media.py#L189) | self, root |  |
| [volume_path](../harness/mechanics/source_media.py#L195) | self, key, generation |  |
| [mount](../harness/mechanics/source_media.py#L198) | self, spec |  |
| [flags](../harness/mechanics/source_media.py#L202) | self, spec |  |
| [start](../harness/mechanics/source_media.py#L213) | self, spec |  |
| [wait](../harness/mechanics/source_media.py#L230) | self, spec |  |
| [stop](../harness/mechanics/source_media.py#L235) | self, spec |  |
| [present](../harness/mechanics/source_media.py#L236) |  |  |
| [unmount](../harness/mechanics/source_media.py#L244) | self, spec |  |
| [_directory](../harness/mechanics/source_media.py#L250) | path |  |
| [_identity](../harness/mechanics/source_media.py#L260) | info |  |
| [_copy_original](../harness/mechanics/source_media.py#L264) | fd, destination, uid, size, checksum |  |
| [_read_json](../harness/mechanics/source_media.py#L283) | path, limit |  |
| [_validate_manifest](../harness/mechanics/source_media.py#L293) | manifest, files, scope, collection, size, checksum, sealed |  |
| [_validate_derived_manifest](../harness/mechanics/source_media.py#L369) | manifest, files, scope, collection, size, checksum, request | Validate fixed-profile claims and sealed byte hashes without media decoding. |
| [dimensions](../harness/mechanics/source_media.py#L406) | row |  |
| [source_frame](../harness/mechanics/source_media.py#L410) | frame |  |
| [_snapshot](../harness/mechanics/source_media.py#L478) | spec, scope, size, checksum, worker_uid | Copy ordinary files only after the whole worker is confirmed absent. |
| [_drain](../harness/mechanics/source_media.py#L550) | task | Finish an owned bounded operation even after repeated cancellation. |
| [__init__](../harness/mechanics/source_media.py#L563) | self, root, backend, app_uid, app_gid, clock, worker_uid, document_previews |  |
| [_row](../harness/mechanics/source_media.py#L579) | self, key |  |
| [_derivation_body](../harness/mechanics/source_media.py#L582) | self, row |  |
| [_spec](../harness/mechanics/source_media.py#L586) | self, row |  |
| [_valid](../harness/mechanics/source_media.py#L595) | self, scope, lease |  |
| [_update](../harness/mechanics/source_media.py#L601) | self, key, status, confirmed, error, result |  |
| [submit](../harness/mechanics/source_media.py#L605) | self, scope, generation, collection, original_sha256, original_bytes, expires_at, original_fd |  |
| [derive](../harness/mechanics/source_media.py#L609) | self, scope, generation, collection, original_sha256, original_bytes, expires_at, original_fd, derivation |  |
| [preview](../harness/mechanics/source_media.py#L615) | self, scope, document, **values |  |
| [_submit](../harness/mechanics/source_media.py#L622) | self, scope, generation, collection, original_sha256, original_bytes, expires_at, original_fd, derivation |  |
| [_expiry](../harness/mechanics/source_media.py#L670) | self, expires |  |
| [heartbeat](../harness/mechanics/source_media.py#L673) | self, scope, lease, expires_at |  |
| [_run](../harness/mechanics/source_media.py#L682) | self, scope, row, spec |  |
| [enforce_expiry](../harness/mechanics/source_media.py#L686) |  |  |
| [cleanup](../harness/mechanics/source_media.py#L731) |  |  |
| [status](../harness/mechanics/source_media.py#L745) | self, scope, lease |  |
| [stop](../harness/mechanics/source_media.py#L752) | self, scope, lease |  |
| [_reconcile](../harness/mechanics/source_media.py#L770) | self, row |  |
| [recover_lease](../harness/mechanics/source_media.py#L781) | self, scope, generation |  |
| [recover](../harness/mechanics/source_media.py#L789) | self |  |
| [output_file](../harness/mechanics/source_media.py#L794) | self, scope, lease, index |  |
| [release](../harness/mechanics/source_media.py#L809) | self, scope, lease |  |
| [close](../harness/mechanics/source_media.py#L818) | self |  |
| [_send_packet](../harness/mechanics/source_media.py#L826) | sock, payload |  |
| [_receive_packet](../harness/mechanics/source_media.py#L831) | sock |  |
| [_send_json](../harness/mechanics/source_media.py#L837) | sock, value |  |
| [_receive_json](../harness/mechanics/source_media.py#L845) | sock |  |
| [_receive_request](../harness/mechanics/source_media.py#L861) | sock, app_uid |  |
| [__init__](../harness/mechanics/source_media.py#L881) | self, broker, path |  |
| [start](../harness/mechanics/source_media.py#L886) | self |  |
| [_accept](../harness/mechanics/source_media.py#L907) | self |  |
| [_connection](../harness/mechanics/source_media.py#L917) | self, sock |  |
| [close](../harness/mechanics/source_media.py#L973) | self |  |
| [__init__](../harness/mechanics/source_media.py#L986) | self, socket_path, server_uid |  |
| [_connect](../harness/mechanics/source_media.py#L989) | self, operation, scope, lease, original_fd, **values |  |
| [_exchange](../harness/mechanics/source_media.py#L1004) | self, operation, scope, lease, **values |  |
| [_request](../harness/mechanics/source_media.py#L1008) | self, operation, scope, lease, **values |  |
| [submit](../harness/mechanics/source_media.py#L1011) | self, scope, **values |  |
| [derive](../harness/mechanics/source_media.py#L1014) | self, scope, **values |  |
| [preview](../harness/mechanics/source_media.py#L1018) | self, scope, **values |  |
| [_admit](../harness/mechanics/source_media.py#L1022) | self, operation, scope, **values |  |
| [exchange](../harness/mechanics/source_media.py#L1026) |  |  |
| [recover](../harness/mechanics/source_media.py#L1037) | self, scope, generation |  |
| [status](../harness/mechanics/source_media.py#L1041) | self, scope, lease |  |
| [heartbeat](../harness/mechanics/source_media.py#L1044) | self, scope, lease, expires_at |  |
| [stop](../harness/mechanics/source_media.py#L1047) | self, scope, lease |  |
| [release](../harness/mechanics/source_media.py#L1052) | self, scope, lease |  |
| [read_output](../harness/mechanics/source_media.py#L1055) | self, scope, lease, index |  |
| [_main](../harness/mechanics/source_media.py#L1084) | args |  |

### harness/mechanics/stored_media.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [media_format](../harness/mechanics/stored_media.py#L13) | name, prefix |  |
| [media_response](../harness/mechanics/stored_media.py#L28) | raw, media_type, range_header |  |

### harness/mechanics/title_stream.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/mechanics/title_stream.py#L17) | self, previous |  |
| [valid](../harness/mechanics/title_stream.py#L25) | text |  |
| [feed](../harness/mechanics/title_stream.py#L29) | self, event |  |

### harness/mechanics/transfer_budget.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/mechanics/transfer_budget.py#L29) | self, code, message |  |
| [__init__](../harness/mechanics/transfer_budget.py#L35) | self, period |  |
| [__init__](../harness/mechanics/transfer_budget.py#L42) | self, path, daily_cap, monthly_cap |  |
| [_periods](../harness/mechanics/transfer_budget.py#L56) | now |  |
| [_blank](../harness/mechanics/transfer_budget.py#L60) | self |  |
| [_lock](../harness/mechanics/transfer_budget.py#L69) | self |  |
| [_read_locked](../harness/mechanics/transfer_budget.py#L89) | self |  |
| [_write_locked](../harness/mechanics/transfer_budget.py#L112) | self, value |  |
| [initialize](../harness/mechanics/transfer_budget.py#L135) | self | Create the ledger once, or validate an existing ledger without resetting it. |
| [reserve](../harness/mechanics/transfer_budget.py#L143) | self, byte_count, now, path, method | Atomically reserve a response's declared bytes before its headers send. |
| [status](../harness/mechanics/transfer_budget.py#L184) | self, now |  |
| [_headers](../harness/mechanics/transfer_budget.py#L197) | message |  |
| [__init__](../harness/mechanics/transfer_budget.py#L208) | self, app, budget |  |
| [_eligible](../harness/mechanics/transfer_budget.py#L213) | cls, path, headers |  |
| [_deny](../harness/mechanics/transfer_budget.py#L220) | send, status, code |  |
| [__call__](../harness/mechanics/transfer_budget.py#L228) | self, scope, receive, send |  |
| [guarded_send](../harness/mechanics/transfer_budget.py#L233) | message |  |

### harness/mechanics/wake_tools.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [specs](../harness/mechanics/wake_tools.py#L12) | write |  |
| [_sources](../harness/mechanics/wake_tools.py#L42) | context |  |
| [read](../harness/mechanics/wake_tools.py#L50) | context, name, arguments |  |
| [call](../harness/mechanics/wake_tools.py#L58) | context, name, arguments |  |
| [_endpoints](../harness/mechanics/wake_tools.py#L83) | context |  |
| [acall](../harness/mechanics/wake_tools.py#L90) | context, name, arguments |  |

### harness/mechanics/web_mount.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [base_path](../harness/mechanics/web_mount.py#L14) | value |  |
| [__init__](../harness/mechanics/web_mount.py#L21) | self, app, prefix, orders_origin, company, read_only, public_origin |  |
| [path](../harness/mechanics/web_mount.py#L26) | self, path |  |
| [origin](../harness/mechanics/web_mount.py#L27) | self, scope |  |
| [text](../harness/mechanics/web_mount.py#L30) | self, text, origin |  |
| [attribute](../harness/mechanics/web_mount.py#L37) | match |  |
| [value](../harness/mechanics/web_mount.py#L42) | self, value, origin |  |
| [unvalue](../harness/mechanics/web_mount.py#L50) | self, value, origin |  |
| [headers](../harness/mechanics/web_mount.py#L59) | self, headers, path |  |
| [__call__](../harness/mechanics/web_mount.py#L77) | self, scope, receive, send |  |
| [normalized_receive](../harness/mechanics/web_mount.py#L103) |  |  |
| [wrapped](../harness/mechanics/web_mount.py#L112) | message |  |
| [proxy](../harness/mechanics/web_mount.py#L135) | self, scope, receive, send, path |  |
| [refuse](../harness/mechanics/web_mount.py#L164) | send, status |  |

### harness/mechanics/workspace_capabilities.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/mechanics/workspace_capabilities.py#L5) | self, connections, custom_connectors, custom_execution, inputs, contribution, builtins |  |
| [live_input_ready](../harness/mechanics/workspace_capabilities.py#L14) | collection |  |
| [execution](../harness/mechanics/workspace_capabilities.py#L17) | self, definition |  |
| [snapshot](../harness/mechanics/workspace_capabilities.py#L20) | self, collection, principal, chat_id, read_only, child, actor |  |

### harness/mechanics/workspace_identity.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_private_regular](../harness/mechanics/workspace_identity.py#L26) | descriptor |  |
| [_locked](../harness/mechanics/workspace_identity.py#L33) | state |  |
| [_read](../harness/mechanics/workspace_identity.py#L49) | path |  |
| [_write](../harness/mechanics/workspace_identity.py#L86) | state, record |  |
| [workspace_identity](../harness/mechanics/workspace_identity.py#L101) | state | Adopt once at the original location; retain that identity after migration. |
| [workspace_scope](../harness/mechanics/workspace_identity.py#L114) | state |  |
| [onboarding_identity](../harness/mechanics/workspace_identity.py#L118) | state, collection |  |
| [initialize_new_workspace](../harness/mechanics/workspace_identity.py#L125) | state | Host-only fresh-company creation; copied history must retain its identity. |

### harness/run.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [main](../harness/run.py#L10) | argv |  |

### harness/runtime/agent_auth.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_hosted](../harness/runtime/agent_auth.py#L41) | origin, host |  |
| [cli_args](../harness/runtime/agent_auth.py#L69) | self |  |
| [__init__](../harness/runtime/agent_auth.py#L75) | self, state, public_origin, mode, environ, runtime_host |  |
| [_environment](../harness/runtime/agent_auth.py#L83) | self |  |
| [status](../harness/runtime/agent_auth.py#L88) | self |  |
| [launch](../harness/runtime/agent_auth.py#L117) | self |  |
| [verify_api_credentials](../harness/runtime/agent_auth.py#L125) | self, timeout, transport | Read current model access; this does not execute or prove inference. |
| [lease](../harness/runtime/agent_auth.py#L160) | self, run_id, gateway_factory, unix_socket, activity_owner | Historical adapter fixture lease; managed execution uses ManagedPolicy.turn. |

### harness/runtime/api_smoke.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [smoke](../harness/runtime/api_smoke.py#L20) | state, api_key |  |
| [main](../harness/runtime/api_smoke.py#L42) |  |  |

### harness/runtime/hosted_capabilities.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_hash](../harness/runtime/hosted_capabilities.py#L33) | data |  |
| [_name](../harness/runtime/hosted_capabilities.py#L37) | value |  |
| [_zip](../harness/runtime/hosted_capabilities.py#L43) | name, files, directories |  |
| [_read_file](../harness/runtime/hosted_capabilities.py#L63) | package, entry | Read verified files through held directory FDs, including every ancestor. |
| [_manifest](../harness/runtime/hosted_capabilities.py#L101) | files, public_servers |  |
| [current](../harness/runtime/hosted_capabilities.py#L148) | self |  |
| [commands](../harness/runtime/hosted_capabilities.py#L154) | self, resolved |  |
| [__init__](../harness/runtime/hosted_capabilities.py#L166) | self, state, store, public_read_servers |  |
| [_cache_directory](../harness/runtime/hosted_capabilities.py#L177) | self |  |
| [_archive](../harness/runtime/hosted_capabilities.py#L183) | self, sha, data |  |
| [freeze](../harness/runtime/hosted_capabilities.py#L229) | self, configuration | Save provider configuration with private archive references, not blobs. |
| [configuration](../harness/runtime/hosted_capabilities.py#L243) | self, frozen |  |
| [_packages](../harness/runtime/hosted_capabilities.py#L260) | selection |  |
| [_guard](../harness/runtime/hosted_capabilities.py#L267) | self, principal, identity |  |
| [prepare](../harness/runtime/hosted_capabilities.py#L286) | self, principal_id, resolved_skills |  |
| [_upload](../harness/runtime/hosted_capabilities.py#L349) | name, description, data |  |
| [restore](../harness/runtime/hosted_capabilities.py#L353) | self, principal_id, identity, frozen |  |

### harness/runtime/hosted_install.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/runtime/hosted_install.py#L19) | self, transport |  |
| [acquire](../harness/runtime/hosted_install.py#L23) | self, entry, catalogue |  |

### harness/runtime/managed_children.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/runtime/managed_children.py#L10) | self, agent, chat_id, run, session, client, admission |  |
| [require_current](../harness/runtime/managed_children.py#L20) | self |  |
| [refresh](../harness/runtime/managed_children.py#L27) | self | Only a bounded, fully paginated provider response establishes lineage. |
| [ancestry](../harness/runtime/managed_children.py#L53) | self, child_id |  |
| [admit](../harness/runtime/managed_children.py#L65) | self, child_id |  |
| [public_event](../harness/runtime/managed_children.py#L97) | self, chat_id |  |
| [recover_history](../harness/runtime/managed_children.py#L103) | self | A subagent's separate canonical history repairs missed live events. |

### harness/runtime/managed_codex.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/runtime/managed_codex.py#L63) | self, code, status_code, request_id |  |
| [_identity](../harness/runtime/managed_codex.py#L75) | value |  |
| [_submission](../harness/runtime/managed_codex.py#L81) | value |  |
| [_obj](../harness/runtime/managed_codex.py#L87) | value |  |
| [type](../harness/runtime/managed_codex.py#L100) | self |  |
| [event_id](../harness/runtime/managed_codex.py#L104) | self |  |
| [session_id](../harness/runtime/managed_codex.py#L108) | self |  |
| [turn_id](../harness/runtime/managed_codex.py#L113) | self |  |
| [item_id](../harness/runtime/managed_codex.py#L118) | self |  |
| [subagent_id](../harness/runtime/managed_codex.py#L122) | self |  |
| [root_turn_outcome](../harness/runtime/managed_codex.py#L129) | self |  |
| [category](../harness/runtime/managed_codex.py#L138) | self |  |
| [__init__](../harness/runtime/managed_codex.py#L174) | self, api_key, transport, timeout, max_event_bytes, spending_mode |  |
| [__aenter__](../harness/runtime/managed_codex.py#L191) | self |  |
| [__aexit__](../harness/runtime/managed_codex.py#L194) | self, *exc |  |
| [aclose](../harness/runtime/managed_codex.py#L197) | self |  |
| [_check](../harness/runtime/managed_codex.py#L201) | response |  |
| [_request](../harness/runtime/managed_codex.py#L206) | self, method, path, body, params, submission_key |  |
| [_session_path](../harness/runtime/managed_codex.py#L227) | session_id |  |
| [_page_params](../harness/runtime/managed_codex.py#L231) | after, limit, order |  |
| [list_artifacts](../harness/runtime/managed_codex.py#L236) | self, session_id, after, limit, order |  |
| [get_artifact](../harness/runtime/managed_codex.py#L241) | self, session_id, artifact_id |  |
| [artifact_content](../harness/runtime/managed_codex.py#L244) | self, session_id, artifact_id, max_bytes | Read bounded immutable bytes from the fixed provider origin, without redirects. |
| [create_session](../harness/runtime/managed_codex.py#L269) | self, config, submission_key | Create a bounded session using OpenAI-managed execution. |
| [_spend_control](../harness/runtime/managed_codex.py#L289) | value |  |
| [update_session](../harness/runtime/managed_codex.py#L294) | self, session_id, config, submission_key | Update subsequent turns while preserving a finite session allowance. |
| [delete_session](../harness/runtime/managed_codex.py#L306) | self, session_id, submission_key | Delete a caller-owned session and request its hosted sandbox cleanup. |
| [get_session](../harness/runtime/managed_codex.py#L310) | self, session_id |  |
| [list_sessions](../harness/runtime/managed_codex.py#L313) | self, after, limit, order |  |
| [get_turn](../harness/runtime/managed_codex.py#L317) | self, session_id, turn_id |  |
| [list_turns](../harness/runtime/managed_codex.py#L320) | self, session_id, after, limit, order |  |
| [list_subagent_turns](../harness/runtime/managed_codex.py#L325) | self, session_id, subagent_id, after, limit, order | Inspect child turns separately; an active child may be idle. |
| [list_items](../harness/runtime/managed_codex.py#L333) | self, session_id, subagent_id, after, limit, order |  |
| [list_subagents](../harness/runtime/managed_codex.py#L340) | self, session_id, after, limit, order |  |
| [submit_events](../harness/runtime/managed_codex.py#L345) | self, session_id, events, submission_key | Send native message/cancel/tool-result/approval schemas unchanged. |
| [send_message](../harness/runtime/managed_codex.py#L352) | self, session_id, text, submission_key, images |  |
| [steer](../harness/runtime/managed_codex.py#L363) | self, session_id, text, submission_key | Native message input steers an active turn, or starts an idle turn. |
| [interrupt](../harness/runtime/managed_codex.py#L367) | self, session_id, submission_key | Request cancellation; await native terminal events to confirm its result. |
| [open_events](../harness/runtime/managed_codex.py#L373) | self, session_id | Subscribe before sending. EOF is a disconnect, not a successful turn. |
| [_decode_events](../harness/runtime/managed_codex.py#L388) | self, response |  |
| [_collect](../harness/runtime/managed_codex.py#L426) | self, fetch, max_pages |  |
| [collect_items](../harness/runtime/managed_codex.py#L444) | self, session_id, subagent_id, max_pages |  |
| [fetch](../harness/runtime/managed_codex.py#L446) | **params |  |
| [recover_session](../harness/runtime/managed_codex.py#L451) | self, session_id, max_pages, max_buffered_events | Open+buffer SSE, then retrieve canonical state, without resubmitting work. |
| [pump](../harness/runtime/managed_codex.py#L465) |  |  |
| [buffered_events](../harness/runtime/managed_codex.py#L477) |  |  |
| [fetch_turns](../harness/runtime/managed_codex.py#L501) | **params |  |

### harness/runtime/managed_diagnostics.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_details](../harness/runtime/managed_diagnostics.py#L24) | error, phase |  |
| [record_failure](../harness/runtime/managed_diagnostics.py#L51) | state, chat_id, error, phase | Keep the latest private failure per hashed chat; failures here preserve UI. |

### harness/runtime/managed_files.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [resource_id](../harness/runtime/managed_files.py#L19) | value |  |
| [metadata](../harness/runtime/managed_files.py#L25) | value |  |
| [__init__](../harness/runtime/managed_files.py#L44) | self, agent, ledger, client, current |  |
| [require_current](../harness/runtime/managed_files.py#L47) | self, binding |  |
| [completed_turn](../harness/runtime/managed_files.py#L57) | self, binding, session, artifact |  |
| [harvest](../harness/runtime/managed_files.py#L98) | self, binding |  |

### harness/runtime/managed_policy.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/runtime/managed_policy.py#L21) | self, authority, usage, binding_id |  |
| [created](../harness/runtime/managed_policy.py#L24) | self, session_id |  |
| [current](../harness/runtime/managed_policy.py#L28) | self |  |
| [__init__](../harness/runtime/managed_policy.py#L32) | self, configuration, mcp, generation, usage, request_id, steering, binding_id |  |
| [created](../harness/runtime/managed_policy.py#L38) | self, session_id |  |
| [revoke](../harness/runtime/managed_policy.py#L42) | self, disconnected |  |
| [persist_monitor](../harness/runtime/managed_policy.py#L49) | self, receipt |  |
| [finish](../harness/runtime/managed_policy.py#L52) | self, snapshot, terminal_status |  |
| [__init__](../harness/runtime/managed_policy.py#L75) | self, turn_limit_cents, spending_mode |  |
| [_require](../harness/runtime/managed_policy.py#L82) | agent, chat_id, run, admission |  |
| [base_configuration](../harness/runtime/managed_policy.py#L97) | self, agent, chat_id, tools, instructions |  |
| [_monitor](../harness/runtime/managed_policy.py#L122) | self, usage, request_id, run, target, model, recovering, baseline |  |
| [_role_turn](../harness/runtime/managed_policy.py#L151) | self, agent, chat_id, session_id, request_id, binding_id, admission, run, recovering |  |
| [turn](../harness/runtime/managed_policy.py#L177) | self, agent, chat_id, tools, instructions, session_id, request_id, binding_id, admission, run, recovering, steering |  |
| [_provider_limit](../harness/runtime/managed_policy.py#L259) | snapshot, session_id, usage, binding_id, allowance, roles |  |

### harness/runtime/managed_runtime.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [resolved](../harness/runtime/managed_runtime.py#L28) | value |  |
| [function_tools](../harness/runtime/managed_runtime.py#L32) | registry | Delegation belongs to OpenAI's stock coordinator tools. |
| [portable_content](../harness/runtime/managed_runtime.py#L40) | content, state |  |
| [pages](../harness/runtime/managed_runtime.py#L63) | fetch, limit |  |
| [quiescent](../harness/runtime/managed_runtime.py#L80) | client, session_id | An available subagent may be idle; its saved turns decide quiescence. |
| [__init__](../harness/runtime/managed_runtime.py#L102) | self, client_factory, policy, timeout |  |
| [_require](../harness/runtime/managed_runtime.py#L108) | agent, chat_id, run, admission |  |
| [_input](../harness/runtime/managed_runtime.py#L118) | self, agent, message, chat_id, dataset, attachments, clips, skills, model_context, selected |  |
| [_history](../harness/runtime/managed_runtime.py#L136) | input_value, record, current_user |  |
| [_revoke_binding](../harness/runtime/managed_runtime.py#L154) | agent, binding |  |
| [_cancel](../harness/runtime/managed_runtime.py#L160) | self, run | A local cancellation flag alone never confirms upstream cancellation. |
| [control](../harness/runtime/managed_runtime.py#L200) | self, agent, chat_id, operation, message, attachments, clip_attachments, skill_ids, sender |  |
| [_update](../harness/runtime/managed_runtime.py#L243) | client, engine, configuration, key |  |
| [_observe](../harness/runtime/managed_runtime.py#L255) | self, client, engine, created, input_value, submission_key, baseline |  |
| [_project](../harness/runtime/managed_runtime.py#L340) | self, observer, run | Publish host prompts while a provider function awaits their answer. |
| [_stop_monitor](../harness/runtime/managed_runtime.py#L389) | run |  |
| [_harvest_files](../harness/runtime/managed_runtime.py#L395) | self, agent, client, chat_id, current, answer, binding_id |  |
| [recover_files](../harness/runtime/managed_runtime.py#L432) | self, agent, chat_id | Read retained generations without sending input or reserving new funds. |
| [run](../harness/runtime/managed_runtime.py#L457) | self, agent, message, chat_id, dataset, attachments, clip_attachments, resolved_skills, model_context, instructions, recovering, recovery_answer, delegated_grant |  |
| [execute](../harness/runtime/managed_runtime.py#L631) | name, arguments |  |
| [monitored_stop](../harness/runtime/managed_runtime.py#L659) | reason |  |
| [files_current](../harness/runtime/managed_runtime.py#L714) |  |  |
| [cleanup](../harness/runtime/managed_runtime.py#L739) |  |  |
| [recover](../harness/runtime/managed_runtime.py#L799) | self, agent, chat_id | Recover current access, or withdraw already-funded work after access ends. |
| [_recover_admitted](../harness/runtime/managed_runtime.py#L833) | self, agent, chat_id | Resume the exact pending outbox into its original saved assistant row. |
| [recover_request](../harness/runtime/managed_runtime.py#L874) | self, agent, chat_id, logical_id | Resolve one saved scheduler input without creating another provider turn. |
| [revoke_plugin](../harness/runtime/managed_runtime.py#L897) | self, agent, principal_id, plugin_id | Retire every original session carrying a removed package, including idle ones. |
| [recover_pending](../harness/runtime/managed_runtime.py#L946) | self, agent | Workspace startup can resume admitted requests without new input/funding. |
| [configured_runtime](../harness/runtime/managed_runtime.py#L961) | agent | Use the owning workspace's protected OpenAI credential and funded policy. |
| [client](../harness/runtime/managed_runtime.py#L966) |  |  |

### harness/runtime/managed_spend.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [spending_mode](../harness/runtime/managed_spend.py#L19) | value |  |
| [estimate_cents](../harness/runtime/managed_spend.py#L26) | snapshot, model | Conservative token estimate; missing optional usage stays unknown. |
| [__init__](../harness/runtime/managed_spend.py#L54) | self, target_cents, deadline_at, model, baseline, observed_cents |  |
| [from_receipt](../harness/runtime/managed_spend.py#L69) | cls, receipt |  |
| [receipt](../harness/runtime/managed_spend.py#L76) | self |  |
| [observe](../harness/runtime/managed_spend.py#L82) | self, snapshot |  |
| [watch](../harness/runtime/managed_spend.py#L89) | self, client, session_id, cancel, persist, poll_interval | Poll until cancellation is requested; caller owns root/child Stop proof. |

### harness/runtime/managed_turn.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [current_managed_call](../harness/runtime/managed_turn.py#L19) |  | Host-only identity of the ledger-admitted function being executed now. |
| [hosted_connection_pending](../harness/runtime/managed_turn.py#L25) | session, action | OpenAI connects its hosted environment; the host only waits for readiness. |
| [__init__](../harness/runtime/managed_turn.py#L40) | self, client, ledger, binding, run, admission, registry, execute, result_fields, current, request, children |  |
| [require_current](../harness/runtime/managed_turn.py#L60) | self |  |
| [accept_session](../harness/runtime/managed_turn.py#L65) | self, session |  |
| [attributed_turn](../harness/runtime/managed_turn.py#L74) | self, turn_id |  |
| [required_actions](../harness/runtime/managed_turn.py#L86) | self | History items and client arguments never authorize effect execution. |
| [event](../harness/runtime/managed_turn.py#L183) | self, event | Whitelist public fields; provider errors/configuration remain private. |
| [snapshot](../harness/runtime/managed_turn.py#L245) | self, session, items, turns, turn_ids | Reconcile canonical public history before consuming buffered events. |
| [child_output](../harness/runtime/managed_turn.py#L272) | self, turn, event |  |

### harness/runtime/native_approvals.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [identity](../harness/runtime/native_approvals.py#L30) | value |  |
| [canonical](../harness/runtime/native_approvals.py#L34) | value |  |
| [digest](../harness/runtime/native_approvals.py#L38) | value |  |
| [native_key](../harness/runtime/native_approvals.py#L39) | value |  |
| [stamp](../harness/runtime/native_approvals.py#L42) | value |  |
| [arguments](../harness/runtime/native_approvals.py#L43) | value |  |
| [__post_init__](../harness/runtime/native_approvals.py#L54) | self |  |
| [__post_init__](../harness/runtime/native_approvals.py#L73) | self |  |
| [permitted](../harness/runtime/native_approvals.py#L91) | self |  |
| [__init__](../harness/runtime/native_approvals.py#L94) | self, state, clock |  |
| [_db](../harness/runtime/native_approvals.py#L118) | self |  |
| [_public](../harness/runtime/native_approvals.py#L127) | row |  |
| [_row](../harness/runtime/native_approvals.py#L137) | db, request_id, scope |  |
| [_change](../harness/runtime/native_approvals.py#L143) | self, db, row, status, reason, **changes |  |
| [_fresh](../harness/runtime/native_approvals.py#L148) | self, db, row, scope, binding, cancelled, refusing |  |
| [open](../harness/runtime/native_approvals.py#L156) | self, scope, actor_chat_id, native_request_id, turn_id, call_id, binding, tool_arguments, ttl_seconds |  |
| [get](../harness/runtime/native_approvals.py#L181) | self, request_id, scope |  |
| [interrupt](../harness/runtime/native_approvals.py#L184) | self, request_id, scope, reason | Retire one owned saved request after its live root connection is gone. |
| [for_chat](../harness/runtime/native_approvals.py#L195) | self, scope |  |
| [delivery_guard](../harness/runtime/native_approvals.py#L199) | self, request_id, scope, binding, cancelled | Synchronous predicate executed under the native connection write lock. |
| [answer](../harness/runtime/native_approvals.py#L210) | self, request_id, scope, binding, action, deliver, cancelled |  |
| [resolve_native](../harness/runtime/native_approvals.py#L241) | self, scope, native_request_id |  |
| [invalidate](../harness/runtime/native_approvals.py#L254) | self, scope, provider, company_id, owner, reason | Host Stop/disconnect/reconfiguration hook; dispatched writes stay uncertain. |
| [provider_cancellations](../harness/runtime/native_approvals.py#L274) | self, scope, provider | Private outstanding reply IDs, including a prior durable invalidation. |
| [preflight_failed](../harness/runtime/native_approvals.py#L283) | self, request_id, scope | Close failed host preflight; return a private reply ID only if unanswered. |
| [cancel_guard](../harness/runtime/native_approvals.py#L297) | self, request_id, scope, cancelled | Close one still-unanswered native request under its transport lock. |
| [finish_call](../harness/runtime/native_approvals.py#L306) | self, scope, thread_id, turn_id, call_id |  |
| [expire](../harness/runtime/native_approvals.py#L318) | self, scope | Return private native reply IDs alongside public records for one host run. |
| [recover](../harness/runtime/native_approvals.py#L326) | self |  |
| [claim_dispatch](../harness/runtime/native_approvals.py#L328) | self, scope, binding, metadata, tool_arguments, cancelled | Host-only future transport hook. No caller in this increment sends writes. |
| [provider_has_unresolved](../harness/runtime/native_approvals.py#L351) | self, scope, provider, metadata | Host admission across this owner's chats; exact-call replay is exempt. |
| [outcome](../harness/runtime/native_approvals.py#L372) | self, request_id, scope, status, receipt | Host reconciliation only; never infer remote success from native completion. |
| [__init__](../harness/runtime/native_approvals.py#L393) | self, store, scope, resolve_binding, cancelled, write |  |
| [_deny](../harness/runtime/native_approvals.py#L398) | self, native_id |  |
| [event](../harness/runtime/native_approvals.py#L401) | self, item, actor_chat_id |  |
| [answer](../harness/runtime/native_approvals.py#L446) | self, request_id, owner, action |  |
| [deliver](../harness/runtime/native_approvals.py#L458) | native_id, payload, guard |  |
| [retire](../harness/runtime/native_approvals.py#L464) | self, reason |  |
| [revoke_provider](../harness/runtime/native_approvals.py#L468) | self, provider | Close this run's provider waits after host connection revocation begins. |
| [expire](../harness/runtime/native_approvals.py#L480) | self |  |

### harness/runtime/native_events.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_text](../harness/runtime/native_events.py#L21) | value, limit |  |
| [_output](../harness/runtime/native_events.py#L25) | value |  |
| [_arguments](../harness/runtime/native_events.py#L30) | value | Native arguments are public, but a malformed/huge value need not fill chat. |
| [_question_record](../harness/runtime/native_events.py#L43) | params, request_id |  |
| [context_usage](../harness/runtime/native_events.py#L79) | token_usage |  |
| [plan_usage](../harness/runtime/native_events.py#L94) | response | Keep native plan windows; exclude account IDs and opaque credit currencies. |
| [__init__](../harness/runtime/native_events.py#L112) | self, result_fields |  |
| [_message](../harness/runtime/native_events.py#L120) | self, identity, text |  |
| [translate_many](../harness/runtime/native_events.py#L125) | self, method, params, request_id, verified_children | Expand a native item without deriving product authority from its IDs. |
| [translate](../harness/runtime/native_events.py#L158) | self, method, params, request_id |  |

### harness/runtime/native_executor.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__post_init__](../harness/runtime/native_executor.py#L54) | self |  |
| [key](../harness/runtime/native_executor.py#L60) | self |  |
| [__post_init__](../harness/runtime/native_executor.py#L71) | self |  |
| [name](../harness/runtime/native_executor.py#L90) | self |  |
| [_command](../harness/runtime/native_executor.py#L94) | timeout, input, *argv |  |
| [__init__](../harness/runtime/native_executor.py#L122) | self, root, size_bytes |  |
| [mount](../harness/runtime/native_executor.py#L128) | self, key |  |
| [unmount](../harness/runtime/native_executor.py#L169) | self, volume |  |
| [__init__](../harness/runtime/native_executor.py#L177) | self, volumes |  |
| [mount](../harness/runtime/native_executor.py#L182) | self, key |  |
| [volume_path](../harness/runtime/native_executor.py#L185) | self, key |  |
| [unmount](../harness/runtime/native_executor.py#L188) | self, volume |  |
| [inspect](../harness/runtime/native_executor.py#L191) | self, spec |  |
| [flags](../harness/runtime/native_executor.py#L197) | spec |  |
| [start](../harness/runtime/native_executor.py#L211) | self, spec, capability |  |
| [pause](../harness/runtime/native_executor.py#L244) | self, spec |  |
| [unpause](../harness/runtime/native_executor.py#L250) | self, spec |  |
| [stop](../harness/runtime/native_executor.py#L253) | self, spec |  |
| [_path_parts](../harness/runtime/native_executor.py#L260) | value |  |
| [_checked_directory](../harness/runtime/native_executor.py#L269) | parent, name, uid |  |
| [snapshot_outputs](../harness/runtime/native_executor.py#L278) | workspace, destination, uid, paths | Snapshot owned ordinary files without following a mutable path or symlink. |
| [copy_file](../harness/runtime/native_executor.py#L293) | parent, name, relative |  |
| [walk](../harness/runtime/native_executor.py#L327) | parent, prefix, depth |  |
| [__init__](../harness/runtime/native_executor.py#L383) | self, root, run_root, backend, app_uid, app_gid, clock, socket_owner, socket_group |  |
| [live_count](../harness/runtime/native_executor.py#L409) | self |  |
| [_row](../harness/runtime/native_executor.py#L414) | self, key |  |
| [_spec](../harness/runtime/native_executor.py#L417) | self, row |  |
| [_update](../harness/runtime/native_executor.py#L423) | self, key, status, volume |  |
| [_validate](../harness/runtime/native_executor.py#L429) | self, scope, lease |  |
| [prepare](../harness/runtime/native_executor.py#L441) | self, scope |  |
| [_freeze_sockets](../harness/runtime/native_executor.py#L469) | self, spec |  |
| [install_packages](../harness/runtime/native_executor.py#L487) | self, scope, lease, reader, writer | Reserve the lease before accepting a bounded stream; no host paths. |
| [start](../harness/runtime/native_executor.py#L540) | self, scope, lease, capability |  |
| [_stop_row](../harness/runtime/native_executor.py#L562) | self, row |  |
| [stop](../harness/runtime/native_executor.py#L590) | self, scope, lease | Caller revokes model/MCP grants first; removal kills the whole process tree. |
| [reconcile](../harness/runtime/native_executor.py#L606) | self |  |
| [expire_prepared](../harness/runtime/native_executor.py#L618) | self |  |
| [snapshot](../harness/runtime/native_executor.py#L630) | self, scope, lease, paths |  |
| [output_file](../harness/runtime/native_executor.py#L674) | self, scope, lease, snapshot_id, index |  |
| [_read_package_frame](../harness/runtime/native_executor.py#L691) | reader, limit |  |
| [_read_frame](../harness/runtime/native_executor.py#L697) | reader |  |
| [_write_frame](../harness/runtime/native_executor.py#L704) | writer, kind, body |  |
| [__init__](../harness/runtime/native_executor.py#L712) | self, broker, path |  |
| [start](../harness/runtime/native_executor.py#L719) | self |  |
| [expire](../harness/runtime/native_executor.py#L733) |  |  |
| [close](../harness/runtime/native_executor.py#L739) | self |  |
| [_connection](../harness/runtime/native_executor.py#L757) | self, reader, writer |  |
| [_fields](../harness/runtime/native_executor.py#L841) | value, allowed |  |
| [_reply](../harness/runtime/native_executor.py#L847) | writer, value |  |
| [_relay](../harness/runtime/native_executor.py#L855) | process, reader, writer |  |
| [stdin](../harness/runtime/native_executor.py#L856) |  |  |
| [output](../harness/runtime/native_executor.py#L867) | source, kind |  |
| [__init__](../harness/runtime/native_executor.py#L888) | self, writer |  |
| [write](../harness/runtime/native_executor.py#L891) | self, data |  |
| [drain](../harness/runtime/native_executor.py#L896) | self |  |
| [write_eof](../harness/runtime/native_executor.py#L899) | self |  |
| [close](../harness/runtime/native_executor.py#L902) | self |  |
| [__init__](../harness/runtime/native_executor.py#L909) | self, client, scope, lease, reader, writer |  |
| [_pump](../harness/runtime/native_executor.py#L918) | self |  |
| [wait](../harness/runtime/native_executor.py#L945) | self |  |
| [stop](../harness/runtime/native_executor.py#L948) | self |  |
| [__init__](../harness/runtime/native_executor.py#L957) | self, socket_path |  |
| [_connect](../harness/runtime/native_executor.py#L960) | self, operation, scope, lease, **values |  |
| [_request](../harness/runtime/native_executor.py#L980) | self, operation, scope, lease, **values |  |
| [prepare](../harness/runtime/native_executor.py#L986) | self, scope |  |
| [install_packages](../harness/runtime/native_executor.py#L989) | self, scope, lease, selection |  |
| [start](../harness/runtime/native_executor.py#L1030) | self, scope, lease, gateway_capability |  |
| [stop](../harness/runtime/native_executor.py#L1034) | self, scope, lease |  |
| [snapshot](../harness/runtime/native_executor.py#L1037) | self, scope, lease, paths |  |
| [read_output](../harness/runtime/native_executor.py#L1040) | self, scope, lease, snapshot_id, index |  |

### harness/runtime/native_install_broker.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [drain](../harness/runtime/native_install_broker.py#L31) | task |  |
| [__init__](../harness/runtime/native_install_broker.py#L38) | self, broker, allowed_sources, worker_path, backend |  |
| [live_count](../harness/runtime/native_install_broker.py#L54) | self |  |
| [_row](../harness/runtime/native_install_broker.py#L57) | self, identifier |  |
| [_status](../harness/runtime/native_install_broker.py#L58) | self, key, status, result |  |
| [_lease](../harness/runtime/native_install_broker.py#L60) | self, row |  |
| [_validate](../harness/runtime/native_install_broker.py#L61) | self, scope, lease |  |
| [_public](../harness/runtime/native_install_broker.py#L66) | self, row |  |
| [prepare](../harness/runtime/native_install_broker.py#L71) | self, scope, request_id, document |  |
| [upload](../harness/runtime/native_install_broker.py#L90) | self, scope, lease, reader, writer |  |
| [_run](../harness/runtime/native_install_broker.py#L119) | self, key |  |
| [_finish](../harness/runtime/native_install_broker.py#L130) | self, key, successful |  |
| [_freeze](../harness/runtime/native_install_broker.py#L158) | self, key, document |  |
| [stop](../harness/runtime/native_install_broker.py#L187) | self, scope, lease |  |
| [release](../harness/runtime/native_install_broker.py#L200) | self, scope, lease |  |
| [_discard](../harness/runtime/native_install_broker.py#L208) | self, key |  |
| [reconcile](../harness/runtime/native_install_broker.py#L217) | self |  |
| [expire](../harness/runtime/native_install_broker.py#L229) | self |  |
| [read](../harness/runtime/native_install_broker.py#L246) | self, scope, lease, writer |  |
| [handle](../harness/runtime/native_install_broker.py#L260) | self, operation, scope, request, reader, writer |  |
| [__init__](../harness/runtime/native_install_broker.py#L279) | self, root, script |  |
| [volume_key](../harness/runtime/native_install_broker.py#L283) | key |  |
| [name](../harness/runtime/native_install_broker.py#L285) | key |  |
| [volume_path](../harness/runtime/native_install_broker.py#L286) | self, key |  |
| [run](../harness/runtime/native_install_broker.py#L287) | self, key, incoming |  |
| [stop](../harness/runtime/native_install_broker.py#L294) | self, key |  |
| [present](../harness/runtime/native_install_broker.py#L295) |  |  |
| [unmount](../harness/runtime/native_install_broker.py#L298) | self, key |  |

### harness/runtime/native_install_client.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [drain](../harness/runtime/native_install_client.py#L23) | task |  |
| [__init__](../harness/runtime/native_install_client.py#L30) | self, socket_path |  |
| [_connect](../harness/runtime/native_install_client.py#L31) | self, operation, scope, **values |  |
| [_request](../harness/runtime/native_install_client.py#L42) | self, operation, scope, **values |  |
| [capabilities](../harness/runtime/native_install_client.py#L45) | self, scope |  |
| [prepare](../harness/runtime/native_install_client.py#L46) | self, scope, request_id, document |  |
| [request](../harness/runtime/native_install_client.py#L48) | self, operation, scope, lease |  |
| [upload](../harness/runtime/native_install_client.py#L50) | self, scope, lease, path, document |  |
| [read](../harness/runtime/native_install_client.py#L61) | self, scope, lease, destination, document |  |
| [__init__](../harness/runtime/native_install_client.py#L91) | self, state, client, fetch |  |
| [acquire_for_principal](../harness/runtime/native_install_client.py#L96) | self, entry, catalogue, principal_id |  |
| [cleanup](../harness/runtime/native_install_client.py#L132) |  |  |

### harness/runtime/native_install_readiness.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/runtime/native_install_readiness.py#L19) | self, state, enabled, client |  |
| [probe](../harness/runtime/native_install_readiness.py#L26) | self, store, principal_id |  |

### harness/runtime/native_install_source.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [url](../harness/runtime/native_install_source.py#L31) | self |  |
| [archive_root](../harness/runtime/native_install_source.py#L34) | self |  |
| [document](../harness/runtime/native_install_source.py#L36) | self |  |
| [source_spec](../harness/runtime/native_install_source.py#L38) | entry, catalogue |  |
| [fetch_archive](../harness/runtime/native_install_source.py#L68) | spec, destination, transport | One finite public HTTPS attempt; caller retries a fresh request explicitly. |

### harness/runtime/native_install_worker.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [canonical](../harness/runtime/native_install_worker.py#L29) | value |  |
| [sha](../harness/runtime/native_install_worker.py#L30) | value |  |
| [request](../harness/runtime/native_install_worker.py#L32) | value |  |
| [parts](../harness/runtime/native_install_worker.py#L45) | value |  |
| [verify_archive](../harness/runtime/native_install_worker.py#L51) | path, expected |  |
| [extract_selected](../harness/runtime/native_install_worker.py#L62) | archive, expected, destination | Stream selected subtree only, rejecting links/devices and ambiguous names. |
| [tree_inventory](../harness/runtime/native_install_worker.py#L100) | root |  |
| [materialize](../harness/runtime/native_install_worker.py#L117) | archive, document, workspace, execute |  |
| [run](../harness/runtime/native_install_worker.py#L133) | arguments |  |

### harness/runtime/native_mcp.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__getattr__](../harness/runtime/native_mcp.py#L38) | name |  |
| [__post_init__](../harness/runtime/native_mcp.py#L58) | self |  |
| [_error](../harness/runtime/native_mcp.py#L82) | message |  |
| [__init__](../harness/runtime/native_mcp.py#L95) | self, agent, scope, company_id, clock, call_timeout, provider_relay |  |
| [list_tools](../harness/runtime/native_mcp.py#L117) |  |  |
| [call_tool](../harness/runtime/native_mcp.py#L129) | name, arguments |  |
| [_lineage](../harness/runtime/native_mcp.py#L139) | self, chat_id, thread_id |  |
| [issue](../harness/runtime/native_mcp.py#L162) | self, actor_chat_id, actor_thread_id, ttl_seconds | Host-only grant creation; default is the inherited read-only root grant. |
| [issue_provider](../harness/runtime/native_mcp.py#L183) | self, server_name, ttl_seconds | Host-only: bind an original server to its package or direct policy. |
| [provider_configs](../harness/runtime/native_mcp.py#L193) | self | Private native config writes; credentials remain in the host broker. |
| [_provider_read](../harness/runtime/native_mcp.py#L206) | self, binding, operation |  |
| [invoke](../harness/runtime/native_mcp.py#L209) |  |  |
| [drain](../harness/runtime/native_mcp.py#L224) |  |  |
| [_participant_reach_context](../harness/runtime/native_mcp.py#L237) | self, binding |  |
| [_provider_write](../harness/runtime/native_mcp.py#L241) | self, binding, name, arguments, metadata |  |
| [drain](../harness/runtime/native_mcp.py#L270) |  |  |
| [_valid](../harness/runtime/native_mcp.py#L280) | self, binding |  |
| [revoke](../harness/runtime/native_mcp.py#L294) | self, grant_id |  |
| [revoke_all](../harness/runtime/native_mcp.py#L300) | self |  |
| [_call](../harness/runtime/native_mcp.py#L305) | self, binding, name, arguments, metadata |  |
| [invoke](../harness/runtime/native_mcp.py#L327) |  |  |
| [_result](../harness/runtime/native_mcp.py#L358) | parts |  |
| [lifespan](../harness/runtime/native_mcp.py#L387) | self |  |
| [__call__](../harness/runtime/native_mcp.py#L396) | self, scope, receive, send |  |
| [_http_error](../harness/runtime/native_mcp.py#L431) | send, status |  |

### harness/runtime/native_package_mount.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [encoded](../harness/runtime/native_package_mount.py#L30) | value |  |
| [digest](../harness/runtime/native_package_mount.py#L33) | value |  |
| [parts](../harness/runtime/native_package_mount.py#L36) | value |  |
| [validate_metadata](../harness/runtime/native_package_mount.py#L44) | value, company, owner |  |
| [selection_metadata](../harness/runtime/native_package_mount.py#L86) | selection |  |
| [_read_json](../harness/runtime/native_package_mount.py#L93) | path |  |
| [native_config](../harness/runtime/native_package_mount.py#L98) | root, metadata | Enable original skills; explicitly disable every bundled MCP server. |
| [seal](../harness/runtime/native_package_mount.py#L140) | root |  |
| [ensure_mount_target](../harness/runtime/native_package_mount.py#L150) | volume | Never follow model-created links when preparing Docker's nested target. |
| [open_source](../harness/runtime/native_package_mount.py#L165) | root, relative | Held descriptor chain prevents app-owned source symlinks from redirecting. |
| [toml_value](../harness/runtime/native_package_mount.py#L181) | value | Codex -c expects TOML values; JSON object colons are not TOML assignments. |

### harness/runtime/native_packages.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_read_packages](../harness/runtime/native_packages.py#L44) | function, *args, **kwargs | Hash bounded package trees off-loop while retaining the caller's fence. |
| [_json](../harness/runtime/native_packages.py#L63) | value |  |
| [_hash](../harness/runtime/native_packages.py#L67) | value |  |
| [_principal](../harness/runtime/native_packages.py#L71) | value |  |
| [_name](../harness/runtime/native_packages.py#L77) | value |  |
| [_ordinary_directory](../harness/runtime/native_packages.py#L83) | path, create |  |
| [_fsync_dir](../harness/runtime/native_packages.py#L98) | path |  |
| [_identity](../harness/runtime/native_packages.py#L104) | info |  |
| [_scan_tree_unchecked](../harness/runtime/native_packages.py#L138) | root, destination | Walk held directory FDs and hash/copy exact regular files without following links. |
| [visit](../harness/runtime/native_packages.py#L145) | fd, relative, depth |  |
| [_scan_tree](../harness/runtime/native_packages.py#L219) | root, destination |  |
| [_remove_private_tree](../harness/runtime/native_packages.py#L226) | path |  |
| [__init__](../harness/runtime/native_packages.py#L235) | self, executable, timeout |  |
| [_base](../harness/runtime/native_packages.py#L240) | self |  |
| [_environment](../harness/runtime/native_packages.py#L253) | home |  |
| [_stop](../harness/runtime/native_packages.py#L260) | process |  |
| [_drain_cleanup](../harness/runtime/native_packages.py#L271) | task |  |
| [_command](../harness/runtime/native_packages.py#L277) | self, args, home, cwd |  |
| [discard](../harness/runtime/native_packages.py#L282) | stream |  |
| [cleanup](../harness/runtime/native_packages.py#L284) | process |  |
| [read](../harness/runtime/native_packages.py#L305) | stream, limit |  |
| [_source](../harness/runtime/native_packages.py#L324) | self, entry, snapshot, market |  |
| [acquire](../harness/runtime/native_packages.py#L336) | self, entry, snapshot |  |
| [__init__](../harness/runtime/native_packages.py#L362) | self, state, catalogue_snapshot, materializer |  |
| [_db](../harness/runtime/native_packages.py#L386) | self |  |
| [_lock](../harness/runtime/native_packages.py#L397) | self |  |
| [_entry](../harness/runtime/native_packages.py#L410) | self, identifier |  |
| [_rows](../harness/runtime/native_packages.py#L416) | self, owner |  |
| [_public](../harness/runtime/native_packages.py#L424) | body |  |
| [list](../harness/runtime/native_packages.py#L429) | self, principal_id |  |
| [read](../harness/runtime/native_packages.py#L433) | self, identifier, principal_id |  |
| [_verified](../harness/runtime/native_packages.py#L439) | self, body |  |
| [_reconcile_trees](../harness/runtime/native_packages.py#L449) | self |  |
| [install](../harness/runtime/native_packages.py#L463) | self, identifier, principal_id |  |
| [uninstall](../harness/runtime/native_packages.py#L534) | self, identifier, principal_id |  |
| [snapshot](../harness/runtime/native_packages.py#L544) | self, principal_id, plugin_ids |  |
| [runtime_selection](../harness/runtime/native_packages.py#L559) | self, principal_id | Prevent install/removal racing a bounded native worker start. |
| [validate_runtime_snapshot](../harness/runtime/native_packages.py#L565) | self, selection, principal_id | Recheck the selected package bytes inside the held runtime lock. |
| [validate_snapshot](../harness/runtime/native_packages.py#L569) | self, selection, principal_id |  |

### harness/runtime/native_plugins.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/runtime/native_plugins.py#L29) | self, process |  |
| [call](../harness/runtime/native_plugins.py#L32) | self, method, params |  |
| [__init__](../harness/runtime/native_plugins.py#L59) | self, state, api_key, executable, snapshot, session_factory |  |
| [_paths](../harness/runtime/native_plugins.py#L68) | self, principal_id |  |
| [_manifest](../harness/runtime/native_plugins.py#L81) | self |  |
| [_session](../harness/runtime/native_plugins.py#L97) | self, principal_id |  |
| [_entry](../harness/runtime/native_plugins.py#L160) | self, identifier |  |
| [_status](../harness/runtime/native_plugins.py#L169) | row |  |
| [_list](../harness/runtime/native_plugins.py#L174) | self, session, marketplace |  |
| [list](../harness/runtime/native_plugins.py#L181) | self, principal_id |  |
| [read](../harness/runtime/native_plugins.py#L185) | self, identifier, principal_id |  |
| [install](../harness/runtime/native_plugins.py#L194) | self, identifier, principal_id |  |
| [uninstall](../harness/runtime/native_plugins.py#L205) | self, identifier, principal_id |  |
| [set_enabled](../harness/runtime/native_plugins.py#L217) | self, identifier, enabled, principal_id |  |

### harness/runtime/native_provider_relay.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_read](../harness/runtime/native_provider_relay.py#L26) | function, *args, **kwargs |  |
| [_canonical_policy](../harness/runtime/native_provider_relay.py#L55) | value |  |
| [__init__](../harness/runtime/native_provider_relay.py#L63) | self, store, connections, selection, company_id, principal_id |  |
| [server_names](../harness/runtime/native_provider_relay.py#L103) | self |  |
| [providers](../harness/runtime/native_provider_relay.py#L106) | self |  |
| [_direct_identity](../harness/runtime/native_provider_relay.py#L108) | self, provider |  |
| [_direct_current](../harness/runtime/native_provider_relay.py#L116) | self, route |  |
| [display_name](../harness/runtime/native_provider_relay.py#L120) | self, server_name |  |
| [_current](../harness/runtime/native_provider_relay.py#L125) | self, name, expected |  |
| [grant](../harness/runtime/native_provider_relay.py#L144) | self, server_name |  |
| [valid](../harness/runtime/native_provider_relay.py#L146) | self, grant |  |
| [tools](../harness/runtime/native_provider_relay.py#L151) | self, grant |  |
| [call](../harness/runtime/native_provider_relay.py#L160) | self, grant, name, arguments, metadata, cancelled, alive |  |
| [configure_writes](../harness/runtime/native_provider_relay.py#L177) | self, approvals, scope, enabled, timeout | Host commissioning seam; selecting read_write alone does not enable it. |
| [operation_kind](../harness/runtime/native_provider_relay.py#L187) | self, grant, name |  |
| [prepare_write](../harness/runtime/native_provider_relay.py#L194) | self, server, name |  |
| [approval_binding](../harness/runtime/native_provider_relay.py#L210) | self, server, name |  |
| [_authority_admission](../harness/runtime/native_provider_relay.py#L214) | self, server_name |  |
| [write_admission](../harness/runtime/native_provider_relay.py#L227) | self, binding |  |
| [write_credentials](../harness/runtime/native_provider_relay.py#L236) | self, binding |  |
| [write_recheck](../harness/runtime/native_provider_relay.py#L245) | self, binding |  |
| [prompt_policy](../harness/runtime/native_provider_relay.py#L260) | self, grant |  |
| [provenance](../harness/runtime/native_provider_relay.py#L271) | self, server_name | Host identity for provider artifacts; result fields supply no authority. |
| [artifact_admission](../harness/runtime/native_provider_relay.py#L284) | self, server_name, expected_provenance | Keep the package/account lease while persisting a provider result. |
| [current](../harness/runtime/native_provider_relay.py#L296) |  |  |

### harness/runtime/native_provider_write.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__post_init__](../harness/runtime/native_provider_write.py#L42) | self |  |
| [_drain](../harness/runtime/native_provider_write.py#L49) | task |  |
| [_offload](../harness/runtime/native_provider_write.py#L63) | function, *args |  |
| [__init__](../harness/runtime/native_provider_write.py#L73) | self, inner, prepared, arguments, claim, alive |  |
| [handle_async_request](../harness/runtime/native_provider_write.py#L80) | self, request |  |
| [aclose](../harness/runtime/native_provider_write.py#L119) | self |  |
| [__init__](../harness/runtime/native_provider_write.py#L132) | self, store, scope, prepare, admission, credentials, enabled, timeout, max_calls, transport_factory, recheck |  |
| [_transport](../harness/runtime/native_provider_write.py#L151) | binding |  |
| [_path](../harness/runtime/native_provider_write.py#L154) | self, request_id |  |
| [_save](../harness/runtime/native_provider_write.py#L159) | self, row, binding, result |  |
| [_saved](../harness/runtime/native_provider_write.py#L182) | self, row, binding |  |
| [execute](../harness/runtime/native_provider_write.py#L198) | self, server, tool, arguments, metadata, cancelled, alive |  |
| [active](../harness/runtime/native_provider_write.py#L204) |  |  |
| [_execute](../harness/runtime/native_provider_write.py#L219) | self, server, tool, arguments, metadata, cancelled, alive |  |
| [deny_reference](../harness/runtime/native_provider_write.py#L230) | uri |  |
| [claim](../harness/runtime/native_provider_write.py#L241) |  |  |
| [recover_saved_result](../harness/runtime/native_provider_write.py#L280) | self, request_id, binding | Host reconciliation under the original runtime scope; no network I/O. |
| [close](../harness/runtime/native_provider_write.py#L289) | self |  |

### harness/runtime/native_questions.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_expires](../harness/runtime/native_questions.py#L42) | row |  |
| [_now](../harness/runtime/native_questions.py#L48) |  |  |
| [_identity](../harness/runtime/native_questions.py#L52) | value |  |
| [_native_key](../harness/runtime/native_questions.py#L58) | value |  |
| [__init__](../harness/runtime/native_questions.py#L66) | self, state |  |
| [_db](../harness/runtime/native_questions.py#L83) | self |  |
| [_public](../harness/runtime/native_questions.py#L99) | row |  |
| [open](../harness/runtime/native_questions.py#L106) | self, root_chat_id, actor_chat_id, owner, generation, native_request_id, params, actor_title, transport |  |
| [open_host](../harness/runtime/native_questions.py#L152) | self, arguments, root_chat_id, owner, generation |  |
| [host_request](../harness/runtime/native_questions.py#L174) | self, request_id, owner, root_chat_id |  |
| [_owned](../harness/runtime/native_questions.py#L179) | db, request_id, owner, root_chat_id, generation |  |
| [get](../harness/runtime/native_questions.py#L186) | self, request_id, owner, root_chat_id |  |
| [for_chat](../harness/runtime/native_questions.py#L190) | self, root_chat_id, owner |  |
| [interrupt](../harness/runtime/native_questions.py#L196) | self, request_id, owner, root_chat_id, reason | Reconcile a saved request after the host confirms its run has ended. |
| [_response](../harness/runtime/native_questions.py#L206) | row, action, answers |  |
| [answer](../harness/runtime/native_questions.py#L232) | self, request_id, owner, root_chat_id, generation, action, answers, deliver, cancelled |  |
| [expire](../harness/runtime/native_questions.py#L275) | self, owner, root_chat_id, generation, deliver, cancelled | Release expired native waits even when every browser is disconnected. |
| [_finish_delivery](../harness/runtime/native_questions.py#L289) | self, request_id, status, reason |  |
| [resolve_native](../harness/runtime/native_questions.py#L295) | self, root_chat_id, generation, native_request_id |  |
| [retire_generation](../harness/runtime/native_questions.py#L308) | self, root_chat_id, generation, reason |  |
| [recover](../harness/runtime/native_questions.py#L317) | self | Call once on bridge startup after its workers have been reconciled. |

### harness/runtime/native_skills.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_error](../harness/runtime/native_skills.py#L21) |  |  |
| [is_native_skill](../harness/runtime/native_skills.py#L22) | identifier |  |
| [_hash](../harness/runtime/native_skills.py#L23) | value |  |
| [__init__](../harness/runtime/native_skills.py#L26) | self, store |  |
| [_descriptors](../harness/runtime/native_skills.py#L30) | self, principal_id |  |
| [original](../harness/runtime/native_skills.py#L38) | path |  |
| [list](../harness/runtime/native_skills.py#L73) | self, principal_id |  |
| [resolve](../harness/runtime/native_skills.py#L77) | self, identifiers, principal_id |  |
| [current](../harness/runtime/native_skills.py#L84) | self, selection, principal_id |  |
| [inputs](../harness/runtime/native_skills.py#L94) | self, identifiers, principal_id, selection, connection, cancelled |  |
| [native_skill_inputs](../harness/runtime/native_skills.py#L120) | agent, resolved, run |  |
| [delivery_guard](../harness/runtime/native_skills.py#L129) |  |  |

### harness/runtime/openai_gateway.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_private_json](../harness/runtime/openai_gateway.py#L68) | path, value |  |
| [_integer](../harness/runtime/openai_gateway.py#L77) | value, minimum, maximum |  |
| [_input_bound](../harness/runtime/openai_gateway.py#L83) | value | Conservative local estimate; keep source images intact, charge patches. |
| [visit](../harness/runtime/openai_gateway.py#L91) | item |  |
| [_has_opaque](../harness/runtime/openai_gateway.py#L138) | value |  |
| [_price_admission](../harness/runtime/openai_gateway.py#L144) | bound, output, web, evidence |  |
| [_client_tool_search](../harness/runtime/openai_gateway.py#L154) | item, output |  |
| [prepare_request](../harness/runtime/openai_gateway.py#L168) | body, max_output_tokens, allow_web_search, allow_native_tool_search |  |
| [flatten](../harness/runtime/openai_gateway.py#L197) | items, depth |  |
| [prepare_compaction](../harness/runtime/openai_gateway.py#L255) | body, allow_native_tool_search |  |
| [usage_receipt](../harness/runtime/openai_gateway.py#L270) | response, request_id, reservation_id, pool_scope, parent_scope, admission |  |
| [capture_signals](../harness/runtime/openai_gateway.py#L316) | self |  |
| [__init__](../harness/runtime/openai_gateway.py#L322) | self, state, api_key, run_id, pool, transport, max_output_tokens, allow_web_search, maximum_run_usd, maximum_requests, unix_socket, allow_native_tool_search |  |
| [cli_config](../harness/runtime/openai_gateway.py#L360) | self |  |
| [__aenter__](../harness/runtime/openai_gateway.py#L370) | self |  |
| [__aexit__](../harness/runtime/openai_gateway.py#L401) | self, *exc |  |
| [revoke](../harness/runtime/openai_gateway.py#L420) | self | Immediately close admission before stopping the entire native tree. |
| [_error](../harness/runtime/openai_gateway.py#L425) | self, message, status |  |
| [_run_reserve](../harness/runtime/openai_gateway.py#L428) | self, request_id, amount |  |
| [_run_settle](../harness/runtime/openai_gateway.py#L436) | self, request_id, amount |  |
| [_admission_headroom](../harness/runtime/openai_gateway.py#L440) | self | A preflight hint only; the subsequent reservations enforce races. |
| [_finish](../harness/runtime/openai_gateway.py#L450) | self, response, request_id, reservation_id, admission |  |
| [_count_input](../harness/runtime/openai_gateway.py#L466) | self, body, admission, request_id |  |
| [handle](../harness/runtime/openai_gateway.py#L493) | self, request |  |
| [stream](../harness/runtime/openai_gateway.py#L578) |  |  |

### harness/runtime/plugin_catalogue.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_documentation_candidate](../harness/runtime/plugin_catalogue.py#L34) | value |  |
| [_source_url](../harness/runtime/plugin_catalogue.py#L48) | path, revision, repository |  |
| [_instruction_evidence](../harness/runtime/plugin_catalogue.py#L52) | source, path, revision, repository | Retain links and authentication mentions, never an executable instruction body. |
| [_mcp_auth](../harness/runtime/plugin_catalogue.py#L67) | details | Describe declared transport setup, without storing credential values. |
| [_connection_setup](../harness/runtime/plugin_catalogue.py#L99) | row, root, paths, revision, fetch, repository |  |
| [_https](../harness/runtime/plugin_catalogue.py#L155) | value |  |
| [_child](../harness/runtime/plugin_catalogue.py#L164) | root, value | Resolve a published relative path inside its own plugin package. |
| [_strings](../harness/runtime/plugin_catalogue.py#L174) | value |  |
| [_skill](../harness/runtime/plugin_catalogue.py#L180) | path, revision, fetch, repository |  |
| [_populate_entry](../harness/runtime/plugin_catalogue.py#L201) | row, root, paths, revision, fetch, repository |  |
| [build_catalogue](../harness/runtime/plugin_catalogue.py#L266) | revision, tree, fetch | Build deterministically from a fixed Git tree and a public-file reader. |
| [read_entry](../harness/runtime/plugin_catalogue.py#L284) | entry |  |
| [materialize_external](../harness/runtime/plugin_catalogue.py#L315) | snapshot, pins, fetch_archive | Resolve reviewed public package pins during refresh, never during serving. |
| [fetch](../harness/runtime/plugin_catalogue.py#L360) | path, limit |  |
| [_snapshot](../harness/runtime/plugin_catalogue.py#L399) |  |  |
| [catalogue](../harness/runtime/plugin_catalogue.py#L406) |  | Return public reference data; connections and installation grants are separate. |
| [read_plugin](../harness/runtime/plugin_catalogue.py#L411) | identifier |  |
| [refresh](../harness/runtime/plugin_catalogue.py#L418) | revision, output, external_pins |  |
| [get](../harness/runtime/plugin_catalogue.py#L422) | url, limit |  |

### harness/runtime/plugin_routes.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_deny](../harness/runtime/plugin_routes.py#L39) | status, code |  |
| [_offload](../harness/runtime/plugin_routes.py#L43) | function, *args, **kwargs |  |
| [_run_store](../harness/runtime/plugin_routes.py#L58) | method, *args, **kwargs |  |
| [invoke](../harness/runtime/plugin_routes.py#L59) |  |  |
| [_admitted](../harness/runtime/plugin_routes.py#L66) |  |  |
| [_header](../harness/runtime/plugin_routes.py#L72) | request, name |  |
| [_identity](../harness/runtime/plugin_routes.py#L78) | request, write |  |
| [_empty_body](../harness/runtime/plugin_routes.py#L98) | request, required |  |
| [_plugin_id](../harness/runtime/plugin_routes.py#L123) | identifier |  |
| [_installable](../harness/runtime/plugin_routes.py#L128) | store |  |
| [_private_fd](../harness/runtime/plugin_routes.py#L139) | path |  |
| [__init__](../harness/runtime/plugin_routes.py#L151) | self, store |  |
| [_db](../harness/runtime/plugin_routes.py#L159) | self |  |
| [_owner](../harness/runtime/plugin_routes.py#L166) | principal |  |
| [list](../harness/runtime/plugin_routes.py#L168) | self, principal |  |
| [begin](../harness/runtime/plugin_routes.py#L172) | self, principal, plugin_id |  |
| [clear](../harness/runtime/plugin_routes.py#L182) | self, principal, plugin_id |  |
| [lock](../harness/runtime/plugin_routes.py#L186) | self |  |
| [_mutation](../harness/runtime/plugin_routes.py#L197) | journal |  |
| [register_plugin_routes](../harness/runtime/plugin_routes.py#L205) | app, store_for_workspace, installation_ready, installation_capabilities, revoke_plugin | Host callbacks receive only its authenticated request.state.workspace. |
| [context](../harness/runtime/plugin_routes.py#L219) | request, write |  |
| [ready](../harness/runtime/plugin_routes.py#L230) | selected |  |
| [capabilities](../harness/runtime/plugin_routes.py#L235) | selected, principal, store |  |
| [installed](../harness/runtime/plugin_routes.py#L253) | request |  |
| [install](../harness/runtime/plugin_routes.py#L265) | plugin_id, request |  |
| [remove](../harness/runtime/plugin_routes.py#L286) | plugin_id, request |  |

### harness/runtime/provider_tool_policy.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [provider_prompt_policy](../harness/runtime/provider_tool_policy.py#L3) | tool_effects | Host effect classification tunes provider prompts without rewriting schemas. |

### harness/sdk/agent_inputs.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [validate_schedule](../harness/sdk/agent_inputs.py#L33) | self |  |
| [attach](../harness/sdk/agent_inputs.py#L66) | self, store |  |
| [normalize](../harness/sdk/agent_inputs.py#L69) | self, record, table |  |
| [collection_allowed](../harness/sdk/agent_inputs.py#L79) | self, spec, datasets, owner |  |
| [validate_definition](../harness/sdk/agent_inputs.py#L82) | self, spec |  |
| [definition_context](../harness/sdk/agent_inputs.py#L86) | self, agent, chat_id, arguments |  |
| [prepare_record](../harness/sdk/agent_inputs.py#L89) | self, record, context |  |
| [describe](../harness/sdk/agent_inputs.py#L92) | self, record, db |  |
| [runnable](../harness/sdk/agent_inputs.py#L95) | self, record |  |
| [validate_activation](../harness/sdk/agent_inputs.py#L99) | self, record |  |
| [resource_ceiling](../harness/sdk/agent_inputs.py#L102) | self |  |
| [resource_allowance](../harness/sdk/agent_inputs.py#L105) | self, definition |  |
| [validate_resource_budget](../harness/sdk/agent_inputs.py#L108) | self, definition, runs |  |
| [resource_admitted](../harness/sdk/agent_inputs.py#L112) | self, run |  |
| [validate_wake](../harness/sdk/agent_inputs.py#L115) | self, wake, definition |  |
| [recovered](../harness/sdk/agent_inputs.py#L118) | self, db, run |  |
| [claimed](../harness/sdk/agent_inputs.py#L121) | self, db, record, run |  |
| [finished](../harness/sdk/agent_inputs.py#L124) | self, db, run, status |  |
| [refresh](../harness/sdk/agent_inputs.py#L127) | self, definitions |  |
| [ready](../harness/sdk/agent_inputs.py#L130) | self, definition, wake, agent, input_optional |  |
| [prepare](../harness/sdk/agent_inputs.py#L133) | self, definition, wake, agent |  |
| [select](../harness/sdk/agent_inputs.py#L136) | self, db, record, sources, source_records, screening, now, wake |  |
| [execution](../harness/sdk/agent_inputs.py#L142) | self, definition |  |
| [recurring_ready](../harness/sdk/agent_inputs.py#L147) | self, collection, principal |  |
| [context](../harness/sdk/agent_inputs.py#L151) | self, agent, run, snapshot |  |

### harness/sdk/capability_contract.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [selection](../harness/sdk/capability_contract.py#L8) | value | Undeclared capabilities remain disabled; settings contain only booleans. |

### harness/sdk/display_presentation.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [extend_kit](../harness/sdk/display_presentation.py#L28) | extension | Merge a vertical's authored kit additions over the shared kit, into a fresh document. |
| [merge](../harness/sdk/display_presentation.py#L30) | base, change |  |
| [__init__](../harness/sdk/display_presentation.py#L43) | self, problem |  |
| [listed](../harness/sdk/display_presentation.py#L47) | names |  |
| [_fields](../harness/sdk/display_presentation.py#L50) | schema |  |
| [build_schema](../harness/sdk/display_presentation.py#L53) | kit | The JSON Schema of a presentation, built from the kit. |
| [_number](../harness/sdk/display_presentation.py#L93) | value |  |
| [_text](../harness/sdk/display_presentation.py#L96) | value |  |
| [_records](../harness/sdk/display_presentation.py#L99) | value, each, least, most |  |
| [_row](../harness/sdk/display_presentation.py#L103) | item |  |
| [holds](../harness/sdk/display_presentation.py#L106) | value | What a field holds, in words a sentence can carry. |
| [bound](../harness/sdk/display_presentation.py#L122) | document, name, shape | The value a binding reads: the output's field of that name; for text, also a written text slot. |
| [short](../harness/sdk/display_presentation.py#L132) | text, most | Text within `most` characters, ending on its last whole word there. |
| [inert](../harness/sdk/display_presentation.py#L140) | text | Text a script wrote, as the page draws it: a link's own words stay and its address goes. |
| [_inert_field](../harness/sdk/display_presentation.py#L144) | value |  |
| [_own_list](../harness/sdk/display_presentation.py#L153) | value, fields | A list a script wrote, as the kit's own fields of each entry: text, numbers and times. |
| [__init__](../harness/sdk/display_presentation.py#L172) | self, kit, shapes, aliases, envelope, trusted_lists, row_fields, views, default_label |  |
| [output_fields](../harness/sdk/display_presentation.py#L189) | self, tile, canvas | The fields of a display's output a presentation can bind, each with the kit shapes it fits. |
| [_problem](../harness/sdk/display_presentation.py#L196) | self, block, field, name, shape, needs, document, value, fixed |  |
| [check_output](../harness/sdk/display_presentation.py#L208) | self, spec, tile, canvas | Each binding of a presentation that the output leaves unfilled: [{block, field, bound_to, shape, needs, sentence}]. |
| [family_blocks](../harness/sdk/display_presentation.py#L243) | self, family, canvas | A family's own blocks. With an output at hand, the ones its fields can fill join them. |
| [default_presentation](../harness/sdk/display_presentation.py#L262) | self, display, output | The presentation a display has before one is saved: its label, a line of its series, a count, and the canvas family its definition names. |
| [merge_presentation](../harness/sdk/display_presentation.py#L270) | self, saved, change, output | A saved presentation with a change of its tile, its canvas or both. A part replaces whole. A canvas named by its family alone takes that family's own blocks. |
| [_named](../harness/sdk/display_presentation.py#L280) | self, value, most |  |
| [validate_presentation](../harness/sdk/display_presentation.py#L283) | self, spec, output, parts | A presentation that the kit and, with `output`, the display's current output can draw. |
| [families_for](../harness/sdk/display_presentation.py#L378) | self, output | The kit's families for one output: each with its sentence, and whether the output's fields fill the family's own blocks. |
| [_unit](../harness/sdk/display_presentation.py#L392) | self, reading, spec | The unit a reading carries on the page. A rate above 1 is the percentage itself: it reads with `%`, whatever unit came with it. A rate from 0 to 1 is a ratio and reads as one, unless its script published it with `%`. |
| [_fraction](../harness/sdk/display_presentation.py#L405) | self, canvas, spec |  |
| [_tile_problems](../harness/sdk/display_presentation.py#L410) | self, reading, canvas, spec, series | Each binding of the tile that this reading leaves unfilled, as the page carries it. |
| [canvas_for_page](../harness/sdk/display_presentation.py#L416) | self, canvas, spec | A canvas as the page reads it: the published fields, the text a script wrote made inert, a list a script wrote whole cut to the kit's own fields, the presentation's family and blocks, and each binding the output leaves unfilled. |
| [apply_to_tile](../harness/sdk/display_presentation.py#L441) | self, row, spec, canvas, agent_id | A company display's tile row with its presentation applied: the names the workspace reads. |
| [revise](../harness/sdk/display_presentation.py#L479) | self, current, change, output, expected_revision, saved_by, saved_at | Validate a change and advance its revision inside the adapter's write transaction. |
| [display](../harness/sdk/display_presentation.py#L488) | self, display_id, owner_agent_id, output, presentation | Project an admitted output, with one explicit owning agent, into its tile and canvas. |

### harness/sdk/display_runs.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [canonical](../harness/sdk/display_runs.py#L30) | value |  |
| [iso](../harness/sdk/display_runs.py#L33) | epoch |  |
| [clean_policy](../harness/sdk/display_runs.py#L36) | value | Validate the shared cadence and bounded runtime policy. |
| [__init__](../harness/sdk/display_runs.py#L81) | self, state, clock, filename, names, policy, keep_runs, scope_field, run_prefix |  |
| [execute](../harness/sdk/display_runs.py#L94) | self, db, statement, values |  |
| [initialize](../harness/sdk/display_runs.py#L97) | self, db |  |
| [connect](../harness/sdk/display_runs.py#L104) | self, write |  |
| [_schedule](../harness/sdk/display_runs.py#L129) | self, db, key |  |
| [_held](../harness/sdk/display_runs.py#L132) | self, db, key |  |
| [state](../harness/sdk/display_runs.py#L139) | self, owner, collection, scope_id, now | The scope’s schedule as the probe and the tools read it. |
| [policy](../harness/sdk/display_runs.py#L155) | self, owner, collection, scope_id |  |
| [set_policy](../harness/sdk/display_runs.py#L159) | self, owner, collection, scope_id, changes, expected_revision | Change the scope’s run policy. `expected_revision` is the revision the caller read. |
| [request](../harness/sdk/display_runs.py#L171) | self, owner, collection, scope_id, by, only | Ask for a pass now. Requests made before the pass starts become that one pass. |
| [claim](../harness/sdk/display_runs.py#L180) | self, owner, collection, scope_id, trigger, stamp, day, now, lease_seconds | Take the scope’s lease and open a run row. None while another pass holds the lease. |
| [_expire](../harness/sdk/display_runs.py#L204) | self, db, key, row, now | Close the run of a lease that ran out and free the scope. |
| [reap](../harness/sdk/display_runs.py#L222) | self, owner, collection, scope_id, now | Close a pass whose lease ran out, so the probe reads the scope as it now stands. True when it closed one. |
| [renew](../harness/sdk/display_runs.py#L237) | self, run_id, lease_token, lease_seconds, now | Extend a lease its holder still has. False once the lease has moved on. |
| [finish](../harness/sdk/display_runs.py#L244) | self, run_id, lease_token, status, stamp, day, period, derived, outputs, errors, skipped, scripts, wall_ms, error, published, reread, now | Close a run row and free its lease. A completed pass that names its `stamp` records that stamp and `day` as processed. A failed pass backs off and leaves what was processed as it is. `reread` says the run stored outputs of another reading than the scope’s own (a chosen day from a host command): the next probe then runs the scope’s whole pass. |
| [_public](../harness/sdk/display_runs.py#L287) | self, row | A run as the tools and the page read it: no principal, no stamp, no file path. |
| [record](../harness/sdk/display_runs.py#L301) | self, owner, collection, scope_id, trigger, status, started_at, wall_ms, period, scripts, error | Write one closed run row beside the passes: a script's test. It holds no lease and leaves the scope’s schedule, its failures and its waits as they are. A display keeps its newest KEEP_TEST_RUNS test rows, so tests leave the scope’s pass rows in place. |
| [forget_display](../harness/sdk/display_runs.py#L322) | self, owner, collection, scope_id, key | Take a removed display out of the scope’s run history: its tests go, and each pass row loses the display's entries. A display added later under the same key starts with an empty history. |
| [job_open](../harness/sdk/display_runs.py#L345) | self, job, owner, collection, scope_id, display_id | Note a sandbox job before the broker hears of it: {'request_id', 'scope'}. |
| [job_close](../harness/sdk/display_runs.py#L351) | self, job | The broker confirmed the job released. |
| [jobs_pending](../harness/sdk/display_runs.py#L356) | self | Sandbox jobs a stopped process left open: [{'request_id', 'scope'}]. |
| [runs](../harness/sdk/display_runs.py#L367) | self, owner, collection, scope_id, limit | The scope’s runs, newest first. |
| [last_run](../harness/sdk/display_runs.py#L376) | self, owner, scope_id | The owner's newest pass, of one scope when it is named. A script's test is a row of the history and stays out of this: it is one display's test, and the scope’s pass stands. |
| [due_reading](../harness/sdk/display_runs.py#L388) | row, stamp, day, now, inputs_ready, daily_ready | One declared input reading through manual, changed-input and daily cadence gates. |

### harness/sdk/display_scripts.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/sdk/display_scripts.py#L54) | self, code, message, line |  |
| [public](../harness/sdk/display_scripts.py#L58) | self |  |
| [validate_source](../harness/sdk/display_scripts.py#L61) | text, filename, max_bytes | A script's source, checked as text: size, encoding, syntax and one top-level `def run(input)`. |
| [__init__](../harness/sdk/display_scripts.py#L101) | self, directory |  |
| [start](../harness/sdk/display_scripts.py#L105) | self |  |
| [_refuse](../harness/sdk/display_scripts.py#L126) | self, reader, writer |  |
| [close](../harness/sdk/display_scripts.py#L149) | self |  |
| [_drain](../harness/sdk/display_scripts.py#L165) | task | Cleanup keeps its owner through a caller's cancellation. |
| [__init__](../harness/sdk/display_scripts.py#L187) | self, path, clock, limits |  |
| [_connect](../harness/sdk/display_scripts.py#L192) | self |  |
| [numbers](../harness/sdk/display_scripts.py#L201) | self, company_id | {'host', 'company'}: jobs in the last 24 hours; 'total': every job this host's service took. |
| [refused](../harness/sdk/display_scripts.py#L217) | self, company_id, retained | The fault code that keeps one more job of this company out now, else None. `retained` says the broker's retention upgrade is installed, which the host states with its event-runs switch. |
| [count](../harness/sdk/display_scripts.py#L230) | self, company_id | Count one job. Returns the mark `uncount` takes. |
| [uncount](../harness/sdk/display_scripts.py#L247) | self, mark | Take back the count of a job the broker refused. |
| [__init__](../harness/sdk/display_scripts.py#L274) | self, contract, enabled, event_runs, client, runtime, socket_factory, poll_seconds, busy_waits, job_seconds, slot_wait, counts, clock, loop |  |
| [client](../harness/sdk/display_scripts.py#L285) | self |  |
| [runtime](../harness/sdk/display_scripts.py#L292) | self |  |
| [available](../harness/sdk/display_scripts.py#L299) | self, company_id, owner | Whether the broker of this host is the commissioned one: same profile, image and worker. |
| [_turn](../harness/sdk/display_scripts.py#L315) | self, company_id, wait | Take the service's sandbox turn for a company. False when the turn is another company's or stays held for the whole wait. |
| [run](../harness/sdk/display_scripts.py#L343) | self, company_id, owner, collection, display_id, revision, source, document, cancelled, opened, closed, wait_seconds, seconds | One job. Returns {status: 'succeeded', results, log, seconds, broker_run_id, input_sha256, input_bytes}, or {status: 'failed' / 'unavailable', error: {code, message, …}, seconds}. `started` says whether the broker holds a row for it: such a job counts against the day's numbers, and a job the broker refused or never heard of counts for nothing. |
| [_uncount](../harness/sdk/display_scripts.py#L415) | self, mark |  |
| [_job](../harness/sdk/display_scripts.py#L421) | self, scope, request_id, snapshot, cancelled, state, job_seconds |  |
| [_clear](../harness/sdk/display_scripts.py#L467) | self, scope, request_id, state | Stop and release the job, whatever happened. True once the broker confirmed it. |
| [recover](../harness/sdk/display_scripts.py#L483) | self, pending, closed | Clear jobs a stopped process left: [{'request_id', 'scope'}]. Returns the request ids cleared. |

### harness/sdk/host.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/sdk/host.py#L11) | self, current, bind, model_context, resource, history_scope |  |
| [current](../harness/sdk/host.py#L18) | self |  |
| [bind](../harness/sdk/host.py#L25) | self |  |
| [__init__](../harness/sdk/host.py#L34) | self |  |
| [register](../harness/sdk/host.py#L38) | self, provider |  |
| [seal](../harness/sdk/host.py#L43) | self |  |
| [list](../harness/sdk/host.py#L46) | self, principal |  |
| [contains](../harness/sdk/host.py#L52) | self, collection, principal |  |
| [__init__](../harness/sdk/host.py#L71) | self, selected |  |
| [read_admission](../harness/sdk/host.py#L74) | self, actor, collection |  |
| [current](../harness/sdk/host.py#L80) |  |  |
| [tool_context](../harness/sdk/host.py#L85) | self, context |  |
| [result_fields](../harness/sdk/host.py#L88) | self, name, content, success |  |
| [status_fields](../harness/sdk/host.py#L91) | self |  |
| [budget_fields](../harness/sdk/host.py#L94) | self |  |
| [member_cards](../harness/sdk/host.py#L97) | self, actor, collection, rows |  |
| [business_fields](../harness/sdk/host.py#L100) | self, actor, collection, value |  |
| [participant_delivery_current](../harness/sdk/host.py#L103) | self, chat_id |  |
| [provider_usage](../harness/sdk/host.py#L106) | self |  |
| [available_credit](../harness/sdk/host.py#L109) | self |  |
| [agent_capabilities](../harness/sdk/host.py#L112) | self |  |
| [validate_activation](../harness/sdk/host.py#L115) | self, definition, once |  |
| [usage_fields](../harness/sdk/host.py#L118) | self |  |
| [collection_names](../harness/sdk/host.py#L121) | self, principal |  |
| [catalogue](../harness/sdk/host.py#L124) | self |  |
| [draft_agent](../harness/sdk/host.py#L127) | self, template_id, collection, principal |  |
| [authorize_file](../harness/sdk/host.py#L130) | self, request, file_id, principal |  |
| [file_download](../harness/sdk/host.py#L134) | self, record, principal |  |
| [tick](../harness/sdk/host.py#L137) | self |  |
| [close](../harness/sdk/host.py#L140) | self |  |
| [connector_details](../harness/sdk/host.py#L143) | self, saved, connector_id, owner, collection |  |
| [connection_fields](../harness/sdk/host.py#L146) | self, value, principal, request |  |
| [source_options](../harness/sdk/host.py#L149) | self, principal, collection |  |
| [request_scope](../harness/sdk/host.py#L153) | self, request |  |
| [bare_lifespan](../harness/sdk/host.py#L158) | app, host |  |

### harness/sdk/job_recipes.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [ordered_steps](../harness/sdk/job_recipes.py#L51) | self |  |
| [_rows](../harness/sdk/job_recipes.py#L60) | reader, name, value, model, maximum |  |
| [load_jobs](../harness/sdk/job_recipes.py#L78) | reader, recipes, roles, classes, chats | Read exact vertical instruction bytes and validate cross-references once. |
| [launcher_for](../harness/sdk/job_recipes.py#L108) | agent, chat_id | Only host-confirmed fixed purposes select an Organization recipe. |
| [available](../harness/sdk/job_recipes.py#L120) | vertical, launcher |  |
| [instructions_for](../harness/sdk/job_recipes.py#L124) | agent, chat_id, vertical |  |

### harness/sdk/layers.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [modules](../harness/sdk/layers.py#L30) | root | Active flat modules and package files; tests and frozen deployment closures stay outside. |
| [_ownership](../harness/sdk/layers.py#L47) | root |  |
| [_named](../harness/sdk/layers.py#L74) | node | The module a call imports by a literal name: import_module('a.b') or __import__('a.b'). |
| [imports](../harness/sdk/layers.py#L84) | root | What each module imports from the other modules of the directory, read with ast. |
| [crossings](../harness/sdk/layers.py#L109) | graph, layer | The imports from layers 1 and 2 into layer 3 that a graph holds. |
| [coupling](../harness/sdk/layers.py#L122) | graph, layer | Measured numbers: modules per layer and imports per pair of layers ('2>3' reads 2 imports 3). |
| [check](../harness/sdk/layers.py#L140) | root, layer, recorded, graph | Every way the tree and this map disagree, as sentences. An empty list is a green ratchet. |
| [by_layer](../harness/sdk/layers.py#L168) |  | {layer: {what the modules do: (module, ...)}}, for the documents and the self-description. |
| [main](../harness/sdk/layers.py#L174) |  |  |

### harness/sdk/pack.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_need](../harness/sdk/pack.py#L142) | condition, message |  |
| [_listed](../harness/sdk/pack.py#L147) | names, last |  |
| [_object](../harness/sdk/pack.py#L152) | where, value, required, optional |  |
| [_text](../harness/sdk/pack.py#L161) | where, value, maximum |  |
| [_match](../harness/sdk/pack.py#L167) | where, value, pattern, shape |  |
| [_choice](../harness/sdk/pack.py#L172) | where, value, choices |  |
| [_rows](../harness/sdk/pack.py#L177) | where, value, minimum |  |
| [_unique](../harness/sdk/pack.py#L183) | where, values, noun |  |
| [_pairs](../harness/sdk/pack.py#L190) | pairs |  |
| [_constant](../harness/sdk/pack.py#L196) | name |  |
| [_parse](../harness/sdk/pack.py#L200) | where, data |  |
| [_plain](../harness/sdk/pack.py#L210) | char | A printing character, a line feed or a tab. |
| [_bytes](../harness/sdk/pack.py#L215) | where, path, limit | The bytes of one regular file that has a single name on disk and fits its size. |
| [__init__](../harness/sdk/pack.py#L240) | self, root |  |
| [read](../harness/sdk/pack.py#L244) | self, where, relative, suffix, bounds, limit |  |
| [text](../harness/sdk/pack.py#L259) | self, where, relative |  |
| [data](../harness/sdk/pack.py#L275) | self, where, relative, bounds |  |
| [_skill](../harness/sdk/pack.py#L280) | where, value, skill_ids |  |
| [_fixed_chats](../harness/sdk/pack.py#L286) | reader, rows, skill_ids |  |
| [_agent_classes](../harness/sdk/pack.py#L310) | rows |  |
| [section_slug](../harness/sdk/pack.py#L346) | name | A section name as the sidebar keys it: lowercase letters and digits, every other run a dash. |
| [_tile_sets](../harness/sdk/pack.py#L351) | reader, rows |  |
| [_vocabulary](../harness/sdk/pack.py#L381) | reader, value, parsed |  |
| [_strings](../harness/sdk/pack.py#L418) | where, value, pattern, shape |  |
| [_seed_connections](../harness/sdk/pack.py#L422) | where, value | The connections a seed needs: up to eight providers, each with its read scopes. |
| [_skills](../harness/sdk/pack.py#L438) | reader, value |  |
| [_templates](../harness/sdk/pack.py#L472) | reader, where, value, skill_ids |  |
| [_ready_made](../harness/sdk/pack.py#L523) | rows, classes, types | Each ready-made agent on offer takes an input of its class and reads event types of this vertical. |
| [_capabilities](../harness/sdk/pack.py#L538) | reader, value | The vertical's rows of the table of what works: rows of its own, and sentences for a harness row. |
| [_surfaces](../harness/sdk/pack.py#L575) | rows |  |
| [_connections](../harness/sdk/pack.py#L598) | rows, skill_ids |  |
| [_data_sources](../harness/sdk/pack.py#L613) | rows, skill_ids |  |
| [_wake_sources](../harness/sdk/pack.py#L629) | rows |  |
| [_flow](../harness/sdk/pack.py#L641) | rows |  |
| [manifest_path](../harness/sdk/pack.py#L672) | self |  |
| [product](../harness/sdk/pack.py#L676) | self |  |
| [prompt](../harness/sdk/pack.py#L679) | self, name | The text of 'system' or 'fixed_chat_common', exactly as its file holds it. |
| [fixed_chats](../harness/sdk/pack.py#L686) | self |  |
| [purposes](../harness/sdk/pack.py#L689) | self | {purpose: title} in the vertical's order. |
| [choose_purpose](../harness/sdk/pack.py#L693) | self |  |
| [fixed_chat](../harness/sdk/pack.py#L696) | self, purpose |  |
| [fixed_chat_text](../harness/sdk/pack.py#L702) | self, purpose | The standing instruction of one fixed chat by itself; None for a chat that carries the developer prompt alone. |
| [fixed_chat_prompt](../harness/sdk/pack.py#L707) | self, purpose | What a fixed chat adds to the developer prompt: the shared prefix, a newline, its own text. |
| [agent_classes](../harness/sdk/pack.py#L716) | self |  |
| [kinds](../harness/sdk/pack.py#L719) | self |  |
| [agent_class](../harness/sdk/pack.py#L722) | self, kind |  |
| [default_kind](../harness/sdk/pack.py#L728) | self |  |
| [authority](../harness/sdk/pack.py#L731) | self, kind |  |
| [tile_sets](../harness/sdk/pack.py#L735) | self |  |
| [tile_set_path](../harness/sdk/pack.py#L738) | self, tile_set_id |  |
| [tile_set](../harness/sdk/pack.py#L745) | self, tile_set_id | The tile_set file, parsed, as it was read when the vertical loaded. |
| [vocabulary](../harness/sdk/pack.py#L755) | self | {'groups': [...], 'types': {event type: entry}}; empty for a vertical that declares zero event types. |
| [recipes](../harness/sdk/pack.py#L762) | self | Complete jobs with declared steps and completion criteria. |
| [recipe](../harness/sdk/pack.py#L766) | self, recipe_id |  |
| [sub_agents](../harness/sdk/pack.py#L772) | self |  |
| [sub_agent](../harness/sdk/pack.py#L775) | self, role_id |  |
| [skills](../harness/sdk/pack.py#L782) | self | The skill seeds of a new company: id, name, description, instructions, required tools and connections. |
| [ready_agents](../harness/sdk/pack.py#L786) | self | The ready-made agents the vertical offers (`ready_agents`). |
| [retired_ready_agents](../harness/sdk/pack.py#L790) | self | Templates kept readable for the conversations that were started from them. |
| [import_host](../harness/sdk/pack.py#L797) | self | Load the explicitly declared composition module from this vertical's folder. |
| [tool_families](../harness/sdk/pack.py#L820) | self |  |
| [import_tool_families](../harness/sdk/pack.py#L823) | self | Import declared families only from this vertical's own module tree. |
| [tool_references](../harness/sdk/pack.py#L849) | self | Every (place, tool name) the manifest relies on outside its skills. |
| [check_tools](../harness/sdk/pack.py#L859) | self, registered_names | The tool names of the manifest that a registry lacks, as sentences. Empty means every name is registered. |
| [check_tile_sets](../harness/sdk/pack.py#L870) | self, tool_specs | What stands between each tile_set and its install, as sentences. Empty means every tile_set installs. |
| [skill_tool_gaps](../harness/sdk/pack.py#L899) | self, registered_names | {skill id: the required tools these names lack}, for each skill they hold back. |
| [surfaces](../harness/sdk/pack.py#L911) | self |  |
| [builtin_capabilities](../harness/sdk/pack.py#L914) | self |  |
| [connections_expected](../harness/sdk/pack.py#L917) | self |  |
| [data_sources](../harness/sdk/pack.py#L920) | self |  |
| [wake_sources](../harness/sdk/pack.py#L923) | self |  |
| [flow](../harness/sdk/pack.py#L926) | self |  |
| [demo](../harness/sdk/pack.py#L929) | self |  |
| [capabilities](../harness/sdk/pack.py#L932) | self | The vertical's rows of the table of what works: its own rows and its sentences for harness rows. |
| [shell](../harness/sdk/pack.py#L936) | self | What the web app needs to draw the sidebar and the pages (schema rocoto.harness-shell.v1). |
| [digest](../harness/sdk/pack.py#L956) | self | sha256 over the manifest and every file it names: one value for 'this exact template'. |
| [_folder](../harness/sdk/pack.py#L964) | source |  |
| [manifest_path](../harness/sdk/pack.py#L974) | root | Read the canonical manifest first; an invalid new file never selects an old one. |
| [_canonical_manifest](../harness/sdk/pack.py#L984) | raw |  |
| [load](../harness/sdk/pack.py#L1011) | source | Validate one vertical and read every file it names. A string is a folder name under verticals/; a Path is a folder. |
| [active](../harness/sdk/pack.py#L1077) |  | The vertical of this process, loaded on first use from the selected vertical and kept for its life. |
| [use](../harness/sdk/pack.py#L1092) | source | Serve another vertical for the length of a with block. For tests: one template per state directory (`bind`). |
| [_binding](../harness/sdk/pack.py#L1105) | path | The vertical id a state directory records, or None while the record is absent. |
| [_record](../harness/sdk/pack.py#L1130) | state, path, template_id | Write the record once and return the id on disk: this one, or the one another process wrote first. |
| [bind](../harness/sdk/pack.py#L1148) | state, template | Tie one company's state directory to the vertical of this process, and return that template. |
| [describe](../harness/sdk/pack.py#L1171) | template | A vertical in a dozen lines, for a person who is writing one. |
| [main](../harness/sdk/pack.py#L1194) | arguments |  |

### harness/sdk/tool_families.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [owner](../harness/sdk/tool_families.py#L40) | self |  |
| [dataset](../harness/sdk/tool_families.py#L44) | self |  |
| [require_current](../harness/sdk/tool_families.py#L47) | self |  |
| [require_parent](../harness/sdk/tool_families.py#L54) | self |  |
| [_offload](../harness/sdk/tool_families.py#L65) | function, *arguments | Retain admission until synchronous work finishes, including after cancellation. |
| [validate_families](../harness/sdk/tool_families.py#L81) | families, reserved_reads, reserved_writes | Validate the original family protocol without importing a vertical. |
| [__init__](../harness/sdk/tool_families.py#L112) | self, families |  |
| [names](../harness/sdk/tool_families.py#L131) | self, surface |  |
| [read_names](../harness/sdk/tool_families.py#L134) | self, surface |  |
| [specs](../harness/sdk/tool_families.py#L137) | self, write, surface |  |
| [family_of](../harness/sdk/tool_families.py#L143) | self, name |  |
| [declared](../harness/sdk/tool_families.py#L146) | self, name, arguments |  |
| [invoke](../harness/sdk/tool_families.py#L152) | self, context, name, arguments, surface |  |
| [build_registry](../harness/sdk/tool_families.py#L181) | agent, families, definition_model | Construct the common product plus exactly the selected vertical families. |
| [__init__](../harness/sdk/tool_families.py#L201) | self, family |  |
| [__getattr__](../harness/sdk/tool_families.py#L204) | self, name |  |
| [context](../harness/sdk/tool_families.py#L208) | context |  |

### harness/server.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [web_asset](../harness/server.py#L54) | relative | Resolve shared shell assets or the active vertical's own web assets. |
| [__init__](../harness/server.py#L65) | self, state, timeout, max_age, auth, agent, api_transport |  |
| [status](../harness/server.py#L72) | self |  |
| [create_app](../harness/server.py#L220) | state, index, messaging_provider_factory, phone_spend_factory, agent_factory, index_factory, read_agent_factory, managed_runtime_factory, builtin_provider_factories |  |
| [ready_workspace](../harness/server.py#L249) | selected |  |
| [recover_managed](../harness/server.py#L256) |  |  |
| [close_workspace](../harness/server.py#L264) | selected |  |
| [abandon_workspace](../harness/server.py#L282) | selected |  |
| [lifespan](../harness/server.py#L292) | app |  |
| [tick](../harness/server.py#L293) |  |  |
| [scope_member](../harness/server.py#L352) | selected, principal |  |
| [scope_members](../harness/server.py#L363) | selected |  |
| [install_scheduler](../harness/server.py#L371) | selected, environment_id |  |
| [phone_spending_ready](../harness/server.py#L449) |  |  |
| [phone_entry](../harness/server.py#L474) | chat_id, entry | Write a contact card or an alert into its Tracking Agent chat, replacing its earlier state. |
| [current_agent_authority](../harness/server.py#L520) | definition, actor |  |
| [current_signal_authority](../harness/server.py#L531) | signal |  |
| [workspace](../harness/server.py#L570) | environment |  |
| [services_for_environment](../harness/server.py#L596) | environment |  |
| [local_operator_only](../harness/server.py#L645) | request, call_next |  |
| [permitted](../harness/server.py#L723) | resources |  |
| [guarded_body](../harness/server.py#L738) |  |  |
| [connection_identity](../harness/server.py#L750) | request, writable |  |
| [messaging_member](../harness/server.py#L760) | selected, principal |  |
| [messaging_members](../harness/server.py#L771) | selected | The company's current owners and operators, the two roles a participant holds. |
| [messaging_authorized](../harness/server.py#L780) | selected, actor |  |
| [messaging_body](../harness/server.py#L804) | request, allowed, required |  |
| [organization_identity](../harness/server.py#L819) | request, collection, write |  |
| [messaging_actor](../harness/server.py#L830) | request, member_id, collection, write |  |
| [messaging_projection](../harness/server.py#L842) | request, member_id, collection |  |
| [organization_chats](../harness/server.py#L877) | request, collection |  |
| [organization_chat](../harness/server.py#L889) | request |  |
| [messaging_status](../harness/server.py#L903) | request, member_id, collection |  |
| [messaging_verification](../harness/server.py#L907) | request |  |
| [messaging_confirm](../harness/server.py#L922) | request |  |
| [messaging_hello](../harness/server.py#L937) | request |  |
| [registered_workspace_root](../harness/server.py#L953) | environment |  |
| [pending_signal_workspaces](../harness/server.py#L961) |  | Discover durable work without constructing another runtime for idle companies. |
| [cold_signal_sources](../harness/server.py#L989) | environment |  |
| [ingress_current](../harness/server.py#L999) | signal |  |
| [incoming_hook](../harness/server.py#L1016) | environment, hook_id, request |  |
| [wake_sources](../harness/server.py#L1038) | request, chat_id |  |
| [endpoint_secret](../harness/server.py#L1048) | endpoint_id, request |  |
| [reveal_wake_secret](../harness/server.py#L1060) | hook_id, request |  |
| [messaging_webhook](../harness/server.py#L1075) | environment, request, channel |  |
| [phone_tick](../harness/server.py#L1121) | selected | One pass of host alert delivery. A failed pass sends nothing and leaves the other ticks running. |
| [messaging_tick](../harness/server.py#L1135) | selected |  |
| [native_package_store](../harness/server.py#L1149) | selected |  |
| [revoke_native_plugin](../harness/server.py#L1156) | selected, principal_id, plugin_id |  |
| [native_installation_capabilities](../harness/server.py#L1166) | selected, principal_id, store |  |
| [plugins_catalogue](../harness/server.py#L1184) |  |  |
| [plugin_details](../harness/server.py#L1188) | plugin_id |  |
| [connections](../harness/server.py#L1195) | request |  |
| [custom_identity](../harness/server.py#L1199) | request, key, writable |  |
| [document_previews_for_workspace](../harness/server.py#L1222) | selected |  |
| [custom_connections](../harness/server.py#L1231) | request |  |
| [create_custom_connection](../harness/server.py#L1246) | body, request |  |
| [build_connector](../harness/server.py#L1267) |  |  |
| [release](../harness/server.py#L1279) | task |  |
| [custom_connection](../harness/server.py#L1285) | connector_id, request |  |
| [custom_connection_package](../harness/server.py#L1303) | connector_id, request |  |
| [custom_connection_secret](../harness/server.py#L1312) | connector_id, request |  |
| [custom_connection_secret_remove](../harness/server.py#L1333) | connector_id, name, request |  |
| [connect_provider](../harness/server.py#L1339) | provider, request |  |
| [connection_flow](../harness/server.py#L1382) | flow_id, request |  |
| [disconnect_provider](../harness/server.py#L1391) | provider, request |  |
| [oauth_landing](../harness/server.py#L1402) |  |  |
| [oauth_script](../harness/server.py#L1408) |  |  |
| [oauth_callback](../harness/server.py#L1412) | body, request |  |
| [home](../harness/server.py#L1421) |  |  |
| [script](../harness/server.py#L1441) |  |  |
| [question_box_script](../harness/server.py#L1445) |  |  |
| [question_box_style](../harness/server.py#L1449) |  |  |
| [logo](../harness/server.py#L1453) |  |  |
| [wordmark_font](../harness/server.py#L1458) |  |  |
| [connection_brand](../harness/server.py#L1463) | filename |  |
| [vendor](../harness/server.py#L1469) | filename |  |
| [workspace_artwork](../harness/server.py#L1476) | request |  |
| [empty_state_artwork](../harness/server.py#L1481) |  |  |
| [style](../harness/server.py#L1486) |  |  |
| [interface_component](../harness/server.py#L1520) | request |  |
| [diagram_component](../harness/server.py#L1526) |  |  |
| [shared_static](../harness/server.py#L1530) | asset |  |
| [shared_vendor](../harness/server.py#L1547) | filename |  |
| [source_icon](../harness/server.py#L1551) | host |  |
| [theme](../harness/server.py#L1559) |  |  |
| [session_details](../harness/server.py#L1583) | session |  |
| [health](../harness/server.py#L1591) |  |  |
| [session_info](../harness/server.py#L1606) | request |  |
| [set_session](../harness/server.py#L1609) | response, token, request |  |
| [login](../harness/server.py#L1614) | body, request, response |  |
| [demo_session](../harness/server.py#L1624) | request, response |  |
| [logout](../harness/server.py#L1633) | request, response |  |
| [select_environment](../harness/server.py#L1641) | body, request |  |
| [observers](../harness/server.py#L1648) | request |  |
| [observe](../harness/server.py#L1655) | body, request |  |
| [end_observation](../harness/server.py#L1662) | request |  |
| [status](../harness/server.py#L1669) | request |  |
| [business](../harness/server.py#L1687) | request, collection |  |
| [business_map](../harness/server.py#L1698) | request, collection, map_id |  |
| [business_profile](../harness/server.py#L1729) | body, request |  |
| [onboarding](../harness/server.py#L1736) | body, request |  |
| [profile_activity](../harness/server.py#L1754) | request, scope, days |  |
| [usage](../harness/server.py#L1779) | request, chat_id |  |
| [usage_settings](../harness/server.py#L1802) | body, request |  |
| [installed_native_skills](../harness/server.py#L1812) | request |  |
| [skills_catalogue](../harness/server.py#L1825) | request |  |
| [skills_installed](../harness/server.py#L1830) | request |  |
| [skills_install](../harness/server.py#L1835) | body, request |  |
| [agent_catalogue](../harness/server.py#L1843) | request |  |
| [participant_agent](../harness/server.py#L1850) | record, request | An agent with participant reach shares its conversation with a selected participant. |
| [owned_agent](../harness/server.py#L1859) | agent_id, request, write | The agent for its owner. A participant reads it; its definition and controls stay the owner's. |
| [public_agent](../harness/server.py#L1875) | record, request |  |
| [capability_snapshot](../harness/server.py#L1885) | request, dataset, chat_id |  |
| [workspace_capabilities](../harness/server.py#L1896) | request, dataset |  |
| [agents_list](../harness/server.py#L1901) | request |  |
| [agents_create](../harness/server.py#L1922) | body, request |  |
| [agent_details](../harness/server.py#L1935) | agent_id, request |  |
| [agent_update](../harness/server.py#L1939) | agent_id, body, request |  |
| [activate_agent](../harness/server.py#L1951) | agent_id, request, once, expected_revision |  |
| [agent_activate](../harness/server.py#L1967) | agent_id, body, request |  |
| [agent_run](../harness/server.py#L1971) | agent_id, body, request |  |
| [agent_pause](../harness/server.py#L1975) | agent_id, request |  |
| [agent_report](../harness/server.py#L1983) | agent_id, run_id, request |  |
| [chat](../harness/server.py#L2006) | body, request |  |
| [release_task](../harness/server.py#L2107) | task |  |
| [events](../harness/server.py#L2111) |  |  |
| [chats](../harness/server.py#L2117) | request, include_archived |  |
| [chat_metadata](../harness/server.py#L2126) | chat_id, body, request |  |
| [child_chat](../harness/server.py#L2137) | chat_id, request |  |
| [require_parent_control](../harness/server.py#L2169) | record |  |
| [answer_native_approval](../harness/server.py#L2176) | chat_id, request_id, request |  |
| [answer_native_question](../harness/server.py#L2209) | chat_id, request_id, request |  |
| [answer_credential_request](../harness/server.py#L2244) | chat_id, request_id, request |  |
| [stop_chat](../harness/server.py#L2289) | chat_id, request |  |
| [steer_chat](../harness/server.py#L2306) | chat_id, body, request |  |
| [attachment](../harness/server.py#L2328) | file, request |  |
| [attachment_image](../harness/server.py#L2347) | attachment_id, request |  |
| [file_owner](../harness/server.py#L2359) | request, write |  |
| [file_principal](../harness/server.py#L2373) | request, file_id, write |  |
| [history_guard](../harness/server.py#L2383) |  |  |
| [list_files](../harness/server.py#L2405) | request, chat_id, dataset |  |
| [get_file](../harness/server.py#L2424) | file_id, request |  |
| [file_content](../harness/server.py#L2432) | file_id, request |  |
| [rename_file](../harness/server.py#L2441) | file_id, body, request |  |
| [mark_file_opened](../harness/server.py#L2454) | file_id, body, request |  |
| [download_file](../harness/server.py#L2463) | file_id, request |  |
| [preview_file](../harness/server.py#L2482) | file_id, request |  |

### harness/verticals/retail/camera_context.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [timestamp](../harness/verticals/retail/camera_context.py#L22) |  |  |
| [geometry](../harness/verticals/retail/camera_context.py#L33) | self |  |
| [content](../harness/verticals/retail/camera_context.py#L55) | self |  |
| [__init__](../harness/verticals/retail/camera_context.py#L62) | self, state, index |  |
| [connect](../harness/verticals/retail/camera_context.py#L80) | self |  |
| [camera_id](../harness/verticals/retail/camera_context.py#L86) | record |  |
| [sync](../harness/verticals/retail/camera_context.py#L90) | self |  |
| [_row](../harness/verticals/retail/camera_context.py#L99) | self, db, camera_id, collection |  |
| [_records](../harness/verticals/retail/camera_context.py#L107) | self, row |  |
| [_views](../harness/verticals/retail/camera_context.py#L112) | db, camera_id |  |
| [_public](../harness/verticals/retail/camera_context.py#L116) | self, db, row, details |  |
| [list](../harness/verticals/retail/camera_context.py#L134) | self, collection |  |
| [get](../harness/verticals/retail/camera_context.py#L143) | self, camera_id, collection |  |
| [observations](../harness/verticals/retail/camera_context.py#L148) | self, clips |  |
| [_source_hash](../harness/verticals/retail/camera_context.py#L161) | self, record |  |
| [propose](../harness/verticals/retail/camera_context.py#L174) | self, camera_id, body, origin, collection |  |
| [confirm](../harness/verticals/retail/camera_context.py#L210) | self, camera_id, draft_id, expected_revision, operator, collection |  |
| [get_context_for_clip](../harness/verticals/retail/camera_context.py#L237) | self, record |  |
| [get_context_for_clip](../harness/verticals/retail/camera_context.py#L260) | state, index, record | Host-only resolution for the model adapter; callers cannot supply context text. |

### harness/verticals/retail/camera_onboarding.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_text](../harness/verticals/retail/camera_onboarding.py#L52) | value, label, limit |  |
| [has_clock_input](../harness/verticals/retail/camera_onboarding.py#L68) | self |  |
| [distinct_ids](../harness/verticals/retail/camera_onboarding.py#L86) | cls, values |  |
| [names](../harness/verticals/retail/camera_onboarding.py#L120) | cls, value, info |  |
| [public_stream_uri](../harness/verticals/retail/camera_onboarding.py#L125) | cls, value |  |
| [connection_requirements](../harness/verticals/retail/camera_onboarding.py#L139) | self |  |
| [credential_request_contract](../harness/verticals/retail/camera_onboarding.py#L147) | connector_id, owner, chat_id, collection, reason | Return metadata for the existing ``request_custom_connector_credentials`` tool. |
| [rtsp_connector_package](../harness/verticals/retail/camera_onboarding.py#L168) | camera_name | Build a source-only connector package for the secure credential flow. |
| [prepare_rtsp_connector](../harness/verticals/retail/camera_onboarding.py#L185) | store, owner, collection, camera_name, chat_id | Create the prepared connector that the existing secure request handler uses. |
| [request_rtsp_credentials](../harness/verticals/retail/camera_onboarding.py#L193) | store, connector_id, owner, chat_id, collection, camera_name | Open the existing private credential card for a prepared RTSP connector. |
| [public_defaults](../harness/verticals/retail/camera_onboarding.py#L202) |  | Return a JSON-safe copy for setup UI and API projections. |
| [serialize_draft](../harness/verticals/retail/camera_onboarding.py#L214) | draft | Stable JSON for a review record; secret values cannot enter this model. |

### harness/verticals/retail/camera_onboarding_policy.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [camera_onboarding_policy](../harness/verticals/retail/camera_onboarding_policy.py#L18) |  | Return a defensive public copy of the RTSP-first setup policy. |

### harness/verticals/retail/catalog_finder.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [readable_text](../harness/verticals/retail/catalog_finder.py#L37) | description |  |
| [classify](../harness/verticals/retail/catalog_finder.py#L41) | description | A stable product type for one item description: (key, label). |
| [product_types](../harness/verticals/retail/catalog_finder.py#L54) | company, location_id | Group the camera-observed items of a location into product types. |
| [write_product_types](../harness/verticals/retail/catalog_finder.py#L82) | company, location_id, path |  |
| [distinct](../harness/verticals/retail/catalog_finder.py#L110) | self |  |
| [import_found_products](../harness/verticals/retail/catalog_finder.py#L118) | company, location_id, path | Validate a finder result and save its products in the location catalog. No downloads. |
| [main](../harness/verticals/retail/catalog_finder.py#L149) | argv |  |

### harness/verticals/retail/catalog_image_model.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/verticals/retail/catalog_image_model.py#L43) | self, state, api_key, transport |  |
| [__call__](../harness/verticals/retail/catalog_image_model.py#L52) | self, owner, image, description, text, candidates, request_id |  |
| [extract_shelf](../harness/verticals/retail/catalog_image_model.py#L77) | self, owner, image, request_id | One bounded catalog extraction; proposed labels and identifiers stay provisional. |
| [_submit](../harness/verticals/retail/catalog_image_model.py#L105) | self, owner, image_bytes, request_id, body, schema, max_output, prefix |  |
| [receipt](../harness/verticals/retail/catalog_image_model.py#L149) | self, response, request_id, reservation_id, bound, max_output |  |

### harness/verticals/retail/catalog_inspection.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [canonical](../harness/verticals/retail/catalog_inspection.py#L22) | value |  |
| [normalized](../harness/verticals/retail/catalog_inspection.py#L26) | value |  |
| [geometry](../harness/verticals/retail/catalog_inspection.py#L30) | value |  |
| [crop](../harness/verticals/retail/catalog_inspection.py#L42) | image, box |  |
| [extract_frame](../harness/verticals/retail/catalog_inspection.py#L50) | path, timestamp | Decode source pixels once on CPU. Host resolves path; model never does. |
| [read_text](../harness/verticals/retail/catalog_inspection.py#L65) | image |  |
| [link_catalog](../harness/verticals/retail/catalog_inspection.py#L77) | text, candidates, object_grounded, proposed_id | Only a unique, visibly read catalog identifier confirms automatically. |
| [__init__](../harness/verticals/retail/catalog_inspection.py#L98) | self, state, authorized, source_resolver, catalog, publish_match, inspect_image, frame_reader, ocr, clock, object_verified |  |
| [connect](../harness/verticals/retail/catalog_inspection.py#L114) | self |  |
| [require](../harness/verticals/retail/catalog_inspection.py#L119) | self, owner, event |  |
| [process](../harness/verticals/retail/catalog_inspection.py#L123) | self, owner, event, payload, job_id |  |
| [image](../harness/verticals/retail/catalog_inspection.py#L214) | self, owner, key, event_lookup |  |

### harness/verticals/retail/catalog_setup.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [token_hash](../harness/verticals/retail/catalog_setup.py#L25) | token |  |
| [qr_svg](../harness/verticals/retail/catalog_setup.py#L31) | value |  |
| [__init__](../harness/verticals/retail/catalog_setup.py#L43) | self, state, locations, environment_id, clock |  |
| [connect](../harness/verticals/retail/catalog_setup.py#L54) | self |  |
| [overview](../harness/verticals/retail/catalog_setup.py#L57) | self, owner, collection, location_id |  |
| [import_products](../harness/verticals/retail/catalog_setup.py#L68) | self, owner, collection, location_id, rows, source_name, source_kind |  |
| [create_handoff](../harness/verticals/retail/catalog_setup.py#L100) | self, owner, collection, location_id, origin |  |
| [_handoff](../harness/verticals/retail/catalog_setup.py#L113) | self, db, token |  |
| [upload](../harness/verticals/retail/catalog_setup.py#L120) | self, token, data, extraction_consent |  |
| [photo](../harness/verticals/retail/catalog_setup.py#L145) | self, owner, key |  |
| [list_pending_photos](../harness/verticals/retail/catalog_setup.py#L156) | self, owner |  |
| [mark_photo_status](../harness/verticals/retail/catalog_setup.py#L165) | self, owner, key, status, detail |  |
| [complete_photo](../harness/verticals/retail/catalog_setup.py#L174) | self, owner, key, product_ids |  |

### harness/verticals/retail/catalog_setup_routes.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [register_catalog_setup_routes](../harness/verticals/retail/catalog_setup_routes.py#L30) | app, workspace, access |  |
| [actor](../harness/verticals/retail/catalog_setup_routes.py#L33) | request, write |  |
| [failed](../harness/verticals/retail/catalog_setup_routes.py#L37) | exc |  |
| [setup](../harness/verticals/retail/catalog_setup_routes.py#L39) | request, collection, location_id |  |
| [import_catalog](../harness/verticals/retail/catalog_setup_routes.py#L44) | body, request |  |
| [import_file](../harness/verticals/retail/catalog_setup_routes.py#L49) | request, file, collection, location_id |  |
| [handoff](../harness/verticals/retail/catalog_setup_routes.py#L60) | body, request |  |
| [shelf_crop](../harness/verticals/retail/catalog_setup_routes.py#L65) | key, index, request |  |
| [current](../harness/verticals/retail/catalog_setup_routes.py#L71) |  |  |
| [photo](../harness/verticals/retail/catalog_setup_routes.py#L77) | key, request |  |
| [current](../harness/verticals/retail/catalog_setup_routes.py#L81) |  |  |
| [mobile_style](../harness/verticals/retail/catalog_setup_routes.py#L87) |  |  |
| [mobile_script](../harness/verticals/retail/catalog_setup_routes.py#L90) |  |  |
| [mobile_page](../harness/verticals/retail/catalog_setup_routes.py#L92) | environment |  |
| [mobile_upload](../harness/verticals/retail/catalog_setup_routes.py#L96) | environment, request, file, extraction_consent |  |

### harness/verticals/retail/catalog_setup_tools.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [specs](../harness/verticals/retail/catalog_setup_tools.py#L6) | write |  |
| [make](../harness/verticals/retail/catalog_setup_tools.py#L8) | name, description, properties, required |  |
| [call](../harness/verticals/retail/catalog_setup_tools.py#L20) | agent, chat_id, collection, name, args, run |  |

### harness/verticals/retail/compute_guard.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_utc](../harness/verticals/retail/compute_guard.py#L49) | value |  |
| [_amount](../harness/verticals/retail/compute_guard.py#L59) | value, name |  |
| [_code_root](../harness/verticals/retail/compute_guard.py#L71) |  | Locate source ownership without assuming a particular install depth. |
| [_read_private](../harness/verticals/retail/compute_guard.py#L84) | path |  |
| [validate_approval](../harness/verticals/retail/compute_guard.py#L88) | path, workspace, planned_gross_usd, purpose, now | Validate an attested $0 provider cap, credits and gross headroom. |
| [claim_approval](../harness/verticals/retail/compute_guard.py#L137) | approval, now | Atomically consume an approval before image builds or remote execution. |

### harness/verticals/retail/control_room_routes.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [owner_directory](../harness/verticals/retail/control_room_routes.py#L43) | state, owner |  |
| [safe_file](../harness/verticals/retail/control_room_routes.py#L46) | root, relative |  |
| [read_bundle](../harness/verticals/retail/control_room_routes.py#L55) | selected, owner |  |
| [state_signature](../harness/verticals/retail/control_room_routes.py#L82) | selected, owner | A fingerprint of what a bundle read depends on: the manifest, the company's stores and the source lookup in force. A write to any of them changes it. |
| [recent_bundle](../harness/verticals/retail/control_room_routes.py#L96) | selected, owner, interval | The owner's bundle, shared by the requests of one page. |
| [register_control_room_routes](../harness/verticals/retail/control_room_routes.py#L112) | app |  |
| [context](../harness/verticals/retail/control_room_routes.py#L115) | request |  |
| [item_image](../harness/verticals/retail/control_room_routes.py#L127) | request, inspection_id |  |
| [allowed](../harness/verticals/retail/control_room_routes.py#L131) |  |  |
| [bootstrap](../harness/verticals/retail/control_room_routes.py#L145) | request |  |
| [control_room_status](../harness/verticals/retail/control_room_routes.py#L156) | request |  |
| [control_room_revision](../harness/verticals/retail/control_room_routes.py#L171) | request | What an open page polls: the revision of its published data, for this session's owner. |
| [control_room_asset](../harness/verticals/retail/control_room_routes.py#L207) | request, asset |  |

### harness/verticals/retail/control_room_static.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [static_code_file](../harness/verticals/retail/control_room_static.py#L9) | asset |  |
| [is_static_viewer_request](../harness/verticals/retail/control_room_static.py#L20) | path, method |  |

### harness/verticals/retail/core_trackers/__init__.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [load_recipe](../harness/verticals/retail/core_trackers/__init__.py#L30) | business_type |  |
| [core_scripts](../harness/verticals/retail/core_trackers/__init__.py#L36) | business_type | The maintained processor script of each Core Tracker of a business type, by tracker key. |
| [core_script](../harness/verticals/retail/core_trackers/__init__.py#L45) | tracker, scripts | The script this service runs for a tracker record in its own process, else None. |
| [tracker_id](../harness/verticals/retail/core_trackers/__init__.py#L64) | company_id, location_id, key |  |
| [install_core_trackers](../harness/verticals/retail/core_trackers/__init__.py#L69) | company, location_id, business_type | Record the business type's Core Trackers for one location. Safe to repeat. |
| [installed_trackers](../harness/verticals/retail/core_trackers/__init__.py#L89) | company, location_id | The location's trackers: core first in recipe order, then the company's own. |
| [add_tracker](../harness/verticals/retail/core_trackers/__init__.py#L95) | company, location_id, key, label, observes, event_types, script, agent_id | Add one of the company's own trackers beside the core set. |
| [agent_tracker_key](../harness/verticals/retail/core_trackers/__init__.py#L115) | agent_id | The tracker key of a Tracking Agent's record: stable, and outside every recipe's keys. |
| [agent_tracker](../harness/verticals/retail/core_trackers/__init__.py#L120) | state, owner, collection, agent_id | The tracker record linked to a Tracking Agent, once it has one. |
| [link_tracking_agent](../harness/verticals/retail/core_trackers/__init__.py#L125) | company, location_id, agent, event_types | The tracker record of a Tracking Agent at a location, written once through `add_tracker`. |
| [remove_tracker](../harness/verticals/retail/core_trackers/__init__.py#L139) | company, location_id, key | Remove one of the company's own trackers. Core Trackers stay. |
| [update_tracker](../harness/verticals/retail/core_trackers/__init__.py#L166) | company, location_id, key, changes, expected_revision | Change one of the company's own trackers. Core Trackers follow their recipe. |
| [tracker_records](../harness/verticals/retail/core_trackers/__init__.py#L193) | state, owner, collection | The owner's saved tracker records of a collection, read without opening the company for writing. |
| [location_trackers](../harness/verticals/retail/core_trackers/__init__.py#L206) | state, owner, collection, location_id, agents, allowed | What the harness lists for a location: Core Trackers, then the customer's own. |

### harness/verticals/retail/core_trackers/basket.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [run](../harness/verticals/retail/core_trackers/basket.py#L12) | company, location_id, period, data |  |
| [measure](../harness/verticals/retail/core_trackers/basket.py#L21) | x, y |  |
| [row](../harness/verticals/retail/core_trackers/basket.py#L25) | basket |  |

### harness/verticals/retail/core_trackers/common.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [epoch](../harness/verticals/retail/core_trackers/common.py#L27) | text |  |
| [day_period](../harness/verticals/retail/core_trackers/common.py#L31) | day |  |
| [days_period](../harness/verticals/retail/core_trackers/common.py#L37) | last_day, days |  |
| [when](../harness/verticals/retail/core_trackers/common.py#L44) | period | The period as a sentence says it: «on Sat 10 Oct 2026», «from 4 Oct to 10 Oct 2026». |
| [buckets](../harness/verticals/retail/core_trackers/common.py#L49) | period |  |
| [within](../harness/verticals/retail/core_trackers/common.py#L55) | row, a, b, key |  |
| [camera_name](../harness/verticals/retail/core_trackers/common.py#L77) | self, camera_id |  |
| [available](../harness/verticals/retail/core_trackers/common.py#L80) | self | The sources this location has, named as the recipe's `requires` names them. |
| [missing](../harness/verticals/retail/core_trackers/common.py#L95) | self, key |  |
| [read_location](../harness/verticals/retail/core_trackers/common.py#L101) | company, location_id | Load one location's records once for a tracker run. |
| [money](../harness/verticals/retail/core_trackers/common.py#L147) | amount, currency | An amount as a person reads it: «€10.60», or «10.60 CHF» for a currency without a common sign. |
| [number](../harness/verticals/retail/core_trackers/common.py#L154) | value, digits |  |
| [series](../harness/verticals/retail/core_trackers/common.py#L161) | period, measure |  |
| [trend](../harness/verticals/retail/core_trackers/common.py#L165) | period, measure, days |  |
| [event_row](../harness/verticals/retail/core_trackers/common.py#L170) | event | The tile's event shape: one observation behind the number. |
| [by_camera](../harness/verticals/retail/core_trackers/common.py#L178) | data, rows_ |  |
| [busiest](../harness/verticals/retail/core_trackers/common.py#L185) | points |  |
| [plural](../harness/verticals/retail/core_trackers/common.py#L190) | value, unit |  |
| [count_summary](../harness/verticals/retail/core_trackers/common.py#L194) | value, unit, period, points, daily |  |
| [count_tracker](../harness/verticals/retail/core_trackers/common.py#L205) | key, unit, data, period, rows_ | A count over the period: the tile number, its series, and the event rows on the canvas. |
| [needs](../harness/verticals/retail/core_trackers/common.py#L225) | data, key, period, phrase | A measure whose source is missing: state "needs" with its three words. |
| [publish](../harness/verticals/retail/core_trackers/common.py#L237) | data, key, period, value, unit, series, events, canvas, summary, trend, state, needs, tile_extra | Write the tracker's output revision: canvas (full view) and tile (its compact summary). |
| [outputs](../harness/verticals/retail/core_trackers/common.py#L271) | company, location_id | Current output of each installed tracker, core first. |

### harness/verticals/retail/core_trackers/conversion.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [run](../harness/verticals/retail/core_trackers/conversion.py#L15) | company, location_id, period, data |  |

### harness/verticals/retail/core_trackers/empty_shelves.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [run](../harness/verticals/retail/core_trackers/empty_shelves.py#L12) | company, location_id, period, data |  |

### harness/verticals/retail/core_trackers/picked_up.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [run](../harness/verticals/retail/core_trackers/picked_up.py#L15) | company, location_id, period, data |  |

### harness/verticals/retail/core_trackers/presentation.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [record_id](../harness/verticals/retail/core_trackers/presentation.py#L54) | tracker |  |
| [public](../harness/verticals/retail/core_trackers/presentation.py#L58) | record | A saved presentation as a tool, a route and the page carry it. |
| [belongs](../harness/verticals/retail/core_trackers/presentation.py#L64) | saved, tracker | Whether a saved presentation is this tracker's own. A tracker's id comes from its key, so a tracker made again under a removed tracker's key meets that one's rows until they are cleared: a presentation saved at a later revision than the tracker has reached was the earlier one's. |
| [presentation_of](../harness/verticals/retail/core_trackers/presentation.py#L71) | tracker, saved, output | A tracker's presentation: the saved one, or its default at revision 0. |
| [forget](../harness/verticals/retail/core_trackers/presentation.py#L78) | db, owner, tracker | Remove a tracker's saved presentation and every kept revision, inside the caller's transaction. A tracker's removal calls this beside the rows of its script. |
| [forget_removed](../harness/verticals/retail/core_trackers/presentation.py#L86) | company, location_id, trackers | Clear the presentations of trackers a location has removed; returns how many. The page pass calls this with the location's trackers, so a key used again starts with its own presentation. |
| [_read](../harness/verticals/retail/core_trackers/presentation.py#L101) | state, query, values |  |
| [saved_presentations](../harness/verticals/retail/core_trackers/presentation.py#L112) | state, owner, collection | The owner's saved presentations of a collection by tracker id, read without opening the company for writing. |
| [saved_revisions](../harness/verticals/retail/core_trackers/presentation.py#L118) | state, owner, tracker | Every kept revision of one tracker's presentation, newest first. |
| [current_output](../harness/verticals/retail/core_trackers/presentation.py#L128) | state, owner, tracker | The tracker's current output revision, once it has one. |
| [save_presentation](../harness/verticals/retail/core_trackers/presentation.py#L135) | company, tracker, change, expected_revision, saved_by, clock | Save a company tracker's presentation as its next revision; returns it in its public form. |

### harness/verticals/retail/core_trackers/product_interactions.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [run](../harness/verticals/retail/core_trackers/product_interactions.py#L15) | company, location_id, period, data |  |

### harness/verticals/retail/core_trackers/put_back.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [run](../harness/verticals/retail/core_trackers/put_back.py#L15) | company, location_id, period, data |  |

### harness/verticals/retail/core_trackers/queue_time.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [run](../harness/verticals/retail/core_trackers/queue_time.py#L15) | company, location_id, period, data |  |
| [measure](../harness/verticals/retail/core_trackers/queue_time.py#L21) | x, y |  |

### harness/verticals/retail/core_trackers/run.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [zone_day](../harness/verticals/retail/core_trackers/run.py#L43) | zone, now | The calendar day at `now` (epoch seconds) in a named timezone, UTC without one. |
| [location_zone](../harness/verticals/retail/core_trackers/run.py#L54) | company, location_id | The timezone of the location's coordinates, when it has them. |
| [local_day](../harness/verticals/retail/core_trackers/run.py#L63) | company, location_id, now | The location's current calendar day: in the timezone of its coordinates, UTC otherwise. |
| [observed_day](../harness/verticals/retail/core_trackers/run.py#L68) | data | The UTC day of the location's latest observation, once it has one. |
| [latest_day](../harness/verticals/retail/core_trackers/run.py#L74) | data | The UTC day of the location's latest observation. |
| [brief](../harness/verticals/retail/core_trackers/run.py#L79) | error, what | A run row's words for a failure: the product's own sentence, or the kind of fault. |
| [run_trackers](../harness/verticals/retail/core_trackers/run.py#L94) | company, location_id, period, only, deadline, custom, clock, defer | Derive the location's records, read them once, then run each installed tracker's processor. |
| [_taken](../harness/verticals/retail/core_trackers/run.py#L150) | key, output, outputs, errors, script_runs | File what `custom` returned for one script tracker: its run, its sentence and its output. |
| [run_script_trackers](../harness/verticals/retail/core_trackers/run.py#L162) | company, location_id, period, data, trackers, custom | The script trackers a pass deferred, each through `custom`, in order. The caller sets `PASS` around this with the script time of the pass. One tracker's fault stays its own. |
| [sandboxed](../harness/verticals/retail/core_trackers/run.py#L177) | tracker | Whether a company's tracker has a processing script: a published sandbox script, or a script name on its record. Either way its code stays out of this process. |
| [reading_periods](../harness/verticals/retail/core_trackers/run.py#L184) | company, location_id, data, last_day | The week, the month and the year a location's trackers are read over: {name: period}. |
| [period_readings](../harness/verticals/retail/core_trackers/run.py#L195) | company, location_id, last_day, data | Each tracker's output over the week, the month and the year. Nothing is stored. |
| [main](../harness/verticals/retail/core_trackers/run.py#L237) | argv |  |

### harness/verticals/retail/core_trackers/sales.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [chosen](../harness/verticals/retail/core_trackers/sales.py#L12) | data, a, b | Till transactions when the period has them, else the estimated sales. |
| [run](../harness/verticals/retail/core_trackers/sales.py#L19) | company, location_id, period, data |  |
| [row](../harness/verticals/retail/core_trackers/sales.py#L30) | sale |  |

### harness/verticals/retail/core_trackers/visitors.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [run](../harness/verticals/retail/core_trackers/visitors.py#L12) | company, location_id, period, data |  |
| [row](../harness/verticals/retail/core_trackers/visitors.py#L24) | visit |  |

### harness/verticals/retail/cosmos_archive_import.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [sha](../harness/verticals/retail/cosmos_archive_import.py#L33) | path |  |
| [collapse](../harness/verticals/retail/cosmos_archive_import.py#L41) | text | A doubled sentence ("A. A.") reads once; every other text stays as the model wrote it. |
| [fenced_json](../harness/verticals/retail/cosmos_archive_import.py#L52) | text | The final JSON of a model answer, with or without a reasoning block or a code fence. |
| [answer_events](../harness/verticals/retail/cosmos_archive_import.py#L59) | answer | Flatten the two event shapes Cosmos returns: a list, or person -> type -> event. |
| [presence](../harness/verticals/retail/cosmos_archive_import.py#L76) | tracks | Tracker person -> the source times the tracker saw that person. |
| [person_of](../harness/verticals/retail/cosmos_archive_import.py#L85) | label, seen |  |
| [validate](../harness/verticals/retail/cosmos_archive_import.py#L98) | raw, seen, start_s, end_s, vocabulary | Structure check for one raw event. Returns (fields, None) or (None, reason). |
| [retail_profile](../harness/verticals/retail/cosmos_archive_import.py#L126) | company, location_id | The saved observation profile for the retail vocabulary of this location. |
| [drain](../harness/verticals/retail/cosmos_archive_import.py#L140) | company, pipeline | Run the projection work the stream queued. Image inspection of real evidence stays queued. |
| [ingest_recording](../harness/verticals/retail/cosmos_archive_import.py#L154) | company, location_id, camera_id, recording, tracks, windows, profile, vocabulary, data_basis, evidence, title, files, clip, pipeline, publisher_note | Admit one recording: source, tracked visitors, model events, receipts. |
| [host_tracks](../harness/verticals/retail/cosmos_archive_import.py#L243) | viewer | The archive's viewer track format, as the tracker frames `ingest_tracks` reads. |
| [archive_windows](../harness/verticals/retail/cosmos_archive_import.py#L255) | root, clip, duration, suffix | The preserved answer windows of one clip for one model, or None when the file is absent. |
| [valid_count](../harness/verticals/retail/cosmos_archive_import.py#L283) | windows, seen, vocabulary |  |
| [import_archive](../harness/verticals/retail/cosmos_archive_import.py#L288) | company, archive_root, location_id, room_id, clips, cameras, capture_starts, publish_media | Ingest the listed archive clips into the location. Safe to repeat. |
| [publish](../harness/verticals/retail/cosmos_archive_import.py#L301) | source, relative |  |
| [main](../harness/verticals/retail/cosmos_archive_import.py#L415) | argv |  |

### harness/verticals/retail/cosmos_inspect.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [inspection_complete](../harness/verticals/retail/cosmos_inspect.py#L58) | result | Check answer completion, separately from metering and visual correctness. |
| [execution_profile](../harness/verticals/retail/cosmos_inspect.py#L72) | model_id, quality_profile |  |
| [processor_settings](../harness/verticals/retail/cosmos_inspect.py#L123) | model_id, quality_profile |  |
| [audit_processor_inputs](../harness/verticals/retail/cosmos_inspect.py#L136) | processor, inputs, video_metadata, settings | Record measured tensors and sampling, without storing hidden model reasoning. |
| [plain](../harness/verticals/retail/cosmos_inspect.py#L140) | value |  |
| [validate_requests](../harness/verticals/retail/cosmos_inspect.py#L184) | requests, clip_ids |  |
| [final_text](../harness/verticals/retail/cosmos_inspect.py#L196) | text |  |
| [parse_answer](../harness/verticals/retail/cosmos_inspect.py#L202) | text, clip_ids |  |
| [parse_comparison](../harness/verticals/retail/cosmos_inspect.py#L230) | text, clip_ids | Map fixed attachment positions to source IDs; the model never chooses IDs. |
| [camera_context_text](../harness/verticals/retail/cosmos_inspect.py#L256) | context | Render host-resolved operator notes as bounded scene data. |
| [inspection_content](../harness/verticals/retail/cosmos_inspect.py#L266) | clip_ids, source_records, paths, prompt |  |
| [_derived_input](../harness/verticals/retail/cosmos_inspect.py#L279) | entry, company_state |  |
| [load_manifest](../harness/verticals/retail/cosmos_inspect.py#L304) | path, quality_profile, company_state |  |
| [inspect_batch](../harness/verticals/retail/cosmos_inspect.py#L357) | clips, requests, model_id, quality_profile | Importable remote function; all GPU work is contained in one bounded call. |
| [create_worker](../harness/verticals/retail/cosmos_inspect.py#L476) | modal, model_id, profile |  |
| [run_inspection](../harness/verticals/retail/cosmos_inspect.py#L494) | clips, requests, approval_path, output, check, query_budget, model_id, warm_benchmark, quality_profile, company_usage |  |
| [stop_own_app](../harness/verticals/retail/cosmos_inspect.py#L634) | app_id | Stop only this verified Rocoto inspection app, never all workspace apps. |
| [stop](../harness/verticals/retail/cosmos_inspect.py#L647) |  |  |
| [_worker_command](../harness/verticals/retail/cosmos_inspect.py#L658) | interpreter, *arguments | Keep fresh inspections and their stop path in the selected harness source layout. |
| [_stop_remote_receipt](../harness/verticals/retail/cosmos_inspect.py#L664) | directory, interpreter, environment |  |
| [cache_results](../harness/verticals/retail/cosmos_inspect.py#L678) | result, state, run_id | Persist model output as observations/candidate connections with provenance. |
| [_cache_results_unlocked](../harness/verticals/retail/cosmos_inspect.py#L689) | result, state, run_id |  |
| [_cache_key](../harness/verticals/retail/cosmos_inspect.py#L733) | clips, requests, model_id, quality_profile |  |
| [_prepare_source_clip](../harness/verticals/retail/cosmos_inspect.py#L758) | record, path, quality_profile | Decode a bounded interval with codec-compatible dimensions. |
| [_request_asset_key](../harness/verticals/retail/cosmos_inspect.py#L775) | requests, model_id, quality_profile |  |
| [_reuse_prepared_source](../harness/verticals/retail/cosmos_inspect.py#L783) | record, path, state, request_key, quality_profile |  |
| [_modal_runtime](../harness/verticals/retail/cosmos_inspect.py#L821) | modal_python | Resolve host-owned Modal credentials only for a fresh inspection. |
| [_inspect_sources](../harness/verticals/retail/cosmos_inspect.py#L843) | ids, requests, index, state, approval_path, query_approval_path, modal_python, model_id, quality_profile |  |
| [inspect](../harness/verticals/retail/cosmos_inspect.py#L942) | clip_id, prompt, index, state, approval_path, query_approval_path, compare_clip_id, modal_python, model_id, quality_profile | Inspect one source or a pair using the exact current question. |
| [inspect_live](../harness/verticals/retail/cosmos_inspect.py#L951) | clip_ids, prompt, index, state, approval_path, compare_views, modal_python, model_id, quality_profile | Fresh Cosmos video reasoning, with exact-question/source-hash cache reuse. |
| [main](../harness/verticals/retail/cosmos_inspect.py#L970) |  |  |
| [terminate](../harness/verticals/retail/cosmos_inspect.py#L981) | signum, frame |  |

### harness/verticals/retail/cosmos_retrieval.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_file_identity](../harness/verticals/retail/cosmos_retrieval.py#L40) | path |  |
| [_atomic_write](../harness/verticals/retail/cosmos_retrieval.py#L45) | path, content | Publish one durable file; unique temporary names allow concurrent import preparation. |
| [_sync_directory](../harness/verticals/retail/cosmos_retrieval.py#L60) | path |  |
| [generation_paths](../harness/verticals/retail/cosmos_retrieval.py#L68) | state, marker | Resolve committed files; callers retain one marker for a coherent view. |
| [_validate_payload](../harness/verticals/retail/cosmos_retrieval.py#L96) | clips, embeddings, report, marker |  |
| [load_generation](../harness/verticals/retail/cosmos_retrieval.py#L116) | state, allow_legacy | Read and verify one complete committed snapshot without loading a model. |
| [_publication_lock](../harness/verticals/retail/cosmos_retrieval.py#L177) | state |  |
| [_stage_generation_locked](../harness/verticals/retail/cosmos_retrieval.py#L193) | state, records, vectors, report |  |
| [_promote_generation_locked](../harness/verticals/retail/cosmos_retrieval.py#L223) | state, marker |  |
| [_publish_generation_locked](../harness/verticals/retail/cosmos_retrieval.py#L229) | state, records, vectors, report |  |
| [_publish_generation](../harness/verticals/retail/cosmos_retrieval.py#L233) | state, records, vectors, report | Explicit full replacement used by the historical offline import command. |
| [_merge_metadata](../harness/verticals/retail/cosmos_retrieval.py#L239) | records, vectors, asset_metadata |  |
| [_combined_report](../harness/verticals/retail/cosmos_retrieval.py#L284) | records, prior, parent_generation |  |
| [merge_index](../harness/verticals/retail/cosmos_retrieval.py#L303) | state, records, vectors, asset_metadata, expected_generation, replace_clip_ids, before_commit | Commit additive source imports under one load/merge/publication lock. |
| [promote](../harness/verticals/retail/cosmos_retrieval.py#L362) |  |  |
| [__init__](../harness/verticals/retail/cosmos_retrieval.py#L377) | self, state |  |
| [use_text_encoder](../harness/verticals/retail/cosmos_retrieval.py#L385) | self, source | Host-only sharing of the pinned CPU model, preserving company indexes. |
| [_reload](../harness/verticals/retail/cosmos_retrieval.py#L406) | self |  |
| [refresh](../harness/verticals/retail/cosmos_retrieval.py#L412) | self | Load a newly committed generation, preserving the index and encoder on failure. |
| [_encoder_ready](../harness/verticals/retail/cosmos_retrieval.py#L434) | self |  |
| [_encoder_verified](../harness/verticals/retail/cosmos_retrieval.py#L440) | self |  |
| [_load_model](../harness/verticals/retail/cosmos_retrieval.py#L449) | self |  |
| [_encode_text](../harness/verticals/retail/cosmos_retrieval.py#L466) | self, query |  |
| [search](../harness/verticals/retail/cosmos_retrieval.py#L483) | self, query, limit, dataset |  |
| [status](../harness/verticals/retail/cosmos_retrieval.py#L493) | self |  |
| [build](../harness/verticals/retail/cosmos_retrieval.py#L499) | self, *args, **kwargs |  |
| [install_text_assets](../harness/verticals/retail/cosmos_retrieval.py#L503) | encoder_path, tokenizer_zip, metadata_path, state | Install a local export without downloading or executing model source code. |
| [prepare_index](../harness/verticals/retail/cosmos_retrieval.py#L538) | embedding_files, manifest_files, state, baseline_state, excluded_datasets | Convert authenticated worker artifacts to a searchable source-video index. |
| [main](../harness/verticals/retail/cosmos_retrieval.py#L667) |  |  |

### harness/verticals/retail/cosmos_stream_bridge.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [digest](../harness/verticals/retail/cosmos_stream_bridge.py#L15) | value |  |
| [final_answer](../harness/verticals/retail/cosmos_stream_bridge.py#L44) | text | Accept final JSON only, including official think/answer tags and JSON fence. |
| [prepare_prompt](../harness/verticals/retail/cosmos_stream_bridge.py#L64) | pipeline, owner, context, clock_basis, source_offset_s, tracker_labels, tracker_receipt, input_preparation | Resolve the saved native profile and persistable host input contract. |
| [_admit_result](../harness/verticals/retail/cosmos_stream_bridge.py#L145) | pipeline, owner, prepared, envelope, input_trace | Validate the stock signal envelope, original trace and model's structured final. |
| [admit_result](../harness/verticals/retail/cosmos_stream_bridge.py#L243) | pipeline, owner, prepared, envelope, input_trace | Preserve authorized raw attempts, including rejected clocks/labels/answers. |
| [connect_stock_results](../harness/verticals/retail/cosmos_stream_bridge.py#L264) | element, pipeline, owner, prepared_for, trace_for, on_receipt | Attach to stock GStreamer's documented vlm-result signal without SDK edits. |
| [receive](../harness/verticals/retail/cosmos_stream_bridge.py#L271) | _element, stream_id, start_sec, end_sec, result_text |  |

### harness/verticals/retail/demo_guidance.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_questions](../harness/verticals/retail/demo_guidance.py#L14) | *prompts |  |
| [demo_guidance](../harness/verticals/retail/demo_guidance.py#L56) | environment_id, clips |  |

### harness/verticals/retail/discovery.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_unit](../harness/verticals/retail/discovery.py#L18) | rows |  |
| [_distribution](../harness/verticals/retail/discovery.py#L26) | scores |  |
| [_cluster](../harness/verticals/retail/discovery.py#L34) | vectors, groups | Deterministic spherical k-means, bounded fitting sample; assign every row. |
| [_merge_intervals](../harness/verticals/retail/discovery.py#L68) | records, vectors, scores, selected |  |
| [_representatives](../harness/verticals/retail/discovery.py#L97) | members, records, vectors, scores, count |  |
| [_clip_result](../harness/verticals/retail/discovery.py#L116) | record, score |  |
| [_interval_result](../harness/verticals/retail/discovery.py#L124) | interval, records, scores |  |
| [discover_patterns](../harness/verticals/retail/discovery.py#L130) | index, query, dataset, groups, candidate_limit, score_threshold, representatives_per_group, group_id, interval_id, offset, limit | Score every scoped window; group selected candidates and page the evidence. |

### harness/verticals/retail/evidence_captions.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_canonical](../harness/verticals/retail/evidence_captions.py#L56) | value |  |
| [_hash](../harness/verticals/retail/evidence_captions.py#L60) | value |  |
| [_identity](../harness/verticals/retail/evidence_captions.py#L64) | value |  |
| [_text](../harness/verticals/retail/evidence_captions.py#L68) | value, maximum |  |
| [pricing](../harness/verticals/retail/evidence_captions.py#L72) | model |  |
| [__init__](../harness/verticals/retail/evidence_captions.py#L86) | self, state, api_key, model, pool, transport, authorized, clock |  |
| [connect](../harness/verticals/retail/evidence_captions.py#L107) | self |  |
| [_current](../harness/verticals/retail/evidence_captions.py#L112) | self, scope, current |  |
| [_observation](../harness/verticals/retail/evidence_captions.py#L117) | self, clip, observation_ref |  |
| [_emit](../harness/verticals/retail/evidence_captions.py#L148) | self, emit, event |  |
| [caption](../harness/verticals/retail/evidence_captions.py#L154) | self, scope, index, clip_id, question, observation_ref, current, emit |  |
| [_plain](../harness/verticals/retail/evidence_captions.py#L300) | value, partial |  |
| [_receipt](../harness/verticals/retail/evidence_captions.py#L312) | self, response, request_id, reservation_id, input_bound |  |

### harness/verticals/retail/evidence_presentation.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [build_presentation](../harness/verticals/retail/evidence_presentation.py#L20) | arguments, index, collection, public_clip |  |

### harness/verticals/retail/execution_policy.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [admit_fresh_inspection](../harness/verticals/retail/execution_policy.py#L18) | maximum_usd |  |

### harness/verticals/retail/focus.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/verticals/retail/focus.py#L22) | self, state, sample_fps, max_width, max_seconds |  |
| [_histogram](../harness/verticals/retail/focus.py#L31) | frame, box |  |
| [_features](../harness/verticals/retail/focus.py#L41) | gray, box |  |
| [_flow](../harness/verticals/retail/focus.py#L48) | previous, current, points, box |  |
| [build](../harness/verticals/retail/focus.py#L70) | self, record, normalized_bbox, anchor_seconds |  |
| [_track](../harness/verticals/retail/focus.py#L102) | self, path, clip_id, start, duration, box, anchor |  |

### harness/verticals/retail/import_control_room_bundle.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [sha](../harness/verticals/retail/import_control_room_bundle.py#L25) | path |  |
| [write_json](../harness/verticals/retail/import_control_room_bundle.py#L32) | path, value |  |
| [source_file](../harness/verticals/retail/import_control_room_bundle.py#L39) | root, relative |  |
| [make_poster](../harness/verticals/retail/import_control_room_bundle.py#L46) | video, target, at_s |  |
| [viewer_tracks](../harness/verticals/retail/import_control_room_bundle.py#L51) | raw |  |
| [import_bundle](../harness/verticals/retail/import_control_room_bundle.py#L62) | run_root, state, owner, location_id, room_id, camera_ids, reviews, collection, location_name, weather, cover_image, poster_builder, visit_scope | Import one location while its scheduler waits, including optional tracked visits. |
| [_import_bundle](../harness/verticals/retail/import_control_room_bundle.py#L80) | run_root, state, owner, location_id, room_id, camera_ids, reviews, collection, location_name, weather, cover_image, poster_builder |  |
| [carried_page_data](../harness/verticals/retail/import_control_room_bundle.py#L250) | destination | What `publish_core_trackers` wrote into this bundle, so a re-import keeps it. |
| [page_lock](../harness/verticals/retail/import_control_room_bundle.py#L266) | destination | One writer of a page's data at a time: a tracker pass, a host import and a saved presentation take turns. |
| [reading](../harness/verticals/retail/import_control_room_bundle.py#L280) | output | One period's reading as a tile carries it: its number, its series and its canvas, each list cut to ROWS. |
| [in_currency](../harness/verticals/retail/import_control_room_bundle.py#L287) | tiles, currency | A company tracker's amount is written in the location's currency, the one the catalog names, when its output names none: Home and the canvas then write the same characters. |
| [tracker_page](../harness/verticals/retail/import_control_room_bundle.py#L295) | company, location_id, readings, only, kept | The tiles and the canvases of a location's trackers as the page reads them: (tiles, canvases keyed by tracker). |
| [tracker_row](../harness/verticals/retail/import_control_room_bundle.py#L336) | company, location_id, tracker_id, currency, kept | One company tracker's tile row and canvas as the page carries them: its stored output and its week, month and year readings with its presentation applied, and an amount in the location's currency. (None, None) while the tracker is still to get a row of its own. A saved presentation and a canvas read ahead of the page both assemble here, so a tile and a canvas come out in one pe |
| [location_currency](../harness/verticals/retail/import_control_room_bundle.py#L354) | company, location_id | The currency a location's catalog names, the one `write_page` gives its page. |
| [show_presentation](../harness/verticals/retail/import_control_room_bundle.py#L360) | company, location_id, tracker_id | Carry one company tracker's saved presentation into the owner's published page, without a tracker pass: its own row and canvas are assembled again from its stored output and readings. Returns whether the page data changed. |
| [publish_core_trackers](../harness/verticals/retail/import_control_room_bundle.py#L384) | company, location_id, location_name | Carry a location's trackers in the page data, core first then the company's own. |
| [write_page](../harness/verticals/retail/import_control_room_bundle.py#L401) | company, location_id, readings, destination, location_name | The page data of `publish_core_trackers`, assembled and written while its lock is held. |
| [generated_cover](../harness/verticals/retail/import_control_room_bundle.py#L519) | relative | Select a shipped generic illustration, preserving its recorded provenance. |
| [ingest_tracker_visits](../harness/verticals/retail/import_control_room_bundle.py#L534) | run_root, state, owner, scope | Project actual tracker presence through current source/camera authority. |
| [main](../harness/verticals/retail/import_control_room_bundle.py#L552) |  |  |
| [member](../harness/verticals/retail/import_control_room_bundle.py#L573) | owner |  |

### harness/verticals/retail/import_cosmos_response.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [load](../harness/verticals/retail/import_cosmos_response.py#L10) | path |  |
| [write](../harness/verticals/retail/import_cosmos_response.py#L15) | path, value |  |
| [main](../harness/verticals/retail/import_cosmos_response.py#L20) | argv |  |

### harness/verticals/retail/import_stream_response.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [main](../harness/verticals/retail/import_stream_response.py#L14) | argv |  |

### harness/verticals/retail/imported_media.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [imported_path](../harness/verticals/retail/imported_media.py#L35) | path |  |
| [imported_record](../harness/verticals/retail/imported_media.py#L44) | record |  |
| [require_sandbox_derivation](../harness/verticals/retail/imported_media.py#L48) | record, purpose |  |
| [_number](../harness/verticals/retail/imported_media.py#L53) | value, low, high |  |
| [_integer](../harness/verticals/retail/imported_media.py#L59) | value, low, high |  |
| [_identity](../harness/verticals/retail/imported_media.py#L65) | info |  |
| [path](../harness/verticals/retail/imported_media.py#L80) | self | Compatibility reference only; HTTP/vision consumers use open/read_bytes. |
| [open](../harness/verticals/retail/imported_media.py#L84) | self | Hash the held FD, check its identity, then rewind it for byte serving. |
| [read_bytes](../harness/verticals/retail/imported_media.py#L120) | self, maximum |  |
| [verify](../harness/verticals/retail/imported_media.py#L126) | self |  |
| [__init__](../harness/verticals/retail/imported_media.py#L142) | self, state |  |
| [_open](../harness/verticals/retail/imported_media.py#L148) | self, relative, sealed |  |
| [_authority](../harness/verticals/retail/imported_media.py#L174) | self, asset_id |  |
| [resolve](../harness/verticals/retail/imported_media.py#L202) | self, record |  |
| [_resolve](../harness/verticals/retail/imported_media.py#L208) | self, record |  |
| [frame_input](../harness/verticals/retail/imported_media.py#L303) | self, record | The available image is the first 640px playback frame, not a video verdict. |
| [byte_response](../harness/verticals/retail/imported_media.py#L312) | file, range_header, attachment | Range-capable HTTP response over a verified held FD, with bounded chunks. |
| [chunks](../harness/verticals/retail/imported_media.py#L339) |  |  |

### harness/verticals/retail/inspection_previews.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__repr__](../harness/verticals/retail/inspection_previews.py#L38) | self |  |
| [_identifier](../harness/verticals/retail/inspection_previews.py#L42) | value, clip |  |
| [_metadata](../harness/verticals/retail/inspection_previews.py#L49) | frame |  |
| [_jpeg](../harness/verticals/retail/inspection_previews.py#L69) | raw |  |
| [_current](../harness/verticals/retail/inspection_previews.py#L78) | guard |  |
| [_canonical](../harness/verticals/retail/inspection_previews.py#L88) | value |  |
| [_unique_object](../harness/verticals/retail/inspection_previews.py#L92) | pairs |  |
| [__init__](../harness/verticals/retail/inspection_previews.py#L102) | self, state, create |  |
| [__repr__](../harness/verticals/retail/inspection_previews.py#L108) | self |  |
| [_check_paths](../harness/verticals/retail/inspection_previews.py#L111) | self |  |
| [_initialize](../harness/verticals/retail/inspection_previews.py#L123) | self |  |
| [_descriptor](../harness/verticals/retail/inspection_previews.py#L154) | receipt_id, index, clip_id, metadata, sha256 |  |
| [save](../harness/verticals/retail/inspection_previews.py#L158) | self, owner_principal_id, chat_id, dataset, clip_id, frames, guard | Atomically admit up to four copied frames; call from drained host offload. |
| [get](../harness/verticals/retail/inspection_previews.py#L202) | self, owner_principal_id, receipt_id, index, chat_id | Read one private frame; absent/foreign scope returns None without writes. |
| [tool_previews](../harness/verticals/retail/inspection_previews.py#L234) | name, content, success | Project host inspection metadata, never arbitrary URLs or model image data. |

### harness/verticals/retail/intake_projection.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [public_import](../harness/verticals/retail/intake_projection.py#L24) | view |  |
| [__init__](../harness/verticals/retail/intake_projection.py#L49) | self, state, company_id, collections |  |
| [collections](../harness/verticals/retail/intake_projection.py#L55) | self, actor |  |
| [_rows](../harness/verticals/retail/intake_projection.py#L65) | self, actor, collection, allowed, limit, offset |  |
| [snapshot](../harness/verticals/retail/intake_projection.py#L89) | self, principal, collection, read_only, limit, offset |  |

### harness/verticals/retail/investigation_plans.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [meaningful_strings](../harness/verticals/retail/investigation_plans.py#L42) | self |  |
| [limits](../harness/verticals/retail/investigation_plans.py#L60) | self |  |
| [_now](../harness/verticals/retail/investigation_plans.py#L72) |  |  |
| [_digest](../harness/verticals/retail/investigation_plans.py#L76) | value |  |
| [__init__](../harness/verticals/retail/investigation_plans.py#L81) | self, state, index |  |
| [connect](../harness/verticals/retail/investigation_plans.py#L98) | self |  |
| [_snapshot](../harness/verticals/retail/investigation_plans.py#L104) | index |  |
| [_model](../harness/verticals/retail/investigation_plans.py#L117) | index |  |
| [_index_snapshot](../harness/verticals/retail/investigation_plans.py#L125) | self, index, dataset |  |
| [context](../harness/verticals/retail/investigation_plans.py#L143) | self, dataset |  |
| [save](../harness/verticals/retail/investigation_plans.py#L182) | self, dataset, chat_id, document |  |
| [get](../harness/verticals/retail/investigation_plans.py#L200) | self, plan_id, dataset, chat_id |  |
| [get_receipt](../harness/verticals/retail/investigation_plans.py#L207) | self, receipt_id, dataset, chat_id |  |
| [get_inspection](../harness/verticals/retail/investigation_plans.py#L214) | self, receipt_id, dataset, chat_id |  |
| [record_inspection](../harness/verticals/retail/investigation_plans.py#L221) | self, plan_id, dataset, chat_id, category_ids, question, clip_ids, result | Record a complete host inspection; model observations remain interpretations. |
| [_cached_encoder](../harness/verticals/retail/investigation_plans.py#L283) | self, index, model, stats |  |
| [encode](../harness/verticals/retail/investigation_plans.py#L284) | query |  |
| [_intervals](../harness/verticals/retail/investigation_plans.py#L304) | candidates |  |
| [retrieve](../harness/verticals/retail/investigation_plans.py#L321) | self, plan_id, dataset, chat_id, index, limit_per_query |  |

### harness/verticals/retail/library.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [read_json](../harness/verticals/retail/library.py#L20) | path, default |  |
| [__init__](../harness/verticals/retail/library.py#L28) | self, state, index |  |
| [catalog](../harness/verticals/retail/library.py#L35) | self |  |
| [folder](../harness/verticals/retail/library.py#L70) | value |  |
| [metadata](../harness/verticals/retail/library.py#L78) | self, path, record |  |
| [public_clip](../harness/verticals/retail/library.py#L118) | clip |  |
| [public_asset](../harness/verticals/retail/library.py#L125) | self, asset, include_clips |  |
| [listing](../harness/verticals/retail/library.py#L148) | self, collection, folder |  |
| [resolve](../harness/verticals/retail/library.py#L172) | self, asset_id, collection |  |
| [original](../harness/verticals/retail/library.py#L178) | self, asset_id, collection |  |
| [source_details](../harness/verticals/retail/library.py#L188) | self, record |  |
| [_results](../harness/verticals/retail/library.py#L191) | self |  |
| [_matching_result](../harness/verticals/retail/library.py#L213) | self, description, clip_id |  |
| [_input_metadata](../harness/verticals/retail/library.py#L232) | self, result_path, clip_id, sha256 |  |
| [descriptions](../harness/verticals/retail/library.py#L256) | self, record |  |

### harness/verticals/retail/link_download.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [require](../harness/verticals/retail/link_download.py#L39) | value, code |  |
| [validate_url](../harness/verticals/retail/link_download.py#L43) | value |  |
| [classify](../harness/verticals/retail/link_download.py#L49) | value |  |
| [media_magic](../harness/verticals/retail/link_download.py#L65) | data |  |
| [metadata](../harness/verticals/retail/link_download.py#L72) | headers, url, max_bytes |  |
| [chunks](../harness/verticals/retail/link_download.py#L98) | self |  |
| [__init__](../harness/verticals/retail/link_download.py#L112) | self, resolver, network_backend, ssl_context |  |
| [open](../harness/verticals/retail/link_download.py#L116) | self, url, current, max_bytes |  |

### harness/verticals/retail/link_intake.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [digest](../harness/verticals/retail/link_intake.py#L33) | value |  |
| [drain](../harness/verticals/retail/link_intake.py#L35) | task |  |
| [offload](../harness/verticals/retail/link_intake.py#L42) | fn, *args, **kwargs |  |
| [__init__](../harness/verticals/retail/link_intake.py#L49) | self, state, store, host, authorized, enabled, transport |  |
| [db](../harness/verticals/retail/link_intake.py#L63) | self, write |  |
| [_row](../harness/verticals/retail/link_intake.py#L75) | self, db, actor, identity |  |
| [_authority](../harness/verticals/retail/link_intake.py#L80) | self, actor, collection, write |  |
| [_public](../harness/verticals/retail/link_intake.py#L85) | self, row |  |
| [create](../harness/verticals/retail/link_intake.py#L101) | self, actor, collection, url, idempotency_key |  |
| [get](../harness/verticals/retail/link_intake.py#L120) | self, actor, identity |  |
| [list](../harness/verticals/retail/link_intake.py#L124) | self, actor, collection |  |
| [_current](../harness/verticals/retail/link_intake.py#L130) | self, actor, identity |  |
| [_lease](../harness/verticals/retail/link_intake.py#L140) | self, name |  |
| [_slot](../harness/verticals/retail/link_intake.py#L147) | self |  |
| [_update](../harness/verticals/retail/link_intake.py#L157) | self, actor, identity, **values |  |
| [start](../harness/verticals/retail/link_intake.py#L166) | self, actor, identity |  |
| [run](../harness/verticals/retail/link_intake.py#L176) | self, actor, identity |  |
| [rejected](../harness/verticals/retail/link_intake.py#L182) |  |  |
| [_run](../harness/verticals/retail/link_intake.py#L190) | self, actor, identity |  |
| [begin](../harness/verticals/retail/link_intake.py#L194) |  |  |
| [_recover_upload](../harness/verticals/retail/link_intake.py#L216) | self, actor, identity |  |
| [_acquire](../harness/verticals/retail/link_intake.py#L222) | self, actor, identity, row |  |
| [_finish_cancel](../harness/verticals/retail/link_intake.py#L258) | self, actor, identity |  |
| [cancel](../harness/verticals/retail/link_intake.py#L267) | self, actor, identity |  |
| [_cancel](../harness/verticals/retail/link_intake.py#L272) | self, actor, identity |  |
| [finish](../harness/verticals/retail/link_intake.py#L277) |  |  |
| [ready](../harness/verticals/retail/link_intake.py#L292) | self |  |
| [reconcile](../harness/verticals/retail/link_intake.py#L298) | self |  |
| [repair](../harness/verticals/retail/link_intake.py#L304) |  |  |
| [close](../harness/verticals/retail/link_intake.py#L314) | self |  |
| [member_current](../harness/verticals/retail/link_intake.py#L321) | state, access_state, environment, owner | Cheap host company-membership fence; browser logout is not revocation. |

### harness/verticals/retail/link_routes.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [public](../harness/verticals/retail/link_routes.py#L22) | value |  |
| [call](../harness/verticals/retail/link_routes.py#L27) | fn, *args, **kwargs |  |
| [register_link_routes](../harness/verticals/retail/link_routes.py#L38) | app, service_for_workspace |  |
| [context](../harness/verticals/retail/link_routes.py#L44) | request, write |  |
| [row](../harness/verticals/retail/link_routes.py#L65) | service, actor, identity, collections |  |
| [response](../harness/verticals/retail/link_routes.py#L69) | value, code |  |
| [listing](../harness/verticals/retail/link_routes.py#L71) | request |  |
| [create](../harness/verticals/retail/link_routes.py#L83) | request |  |
| [detail](../harness/verticals/retail/link_routes.py#L96) | identity, request |  |
| [retry](../harness/verticals/retail/link_routes.py#L100) | identity, request |  |
| [cancel](../harness/verticals/retail/link_routes.py#L106) | identity, request |  |

### harness/verticals/retail/location_context.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/verticals/retail/location_context.py#L131) | self, status |  |
| [context_enabled](../harness/verticals/retail/location_context.py#L136) | environ |  |
| [map_provider](../harness/verticals/retail/location_context.py#L143) | environ | The commissioned map provider and its key: Mapbox first, then Google; None keeps the tiles. |
| [claim_provider](../harness/verticals/retail/location_context.py#L155) | environ | Read the provider key once and take both names out of the environment, so no child process inherits it. |
| [host_ledger](../harness/verticals/retail/location_context.py#L166) | environ | The provider-call ledger every server process of this host's user shares; None where the user has no home. |
| [picture_request](../harness/verticals/retail/location_context.py#L178) | provider, secret, place, width, height | The one outside request for a picture: the shop's coordinates, the shape, the key. |
| [provider_png](../harness/verticals/retail/location_context.py#L191) | body, width, height | The provider's answer as one plain PNG of the asked shape at two pixels per point. |
| [kept_provider_png](../harness/verticals/retail/location_context.py#L210) | picture, width, height | True for a kept file that is still the PNG this service saved for that shape. |
| [valid_for](../harness/verticals/retail/location_context.py#L220) | headers | How long the provider says its picture stays valid, inside this service's bounds. |
| [__init__](../harness/verticals/retail/location_context.py#L237) | self, path, daily, monthly, clock |  |
| [_now](../harness/verticals/retail/location_context.py#L241) | self |  |
| [_counts](../harness/verticals/retail/location_context.py#L246) | table, stamp |  |
| [_write](../harness/verticals/retail/location_context.py#L253) | self, ledger |  |
| [_ledger](../harness/verticals/retail/location_context.py#L267) | self, write |  |
| [commission](../harness/verticals/retail/location_context.py#L285) | self | Make the ledger where none stands. True when this call made it; a standing ledger is left as it is. |
| [reserve](../harness/verticals/retail/location_context.py#L297) | self, count | Count these calls against the day and the month before they leave. False admits none of them. |
| [used](../harness/verticals/retail/location_context.py#L311) | self | Today's and this month's counts; a ledger that cannot be read reads as full. |
| [__init__](../harness/verticals/retail/location_context.py#L324) | self, path, caps, clock |  |
| [_day](../harness/verticals/retail/location_context.py#L330) | self |  |
| [_today](../harness/verticals/retail/location_context.py#L333) | self, ledger |  |
| [_ledger](../harness/verticals/retail/location_context.py#L343) | self, write |  |
| [reserve](../harness/verticals/retail/location_context.py#L363) | self, kind, count | Count these calls against today's cap before they leave. False admits none of them. |
| [used](../harness/verticals/retail/location_context.py#L375) | self, kind | Today's count; an unreadable ledger reads as a full day. |
| [_number](../harness/verticals/retail/location_context.py#L384) | value, low, high |  |
| [_optional](../harness/verticals/retail/location_context.py#L390) | value, low, high |  |
| [_stamp](../harness/verticals/retail/location_context.py#L394) | value, pattern |  |
| [checked](../harness/verticals/retail/location_context.py#L404) | raw | The upstream answer reduced to the measured values this product shows, each one in range. |
| [column](../harness/verticals/retail/location_context.py#L418) | table, name, count, convert |  |
| [code](../harness/verticals/retail/location_context.py#L424) | value |  |
| [flag](../harness/verticals/retail/location_context.py#L429) | value |  |
| [condition](../harness/verticals/retail/location_context.py#L462) | code, is_day |  |
| [city_of](../harness/verticals/retail/location_context.py#L467) | address, zone | The city a person would say for this address. Stored text only: no lookup. |
| [forecast](../harness/verticals/retail/location_context.py#L478) | saved, place, now, fetched, stale | The answer the page reads, cut to the hours and days ahead of this moment at the shop. |
| [hour](../harness/verticals/retail/location_context.py#L487) | index |  |
| [day](../harness/verticals/retail/location_context.py#L492) | index |  |
| [tile_position](../harness/verticals/retail/location_context.py#L520) | latitude, longitude, zoom | Fractional slippy-map tile coordinates of a point (Web Mercator). |
| [tile_block](../harness/verticals/retail/location_context.py#L529) | latitude, longitude, zoom | The 3x3 tiles around the shop and the shop's pixel inside that block. |
| [compose](../harness/verticals/retail/location_context.py#L538) | tiles, point | One square picture centred on the shop, cut from the 3x3 block. |
| [theme_tone](../harness/verticals/retail/location_context.py#L554) | path | The map tone the theme names (saturate, contrast, brightness), for this service to bake into the tiles' picture. |
| [find](../harness/verticals/retail/location_context.py#L561) | node |  |
| [toned](../harness/verticals/retail/location_context.py#L577) | image | The tiles' picture in the theme's quiet tone; the page shows every map picture as it arrives. |
| [credited](../harness/verticals/retail/location_context.py#L586) | picture, width, height | The picture at the asked shape, the shop still at its centre, the map's credit in its corner. |
| [lettering](../harness/verticals/retail/location_context.py#L595) | size |  |
| [__init__](../harness/verticals/retail/location_context.py#L626) | self, directory, transport, clock, enabled, provider, picture_ledger |  |
| [key](../harness/verticals/retail/location_context.py#L649) | place |  |
| [_lock](../harness/verticals/retail/location_context.py#L652) | self, kind, key |  |
| [_resting](../harness/verticals/retail/location_context.py#L655) | self, kind, key |  |
| [_keep](../harness/verticals/retail/location_context.py#L658) | self, table, key, value, limit |  |
| [_get](../harness/verticals/retail/location_context.py#L664) | self, client, url, params, limit | One bounded read: a 200 answer of at most `limit` bytes. |
| [_client](../harness/verticals/retail/location_context.py#L676) | self |  |
| [_fetch_weather](../harness/verticals/retail/location_context.py#L681) | self, place, key |  |
| [weather](../harness/verticals/retail/location_context.py#L697) | self, place |  |
| [answer](../harness/verticals/retail/location_context.py#L700) | saved, stale |  |
| [fresh](../harness/verticals/retail/location_context.py#L707) |  |  |
| [_picture_path](../harness/verticals/retail/location_context.py#L731) | self, key |  |
| [_saved_picture](../harness/verticals/retail/location_context.py#L735) | self, key |  |
| [_save_picture](../harness/verticals/retail/location_context.py#L738) | self, key, picture |  |
| [_saved](../harness/verticals/retail/location_context.py#L741) | self, key, path |  |
| [_save](../harness/verticals/retail/location_context.py#L754) | self, key, path, picture, stamp |  |
| [_fetch_picture](../harness/verticals/retail/location_context.py#L771) | self, place, key |  |
| [one](../harness/verticals/retail/location_context.py#L778) | client, column, row |  |
| [_fetch_provider](../harness/verticals/retail/location_context.py#L793) | self, place, key, width, height | One counted call: (picture, seconds it stays valid), or None with the shape at rest. |
| [_provider_picture](../harness/verticals/retail/location_context.py#L819) | self, place, width, height | The commissioned provider's picture of this shape, kept while the provider says it is valid. None hands the map to the tiles. |
| [kept](../harness/verticals/retail/location_context.py#L826) |  |  |
| [fresh](../harness/verticals/retail/location_context.py#L839) |  |  |
| [map](../harness/verticals/retail/location_context.py#L857) | self, place, width, height |  |
| [fresh](../harness/verticals/retail/location_context.py#L867) |  |  |
| [locate](../harness/verticals/retail/location_context.py#L890) | selected, owner, location_id | The session's location and its coordinates, read through the company's own stores. |
| [service_directory](../harness/verticals/retail/location_context.py#L931) | app | The service's own state directory, beside its transfer ledger. |
| [register_location_context_routes](../harness/verticals/retail/location_context.py#L937) | app, context | Two reads behind the control room's own session and company checks. |
| [place_of](../harness/verticals/retail/location_context.py#L946) | request, location_id |  |
| [location_weather](../harness/verticals/retail/location_context.py#L955) | request, location_id |  |
| [location_map](../harness/verticals/retail/location_context.py#L964) | request, location_id, width, height |  |
| [main](../harness/verticals/retail/location_context.py#L976) | argv | Host commands for the map provider's call ledger. |

### harness/verticals/retail/location_intelligence.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [encoded](../harness/verticals/retail/location_intelligence.py#L23) | value |  |
| [evidence](../harness/verticals/retail/location_intelligence.py#L36) | self |  |
| [provenance](../harness/verticals/retail/location_intelligence.py#L54) | self |  |
| [displayed_price](../harness/verticals/retail/location_intelligence.py#L60) | value |  |
| [payment_evidence](../harness/verticals/retail/location_intelligence.py#L69) | events |  |
| [identity](../harness/verticals/retail/location_intelligence.py#L89) | self |  |
| [sourced](../harness/verticals/retail/location_intelligence.py#L104) | self |  |
| [coordinates_from_weather](../harness/verticals/retail/location_intelligence.py#L114) | value | Import an existing sourced configuration; perform no geocoding or lookup. |
| [proof](../harness/verticals/retail/location_intelligence.py#L145) | self |  |
| [valid](../harness/verticals/retail/location_intelligence.py#L166) | self |  |
| [__init__](../harness/verticals/retail/location_intelligence.py#L178) | self, state, scope, monitoring, clock |  |
| [connect](../harness/verticals/retail/location_intelligence.py#L183) | self, write |  |
| [_rows](../harness/verticals/retail/location_intelligence.py#L198) | self, owner, kind |  |
| [_get](../harness/verticals/retail/location_intelligence.py#L203) | self, owner, kind, key |  |
| [_put](../harness/verticals/retail/location_intelligence.py#L209) | self, owner, kind, value, immutable |  |
| [authorized](../harness/verticals/retail/location_intelligence.py#L219) | self, owner, collection, location_id, write |  |
| [configure_location](../harness/verticals/retail/location_intelligence.py#L229) | self, owner, definition |  |
| [save_product](../harness/verticals/retail/location_intelligence.py#L240) | self, owner, definition |  |
| [_event_reader](../harness/verticals/retail/location_intelligence.py#L249) | self, owner | One read names every event's source; each source's access is decided once per caller. |
| [readable](../harness/verticals/retail/location_intelligence.py#L254) | source_id, dataset |  |
| [products](../harness/verticals/retail/location_intelligence.py#L262) | self, owner, collection, location_id, reader |  |
| [_event_place](../harness/verticals/retail/location_intelligence.py#L276) | self, owner, event |  |
| [_source_place](../harness/verticals/retail/location_intelligence.py#L283) | self, owner, source, collection |  |
| [ingest_tracks](../harness/verticals/retail/location_intelligence.py#L300) | self, owner, source_id, tracks, tracks_sha256 | Trusted host adapter for real tracker observations, independent of VLM events. |
| [ingest_event](../harness/verticals/retail/location_intelligence.py#L344) | self, owner, event, job_id |  |
| [_project_visit](../harness/verticals/retail/location_intelligence.py#L376) | self, owner, event |  |
| [resolve_location](../harness/verticals/retail/location_intelligence.py#L388) | self, owner, event |  |
| [catalog_products](../harness/verticals/retail/location_intelligence.py#L392) | self, owner, event |  |
| [apply_product_match](../harness/verticals/retail/location_intelligence.py#L396) | self, owner, event_id, match |  |
| [product_match](../harness/verticals/retail/location_intelligence.py#L410) | self, owner, event_id | Read a saved matching receipt; this endpoint starts no image work. |
| [save_daily_fact](../harness/verticals/retail/location_intelligence.py#L423) | self, owner, definition |  |
| [_metrics](../harness/verticals/retail/location_intelligence.py#L429) | events, facts |  |
| [total](../harness/verticals/retail/location_intelligence.py#L438) | field |  |
| [_projection](../harness/verticals/retail/location_intelligence.py#L454) | self, events, products, facts |  |
| [snapshot](../harness/verticals/retail/location_intelligence.py#L490) | self, owner, collection, now, scenario |  |

### harness/verticals/retail/location_intelligence_routes.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [register_location_intelligence_routes](../harness/verticals/retail/location_intelligence_routes.py#L7) | app |  |
| [location](../harness/verticals/retail/location_intelligence_routes.py#L11) | request, collection |  |
| [catalog](../harness/verticals/retail/location_intelligence_routes.py#L24) | request, collection, location_id |  |
| [visit_basket](../harness/verticals/retail/location_intelligence_routes.py#L38) | request, source_id, track_id, at_s |  |
| [current](../harness/verticals/retail/location_intelligence_routes.py#L63) |  |  |

### harness/verticals/retail/media.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/verticals/retail/media.py#L13) | self, state |  |
| [_derivatives](../harness/verticals/retail/media.py#L18) | self, owner_principal_id |  |
| [source_cut](../harness/verticals/retail/media.py#L26) | self, record, owner_principal_id |  |
| [inspect](../harness/verticals/retail/media.py#L30) | self, record, owner_principal_id |  |
| [clip](../harness/verticals/retail/media.py#L43) | self, record, source_resolution, owner_principal_id |  |
| [save_attachment](../harness/verticals/retail/media.py#L82) | self, data, name |  |

### harness/verticals/retail/media_derive.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_valid_number](../harness/verticals/retail/media_derive.py#L40) | value |  |
| [validate_request](../harness/verticals/retail/media_derive.py#L46) | asset_id, collection, clip_id, purpose, start, end, frame_seconds |  |
| [_command](../harness/verticals/retail/media_derive.py#L65) | source |  |
| [_audio_probe](../harness/verticals/retail/media_derive.py#L70) | source, work, limits, deadline |  |
| [_source_frame](../harness/verticals/retail/media_derive.py#L78) | index, timing, timebase, origin |  |
| [_file](../harness/verticals/retail/media_derive.py#L86) | path, maximum |  |
| [_video_metadata](../harness/verticals/retail/media_derive.py#L92) | path, work, limits, deadline |  |
| [derive](../harness/verticals/retail/media_derive.py#L117) | asset_id, collection, clip_id, purpose, start, end, frame_seconds, source, output, limits | Publish output/derived atomically; the caller owns scope and job fencing. |
| [_probe_image](../harness/verticals/retail/media_derive.py#L238) | path, work, limits, deadline |  |
| [main](../harness/verticals/retail/media_derive.py#L250) |  |  |

### harness/verticals/retail/media_exports.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_now](../harness/verticals/retail/media_exports.py#L47) |  |  |
| [_rational](../harness/verticals/retail/media_exports.py#L51) | value |  |
| [_fraction](../harness/verticals/retail/media_exports.py#L55) | value, minimum, maximum |  |
| [_text](../harness/verticals/retail/media_exports.py#L67) | value, limit, empty |  |
| [_safe_file](../harness/verticals/retail/media_exports.py#L74) | path, root | Only regular, nonsymlink files inside this host-selected company state. |
| [_fingerprint](../harness/verticals/retail/media_exports.py#L95) | path |  |
| [_public_reference](../harness/verticals/retail/media_exports.py#L100) | value |  |
| [_public_note](../harness/verticals/retail/media_exports.py#L113) | value, root, source, limit |  |
| [_check](../harness/verticals/retail/media_exports.py#L128) | stop |  |
| [_transfer](../harness/verticals/retail/media_exports.py#L133) | stop, source, destination, limit | Hash/copy in bounded chunks on a worker thread, with cooperative cancellation. |
| [_joined](../harness/verticals/retail/media_exports.py#L164) | task |  |
| [_thread](../harness/verticals/retail/media_exports.py#L177) | operation, *args |  |
| [_blocking](../harness/verticals/retail/media_exports.py#L189) | operation, *args | Join short state mutations before propagating cancellation to cleanup. |
| [_probe](../harness/verticals/retail/media_exports.py#L199) | path |  |
| [__init__](../harness/verticals/retail/media_exports.py#L227) | self, state, index, media |  |
| [connect](../harness/verticals/retail/media_exports.py#L248) | self |  |
| [_owner](../harness/verticals/retail/media_exports.py#L252) | owner |  |
| [_key](../harness/verticals/retail/media_exports.py#L258) | key |  |
| [_lock](../harness/verticals/retail/media_exports.py#L263) | self |  |
| [_save](../harness/verticals/retail/media_exports.py#L272) | self, record |  |
| [_admit](../harness/verticals/retail/media_exports.py#L279) | self, document, dataset, owner, duration |  |
| [_imported_source](../harness/verticals/retail/media_exports.py#L304) | self, record, owner |  |
| [_verified_receipt](../harness/verticals/retail/media_exports.py#L311) | self, identity, source_record, owner |  |
| [_selection](../harness/verticals/retail/media_exports.py#L317) | self, document, dataset, owner |  |
| [_public](../harness/verticals/retail/media_exports.py#L368) | record |  |
| [get](../harness/verticals/retail/media_exports.py#L375) | self, payload_id, owner_principal_id, dataset |  |
| [list](../harness/verticals/retail/media_exports.py#L386) | self, owner_principal_id, dataset |  |
| [download_path](../harness/verticals/retail/media_exports.py#L392) | self, payload_id, owner_principal_id, dataset |  |
| [recover](../harness/verticals/retail/media_exports.py#L401) | self | Call once at service startup. A live export's lock blocks recovery. |
| [_cleanup](../harness/verticals/retail/media_exports.py#L416) | self, key |  |
| [prepare](../harness/verticals/retail/media_exports.py#L424) | self, document, dataset, owner_principal_id |  |
| [_build](../harness/verticals/retail/media_exports.py#L467) | self, record, records, files, allowance, imported_checks |  |
| [_documents_and_zip](../harness/verticals/retail/media_exports.py#L577) | stop, files, archive, manifest, allowance |  |
| [fraction](../harness/verticals/retail/media_exports.py#L578) | value |  |
| [write](../harness/verticals/retail/media_exports.py#L579) | name, text |  |

### harness/verticals/retail/media_prepare.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/verticals/retail/media_prepare.py#L34) | self, code |  |
| [validate](../harness/verticals/retail/media_prepare.py#L57) | self |  |
| [_tree_bytes](../harness/verticals/retail/media_prepare.py#L65) | root |  |
| [_kill_reap](../harness/verticals/retail/media_prepare.py#L75) | process |  |
| [_run](../harness/verticals/retail/media_prepare.py#L83) | argv, work, limits, deadline, stdout_limit | Bound pipes using files, enforce wall/output budgets, kill the whole group. |
| [_probe](../harness/verticals/retail/media_prepare.py#L117) | source, work, limits, deadline, frames |  |
| [_regular](../harness/verticals/retail/media_prepare.py#L134) | path |  |
| [_hash_fd](../harness/verticals/retail/media_prepare.py#L146) | fd |  |
| [_hash](../harness/verticals/retail/media_prepare.py#L154) | path |  |
| [_number](../harness/verticals/retail/media_prepare.py#L162) | value |  |
| [_dimensions](../harness/verticals/retail/media_prepare.py#L172) | width, height, limits |  |
| [_source_metadata](../harness/verticals/retail/media_prepare.py#L179) | probe, frame_probe, limits |  |
| [embedding_batches](../harness/verticals/retail/media_prepare.py#L245) | clips | Match the existing Cosmos admission transport: 160 clips / 64 MiB. |
| [prepare](../harness/verticals/retail/media_prepare.py#L261) | asset_id, collection, source, output, limits | Return manifest after atomic publish to output/prepared. Caller owns tenancy. |
| [main](../harness/verticals/retail/media_prepare.py#L386) |  |  |

### harness/verticals/retail/modal_embed.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_load_clips](../harness/verticals/retail/modal_embed.py#L49) | paths |  |
| [_embed_batch](../harness/verticals/retail/modal_embed.py#L80) | clips, queries, export_text | One remote input; imports and all model work stay inside the GPU worker. |
| [__init__](../harness/verticals/retail/modal_embed.py#L157) | self, bert, projection |  |
| [forward](../harness/verticals/retail/modal_embed.py#L162) | self, input_ids, attention_mask |  |
| [_create_worker](../harness/verticals/retail/modal_embed.py#L222) | modal, small_batch |  |
| [main](../harness/verticals/retail/modal_embed.py#L247) | argv |  |

### harness/verticals/retail/monitoring.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [is_reference_event](../harness/verticals/retail/monitoring.py#L18) | value |  |
| [unique](../harness/verticals/retail/monitoring.py#L39) | self |  |
| [valid_geometry](../harness/verticals/retail/monitoring.py#L65) | self |  |
| [bounds](../harness/verticals/retail/monitoring.py#L91) | self |  |
| [__init__](../harness/verticals/retail/monitoring.py#L96) | self, state, source_lookup |  |
| [connect](../harness/verticals/retail/monitoring.py#L110) | self |  |
| [owner](../harness/verticals/retail/monitoring.py#L113) | owner |  |
| [register_source](../harness/verticals/retail/monitoring.py#L117) | self, owner, descriptor | Called by the host only after it verifies the imported bytes and routes. |
| [registered_source](../harness/verticals/retail/monitoring.py#L129) | self, owner, key |  |
| [registered_sources](../harness/verticals/retail/monitoring.py#L133) | self, owner, dataset |  |
| [registered_datasets](../harness/verticals/retail/monitoring.py#L137) | self, owner |  |
| [save_profile](../harness/verticals/retail/monitoring.py#L140) | self, owner, definition, datasets, profile_id, expected_revision |  |
| [get_profile](../harness/verticals/retail/monitoring.py#L160) | self, owner, key, revision |  |
| [list_profiles](../harness/verticals/retail/monitoring.py#L170) | self, owner, dataset |  |
| [source](../harness/verticals/retail/monitoring.py#L175) | self, owner, key, dataset |  |
| [commit_event](../harness/verticals/retail/monitoring.py#L179) | self, owner, definition, origin |  |
| [list_events](../harness/verticals/retail/monitoring.py#L219) | self, owner, dataset, profile_ids, event_types, limit, after, exclude_ids, oldest_first, include_reference |  |
| [event_sources](../harness/verticals/retail/monitoring.py#L237) | self, owner | Each of the owner's events as (source, dataset, origin, review state), in one read. |
| [get_event](../harness/verticals/retail/monitoring.py#L246) | self, owner, key |  |
| [validate_definition](../harness/verticals/retail/monitoring.py#L251) | self, definition |  |
| [events_for](../harness/verticals/retail/monitoring.py#L255) | self, definition |  |
| [readiness](../harness/verticals/retail/monitoring.py#L259) | self, definition |  |
| [resolve_monitoring_source](../harness/verticals/retail/monitoring.py#L265) | selected, owner, key, chat_id | Resolve current source and optional conversation grants before returning evidence. |
| [available_monitoring_datasets](../harness/verticals/retail/monitoring.py#L286) | selected, owner |  |
| [monitoring_profile_authorized](../harness/verticals/retail/monitoring.py#L290) | selected, owner, record |  |

### harness/verticals/retail/monitoring_routes.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [phone_default](../harness/verticals/retail/monitoring_routes.py#L26) | selected, record | Phone chat is a default capability of every Tracking Agent. |
| [promotion](../harness/verticals/retail/monitoring_routes.py#L40) | selected, chat_id, kind, definition, allow_active |  |
| [observation_detail](../harness/verticals/retail/monitoring_routes.py#L60) | selected, record, reader, guards |  |
| [shown_presentation](../harness/verticals/retail/monitoring_routes.py#L79) | selected, record, reader, guards | What a Tracking Agent's canvas draws beside its events, once its tracker has a record. |
| [assembled](../harness/verticals/retail/monitoring_routes.py#L118) | selected, record, tracker, page | A company tracker's row and canvas as the page would carry them now, from its stored output and readings. |
| [published_page](../harness/verticals/retail/monitoring_routes.py#L131) | state, owner | What the owner's published page holds of the company's own trackers, read once per version of the page: each tracker's tile row with its canvas, the page's currency and the location it shows. |
| [register_monitoring_routes](../harness/verticals/retail/monitoring_routes.py#L154) | app |  |
| [actor](../harness/verticals/retail/monitoring_routes.py#L157) | request, write |  |
| [allowed](../harness/verticals/retail/monitoring_routes.py#L163) | request, record, write |  |
| [execute](../harness/verticals/retail/monitoring_routes.py#L170) | fn, *args, **kwargs |  |
| [execute_save](../harness/verticals/retail/monitoring_routes.py#L173) | fn, *args, **kwargs | A person's save, answered in a person's words. A presentation someone saved in between answers 409, so the page reads it and sends the pick once more; a tracker still to get its location answers 409 too, and the page keeps what it holds; a canvas the output leaves unfilled answers the sentence its control shows. |
| [profiles](../harness/verticals/retail/monitoring_routes.py#L187) | request, dataset |  |
| [create_profile](../harness/verticals/retail/monitoring_routes.py#L194) | body, request |  |
| [profile](../harness/verticals/retail/monitoring_routes.py#L199) | profile_id, request, revision |  |
| [update_profile](../harness/verticals/retail/monitoring_routes.py#L203) | profile_id, body, request |  |
| [events](../harness/verticals/retail/monitoring_routes.py#L209) | request, dataset, profile_id, limit, after, evaluation |  |
| [event](../harness/verticals/retail/monitoring_routes.py#L216) | event_id, request, evaluation |  |
| [commit_event](../harness/verticals/retail/monitoring_routes.py#L222) | body, request |  |
| [observations](../harness/verticals/retail/monitoring_routes.py#L227) | agent_id, request |  |
| [save_presentation](../harness/verticals/retail/monitoring_routes.py#L232) | agent_id, body, request | A person's change of a Tracking Agent's tile or canvas: the same save as the harness's save_tracker_presentation. The agent's own record stays as it is, so a running agent keeps running. |
| [promote](../harness/verticals/retail/monitoring_routes.py#L243) | chat_id, body, request |  |

### harness/verticals/retail/monitoring_tools.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [tool](../harness/verticals/retail/monitoring_tools.py#L25) | name, description, properties, required |  |
| [observation_specs](../harness/verticals/retail/monitoring_tools.py#L29) | write |  |
| [specs](../harness/verticals/retail/monitoring_tools.py#L48) | write |  |
| [scoped](../harness/verticals/retail/monitoring_tools.py#L51) | store, index, host, chat_id |  |
| [lookup](../harness/verticals/retail/monitoring_tools.py#L53) | owner, key |  |
| [family_of](../harness/verticals/retail/monitoring_tools.py#L75) | name |  |
| [declared](../harness/verticals/retail/monitoring_tools.py#L78) | family, name, args | A family tool's arguments, checked against the schema the tool itself declares. MCP checks them on its way in; the hosted chat hands them over as the model wrote them. |
| [read](../harness/verticals/retail/monitoring_tools.py#L87) | store, owner, dataset, name, args, agents |  |
| [admit_event_history](../harness/verticals/retail/monitoring_tools.py#L104) | agent, chat_id, events |  |
| [_admit](../harness/verticals/retail/monitoring_tools.py#L114) | family, agent, chat_id, scope, name, args, run, store, origin | What every family tool passes before its handler: a current member, the declared fields, and for a write the active parent conversation. Returns the handler's context and its arguments. |
| [call_async](../harness/verticals/retail/monitoring_tools.py#L128) | agent, chat_id, scope, name, args, run, index | A family write that waits on the event loop (`ASYNC_NAMES`): the checks of `call`, then the family's `acall`. The hosted conversation awaits it, so the wait holds no worker thread and follows the turn's stop. |
| [admitted](../harness/verticals/retail/monitoring_tools.py#L133) |  |  |
| [call](../harness/verticals/retail/monitoring_tools.py#L144) | agent, chat_id, scope, name, args, run, index |  |
| [tracker_specs](../harness/verticals/retail/monitoring_tools.py#L208) | write |  |
| [_schedule](../harness/verticals/retail/monitoring_tools.py#L235) | state, tracker, service | A location's schedule as a tool returns it; for one of the company's own trackers, its own automatic setting. `service` is the tracker service's note for this company: on, off, or waiting for its first sweep. |
| [_run_rows](../harness/verticals/retail/monitoring_tools.py#L244) | context, location_id, rows | A location's run rows for this reader. The counts a pass derived add up every camera of the location, so they are read with those cameras, like the outputs. |
| [_run_of](../harness/verticals/retail/monitoring_tools.py#L251) | run, key | One run as it concerns one tracker. |
| [_script](../harness/verticals/retail/monitoring_tools.py#L260) | context, row | A tracker's processing script as get_tracker returns it: the record's processor layer, and for a saved script its revision, policy, health and last test. |
| [_trackers](../harness/verticals/retail/monitoring_tools.py#L266) | context, location_id | The listing rows of `list_monitoring_profiles`, each with its schedule, output summary and last run. |
| [place](../harness/verticals/retail/monitoring_tools.py#L275) | key |  |
| [covered](../harness/verticals/retail/monitoring_tools.py#L278) | key, cameras |  |
| [_other_installation](../harness/verticals/retail/monitoring_tools.py#L297) | context, location_id, runs | A location the reader manages whose trackers run as another member, once that member's passes have stopped: the schedule and the last run of that installation, and the next step. |
| [tracker_read](../harness/verticals/retail/monitoring_tools.py#L311) | context, name, args |  |
| [readable](../harness/verticals/retail/monitoring_tools.py#L332) | entry |  |
| [tracker_call](../harness/verticals/retail/monitoring_tools.py#L345) | context, name, args |  |
| [present](../harness/verticals/retail/monitoring_tools.py#L445) | *names |  |
| [registry](../harness/verticals/retail/monitoring_tools.py#L450) | families | The read and the write names of every tool here, checked as the module loads. |
| [observation_read](../harness/verticals/retail/monitoring_tools.py#L468) | context, name, arguments |  |
| [observation_call](../harness/verticals/retail/monitoring_tools.py#L476) | context, name, arguments |  |

### harness/verticals/retail/mv3dt_dataset.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_identifier](../harness/verticals/retail/mv3dt_dataset.py#L34) | value |  |
| [_number](../harness/verticals/retail/mv3dt_dataset.py#L40) | value, minimum, maximum |  |
| [__init__](../harness/verticals/retail/mv3dt_dataset.py#L47) | self, root |  |
| [remaining](../harness/verticals/retail/mv3dt_dataset.py#L53) | self |  |
| [resolve](../harness/verticals/retail/mv3dt_dataset.py#L59) | self, relative |  |
| [verify](../harness/verticals/retail/mv3dt_dataset.py#L70) | self, reference, maximum |  |
| [receipt](../harness/verticals/retail/mv3dt_dataset.py#L101) | self, reference, camera, kind |  |
| [_probe_bytes](../harness/verticals/retail/mv3dt_dataset.py#L115) | command, timeout | Bound actual pipe reads, including malformed files with excessive video tracks. |
| [probe_video](../harness/verticals/retail/mv3dt_dataset.py#L142) | path, timeout | Read bounded MP4 metadata with ffprobe; this does not run a decoder/model. |
| [compose_node](../harness/verticals/retail/mv3dt_dataset.py#L175) | self, parent, index |  |
| [construct_mapping](../harness/verticals/retail/mv3dt_dataset.py#L180) | self, node, deep |  |
| [_calibration](../harness/verticals/retail/mv3dt_dataset.py#L187) | path, detector |  |
| [determinant](../harness/verticals/retail/mv3dt_dataset.py#L202) | columns |  |
| [_clock](../harness/verticals/retail/mv3dt_dataset.py#L228) | body, media, policy |  |
| [_frame_clock](../harness/verticals/retail/mv3dt_dataset.py#L262) | body, media | Validate retained full-file probes; never synthesize timing from average FPS. |
| [_qualification](../harness/verticals/retail/mv3dt_dataset.py#L313) | files, request, pending |  |
| [preflight](../harness/verticals/retail/mv3dt_dataset.py#L361) | dataset_root, request | Validate explicit host mappings; absent qualification evidence stays pending. |
| [main](../harness/verticals/retail/mv3dt_dataset.py#L578) |  |  |

### harness/verticals/retail/playback_media.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [safe_relative](../harness/verticals/retail/playback_media.py#L53) | self |  |
| [files](../harness/verticals/retail/playback_media.py#L80) | self |  |
| [unique_mappings](../harness/verticals/retail/playback_media.py#L99) | self |  |
| [__init__](../harness/verticals/retail/playback_media.py#L110) | self, state, owner |  |
| [catalog](../harness/verticals/retail/playback_media.py#L115) | self |  |
| [file](../harness/verticals/retail/playback_media.py#L123) | self, spec, kind |  |
| [sealed](../harness/verticals/retail/playback_media.py#L128) | self, specs | Each reference is a private, read-only regular file of its declared length. |
| [resolver](../harness/verticals/retail/playback_media.py#L143) | request, context |  |
| [_catalog](../harness/verticals/retail/playback_media.py#L155) | request, context |  |
| [_match](../harness/verticals/retail/playback_media.py#L163) | artifact, binding |  |
| [_text](../harness/verticals/retail/playback_media.py#L173) | value, maximum |  |
| [_location](../harness/verticals/retail/playback_media.py#L177) | selected, context, catalog | The location record of this session's cameras, read through the company's own stores. |
| [_error](../harness/verticals/retail/playback_media.py#L233) | exc, refused | Stable sanitized outcomes; the selected authority stays selected in every one. |
| [maintained_bootstrap](../harness/verticals/retail/playback_media.py#L245) | request |  |
| [_admit](../harness/verticals/retail/playback_media.py#L295) | request, address | One complete decision: session identity, sealed catalog and current PostgreSQL lineage. |
| [maintained_media](../harness/verticals/retail/playback_media.py#L315) | request, asset |  |
| [current](../harness/verticals/retail/playback_media.py#L336) |  |  |
| [guarded](../harness/verticals/retail/playback_media.py#L344) |  |  |

### harness/verticals/retail/presentation_captions.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [enrich](../harness/verticals/retail/presentation_captions.py#L7) | agent, chat_id, run, collection, index, presentation |  |
| [current](../harness/verticals/retail/presentation_captions.py#L12) |  |  |
| [emit](../harness/verticals/retail/presentation_captions.py#L38) | event |  |

### harness/verticals/retail/qdrant_retrieval.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [point_id](../harness/verticals/retail/qdrant_retrieval.py#L33) | clip_id |  |
| [redirect_request](../harness/verticals/retail/qdrant_retrieval.py#L38) | self, *args, **kwargs |  |
| [__init__](../harness/verticals/retail/qdrant_retrieval.py#L44) | self, url, timeout |  |
| [request](../harness/verticals/retail/qdrant_retrieval.py#L54) | self, method, path, body, allow_missing |  |
| [__init__](../harness/verticals/retail/qdrant_retrieval.py#L85) | self, state, url, client |  |
| [publish_snapshot](../harness/verticals/retail/qdrant_retrieval.py#L99) | cls, state, snapshot, client, promote | Publish a HOST-staged immutable snapshot without changing reader state. |
| [_loaded_fingerprint](../harness/verticals/retail/qdrant_retrieval.py#L125) | self |  |
| [_base_filter](../harness/verticals/retail/qdrant_retrieval.py#L143) | self, fingerprint |  |
| [_publish_loaded](../harness/verticals/retail/qdrant_retrieval.py#L150) | self, promote |  |
| [_check_source_generation](../harness/verticals/retail/qdrant_retrieval.py#L214) | self |  |
| [refresh](../harness/verticals/retail/qdrant_retrieval.py#L220) | self |  |
| [search_vector](../harness/verticals/retail/qdrant_retrieval.py#L235) | self, vector, limit, dataset | Search a matching text vector; also allows isolated lookup benchmarking. |
| [search](../harness/verticals/retail/qdrant_retrieval.py#L279) | self, query, limit, dataset |  |
| [status](../harness/verticals/retail/qdrant_retrieval.py#L286) | self |  |
| [main](../harness/verticals/retail/qdrant_retrieval.py#L294) |  |  |

### harness/verticals/retail/query_budget.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_now](../harness/verticals/retail/query_budget.py#L33) |  |  |
| [_money](../harness/verticals/retail/query_budget.py#L37) | value |  |
| [__init__](../harness/verticals/retail/query_budget.py#L50) | self, approval_path, workspace |  |
| [_locked](../harness/verticals/retail/query_budget.py#L57) | self, planned |  |
| [_read_ledger](../harness/verticals/retail/query_budget.py#L102) | self |  |
| [_write_ledger](../harness/verticals/retail/query_budget.py#L117) | self, ledger |  |
| [_summary](../harness/verticals/retail/query_budget.py#L135) | ledger |  |
| [status](../harness/verticals/retail/query_budget.py#L144) | self |  |
| [reserve](../harness/verticals/retail/query_budget.py#L148) | self, planned_gross_usd, request_id |  |
| [_entry](../harness/verticals/retail/query_budget.py#L168) | ledger, reservation_id |  |
| [mark_started](../harness/verticals/retail/query_budget.py#L174) | self, reservation_id, resource_profile |  |
| [complete](../harness/verticals/retail/query_budget.py#L181) | self, reservation_id, runtime_estimate_usd, timing, billing_snapshot |  |
| [attach_app](../harness/verticals/retail/query_budget.py#L193) | self, reservation_id, app_id | Persist app identity before inference so failures can reconcile later. |
| [fail](../harness/verticals/retail/query_budget.py#L205) | self, reservation_id, reason |  |
| [cancel_before_remote](../harness/verticals/retail/query_budget.py#L212) | self, reservation_id |  |
| [reconcile_modal](../harness/verticals/retail/query_budget.py#L219) | self, reservation_id, app_id | Autonomously reconcile using authenticated provider evidence. |
| [reconcile_pending](../harness/verticals/retail/query_budget.py#L247) | self | Retry delayed provider reads automatically before later admissions. |
| [_apply_provider_evidence](../harness/verticals/retail/query_budget.py#L262) | self, reservation_id, app_id, evidence | Pure accounting step; production evidence comes from Modal above. |
| [reconcile](../harness/verticals/retail/query_budget.py#L304) | self, reservation_id, provider_evidence_path | Release unused credit only with a private, verified app-charge record. |
| [_modal_app_evidence](../harness/verticals/retail/query_budget.py#L329) | workspace_name, app_id | Read provider state, current rates, and per-app costs without mutations. |
| [read_app](../harness/verticals/retail/query_budget.py#L342) |  |  |

### harness/verticals/retail/realtime_read_routes.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [read_authority](../harness/verticals/retail/realtime_read_routes.py#L26) | environ |  |
| [_load_backend](../harness/verticals/retail/realtime_read_routes.py#L35) |  | Use the reviewed artifact closure, or the same checkout during development. |
| [maintained_lifespan](../harness/verticals/retail/realtime_read_routes.py#L53) | app | Open one restricted pool per service lifetime; startup never imports data. |
| [_saved_company](../harness/verticals/retail/realtime_read_routes.py#L69) | selected |  |
| [_context](../harness/verticals/retail/realtime_read_routes.py#L79) | request |  |
| [register_realtime_read_routes](../harness/verticals/retail/realtime_read_routes.py#L112) | app, authority |  |
| [read](../harness/verticals/retail/realtime_read_routes.py#L125) | request, source_id, identity, at_s, epoch |  |
| [legacy_basket](../harness/verticals/retail/realtime_read_routes.py#L152) | request |  |
| [epoch_snapshot](../harness/verticals/retail/realtime_read_routes.py#L157) | request, source_id, epoch_id, at_s |  |
| [asset_snapshot](../harness/verticals/retail/realtime_read_routes.py#L166) | request, source_id, asset_id, at_s |  |

### harness/verticals/retail/retail_agent_inputs.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [validate_schedule](../harness/verticals/retail/retail_agent_inputs.py#L43) | self |  |
| [inspection_ceiling](../harness/verticals/retail/retail_agent_inputs.py#L66) |  |  |
| [_capture_interval](../harness/verticals/retail/retail_agent_inputs.py#L71) | source | Use only explicit imported wall-clock provenance, never file/index times. |
| [timestamp](../harness/verticals/retail/retail_agent_inputs.py#L73) | value |  |
| [evidence_scope](../harness/verticals/retail/retail_agent_inputs.py#L90) | definition, sources, source_records, now |  |
| [__init__](../harness/verticals/retail/retail_agent_inputs.py#L126) | self, monitoring, index, live_input_ready |  |
| [attach](../harness/verticals/retail/retail_agent_inputs.py#L132) | self, store |  |
| [bind](../harness/verticals/retail/retail_agent_inputs.py#L144) | self, index, live_input_ready |  |
| [normalize](../harness/verticals/retail/retail_agent_inputs.py#L151) | self, record, table |  |
| [collection_allowed](../harness/verticals/retail/retail_agent_inputs.py#L162) | self, spec, datasets, owner |  |
| [validate_definition](../harness/verticals/retail/retail_agent_inputs.py#L166) | self, spec |  |
| [definition_context](../harness/verticals/retail/retail_agent_inputs.py#L172) | self, agent, chat_id, arguments |  |
| [prepare_record](../harness/verticals/retail/retail_agent_inputs.py#L181) | self, record, context |  |
| [runnable](../harness/verticals/retail/retail_agent_inputs.py#L188) | self, record |  |
| [validate_activation](../harness/verticals/retail/retail_agent_inputs.py#L191) | self, record |  |
| [resource_ceiling](../harness/verticals/retail/retail_agent_inputs.py#L198) | self |  |
| [resource_allowance](../harness/verticals/retail/retail_agent_inputs.py#L201) | self, definition |  |
| [validate_resource_budget](../harness/verticals/retail/retail_agent_inputs.py#L204) | self, definition, runs |  |
| [resource_admitted](../harness/verticals/retail/retail_agent_inputs.py#L212) | self, run |  |
| [describe](../harness/verticals/retail/retail_agent_inputs.py#L215) | self, record, db |  |
| [recovered](../harness/verticals/retail/retail_agent_inputs.py#L228) | self, db, run |  |
| [finished](../harness/verticals/retail/retail_agent_inputs.py#L231) | self, db, run, status |  |
| [claimed](../harness/verticals/retail/retail_agent_inputs.py#L234) | self, db, record, run |  |
| [prepare_screening](../harness/verticals/retail/retail_agent_inputs.py#L238) | self, key, sources, source_records, now, force |  |
| [screening_failed](../harness/verticals/retail/retail_agent_inputs.py#L251) | self, key, revision, error |  |
| [select](../harness/verticals/retail/retail_agent_inputs.py#L258) | self, db, record, sources, source_records, screening, now, wake |  |
| [validate_wake](../harness/verticals/retail/retail_agent_inputs.py#L341) | self, record, definition |  |
| [refresh](../harness/verticals/retail/retail_agent_inputs.py#L353) | self, definitions |  |
| [sources](../harness/verticals/retail/retail_agent_inputs.py#L357) | self, dataset |  |
| [ready](../harness/verticals/retail/retail_agent_inputs.py#L360) | self, definition, wake, agent, input_optional |  |
| [prepare](../harness/verticals/retail/retail_agent_inputs.py#L367) | self, definition, wake, agent |  |
| [execution](../harness/verticals/retail/retail_agent_inputs.py#L403) | self, definition |  |
| [recurring_ready](../harness/verticals/retail/retail_agent_inputs.py#L417) | self, collection, principal |  |
| [context](../harness/verticals/retail/retail_agent_inputs.py#L426) | self, agent, run, snapshot |  |

### harness/verticals/retail/retail_business.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [safe_description](../harness/verticals/retail/retail_business.py#L26) | self |  |
| [__init__](../harness/verticals/retail/retail_business.py#L35) | self, state, index, collections |  |
| [_collection_exists](../harness/verticals/retail/retail_business.py#L39) | self, collection |  |
| [_initial](../harness/verticals/retail/retail_business.py#L44) | self, collection |  |
| [_present](../harness/verticals/retail/retail_business.py#L51) | self, record |  |
| [update_settings](../harness/verticals/retail/retail_business.py#L54) | self, collection, expected_revision, settings |  |
| [change](../harness/verticals/retail/retail_business.py#L59) | current, revision, timestamp |  |
| [save_connection](../harness/verticals/retail/retail_business.py#L63) | self, collection, body |  |
| [change](../harness/verticals/retail/retail_business.py#L65) | current, revision, timestamp |  |
| [install_business](../harness/verticals/retail/retail_business.py#L77) | selected |  |
| [register_routes](../harness/verticals/retail/retail_business.py#L94) | app |  |
| [business_settings](../harness/verticals/retail/retail_business.py#L99) | body, request |  |
| [business_connection](../harness/verticals/retail/retail_business.py#L107) | body, request |  |

### harness/verticals/retail/retail_business_scope.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/verticals/retail/retail_business_scope.py#L25) | self, state, company_id, member, members, source_authorized, clock |  |
| [_db](../harness/verticals/retail/retail_business_scope.py#L31) | self, write |  |
| [_graph](../harness/verticals/retail/retail_business_scope.py#L60) | db, collection |  |
| [_effective](../harness/verticals/retail/retail_business_scope.py#L64) | self, actor, member, graph, revision, collection, locations |  |
| [effective](../harness/verticals/retail/retail_business_scope.py#L90) | self, actor, collection, location_ids |  |
| [describe](../harness/verticals/retail/retail_business_scope.py#L96) | self, actor, collection |  |
| [camera](../harness/verticals/retail/retail_business_scope.py#L128) | self, actor, collection, camera_id, manage |  |
| [mutate](../harness/verticals/retail/retail_business_scope.py#L135) | self, actor, collection, kind, value, expected_revision |  |
| [_event](../harness/verticals/retail/retail_business_scope.py#L209) | self, db, collection, revision, actor, kind, record_id, value |  |
| [events](../harness/verticals/retail/retail_business_scope.py#L214) | self, actor, collection, after, limit |  |
| [bind_chat](../harness/verticals/retail/retail_business_scope.py#L224) | self, actor, chat_id, collection, location_ids, expected_revision, expected_selection_revision |  |
| [chat_scope](../harness/verticals/retail/retail_business_scope.py#L242) | self, actor, chat_id, collection |  |
| [history](../harness/verticals/retail/retail_business_scope.py#L255) | self, chat_id |  |
| [admit_history](../harness/verticals/retail/retail_business_scope.py#L262) | self, actor, chat_id, scopes, source_ids, legacy | Bind all admitted context before any model/tool can expose it. |
| [current](../harness/verticals/retail/retail_business_scope.py#L298) | self, actor, collection, revision, account_role, chat_id, selection_revision | Cheap fail-closed fence for a previously admitted tool/media result. |
| [legacy_scope_current](../harness/verticals/retail/retail_business_scope.py#L325) | state, collection | Legacy local MCP has no live member resolver: configured scope uses HTTP. |

### harness/verticals/retail/retail_dataset_reference.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [associate_subject](../harness/verticals/retail/retail_dataset_reference.py#L18) | metadata, view, mapping, tracks, start, end |  |
| [reference_windows](../harness/verticals/retail/retail_dataset_reference.py#L40) | run_root, records, profile |  |

### harness/verticals/retail/retail_demo_history.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [event](../harness/verticals/retail/retail_demo_history.py#L44) | person, kind, start, end, reference, item, where, evidence | One event with every field a Cosmos answer event carries. |
| [visitor](../harness/verticals/retail/retail_demo_history.py#L52) | rng, person, products, counter, hour | One visitor's events inside a recording, and the seconds the tracker sees them. |
| [step](../harness/verticals/retail/retail_demo_history.py#L60) | kind, seconds, reference, item, evidence, where |  |
| [take](../harness/verticals/retail/retail_demo_history.py#L65) |  |  |
| [tracker_frames](../harness/verticals/retail/retail_demo_history.py#L100) | people, duration | Two frames per second; each visible person has one box that moves along the aisle. |
| [plan](../harness/verticals/retail/retail_demo_history.py#L115) | products, last_day, days, seed, last_day_until | The deterministic history: one entry per recording, oldest first. |
| [generate](../harness/verticals/retail/retail_demo_history.py#L170) | company, location_id, room_id, last_day, days, camera, seed, last_day_until | Write the planned history into the location through the ordinary ingestion. Safe to repeat. |

### harness/verticals/retail/retail_host.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [public_corpus](../harness/verticals/retail/retail_host.py#L23) | index |  |
| [__init__](../harness/verticals/retail/retail_host.py#L36) | self, host, selected |  |
| [participant_delivery_current](../harness/verticals/retail/retail_host.py#L43) | self, chat_id |  |
| [read_admission](../harness/verticals/retail/retail_host.py#L51) | self, actor, collection |  |
| [tool_context](../harness/verticals/retail/retail_host.py#L62) | self, context |  |
| [result_fields](../harness/verticals/retail/retail_host.py#L66) | self, name, content, success |  |
| [status_fields](../harness/verticals/retail/retail_host.py#L70) | self |  |
| [budget_fields](../harness/verticals/retail/retail_host.py#L77) | self |  |
| [member_cards](../harness/verticals/retail/retail_host.py#L85) | self, actor, collection, rows |  |
| [business_fields](../harness/verticals/retail/retail_host.py#L88) | self, actor, collection, value |  |
| [provider_usage](../harness/verticals/retail/retail_host.py#L91) | self |  |
| [available_credit](../harness/verticals/retail/retail_host.py#L94) | self |  |
| [agent_capabilities](../harness/verticals/retail/retail_host.py#L99) | self |  |
| [validate_activation](../harness/verticals/retail/retail_host.py#L103) | self, definition, once |  |
| [usage_fields](../harness/verticals/retail/retail_host.py#L113) | self |  |
| [authorize_file](../harness/verticals/retail/retail_host.py#L123) | self, request, file_id, principal |  |
| [file_download](../harness/verticals/retail/retail_host.py#L126) | self, record, principal |  |
| [plans](../harness/verticals/retail/retail_host.py#L129) | self |  |
| [public_clip](../harness/verticals/retail/retail_host.py#L133) | self, record |  |
| [inspection_metadata](../harness/verticals/retail/retail_host.py#L137) | self, record, frames, include_observations |  |
| [clip_attachments](../harness/verticals/retail/retail_host.py#L141) | self, ids, dataset |  |
| [connector_details](../harness/verticals/retail/retail_host.py#L145) | self, saved, connector_id, owner, collection |  |
| [connection_fields](../harness/verticals/retail/retail_host.py#L149) | self, value, principal, request |  |
| [catalogue](../harness/verticals/retail/retail_host.py#L159) | self |  |
| [draft_agent](../harness/verticals/retail/retail_host.py#L163) | self, template_id, collection, principal |  |
| [source_options](../harness/verticals/retail/retail_host.py#L167) | self, principal, collection |  |
| [request_scope](../harness/verticals/retail/retail_host.py#L170) | self, request |  |
| [tick](../harness/verticals/retail/retail_host.py#L173) | self |  |
| [close](../harness/verticals/retail/retail_host.py#L177) | self |  |
| [session_fields](../harness/verticals/retail/retail_host.py#L181) | self |  |
| [source_host](../harness/verticals/retail/retail_host.py#L187) | self |  |
| [source_store](../harness/verticals/retail/retail_host.py#L196) | self |  |
| [storage_runtime](../harness/verticals/retail/retail_host.py#L205) | self |  |
| [link_intake](../harness/verticals/retail/retail_host.py#L219) | self |  |
| [capabilities](../harness/verticals/retail/retail_host.py#L231) | self, collection, principal, chat_id, read_only, child, actor, custom |  |
| [install_workspace](../harness/verticals/retail/retail_host.py#L257) | host, selected |  |
| [monitoring_source](../harness/verticals/retail/retail_host.py#L299) | owner, key |  |
| [display_owner_agent](../harness/verticals/retail/retail_host.py#L318) | owner, collection, create |  |
| [collections](../harness/verticals/retail/retail_host.py#L338) | principal |  |
| [run_lane](../harness/verticals/retail/retail_host.py#L358) | run, depth | The lane of one run: the observation that woke it and the observations it was handed. |
| [observation_lane](../harness/verticals/retail/retail_host.py#L369) | event, depth | 'live', 'replay' or 'unknown' for one committed observation, decided once and kept. |
| [decide](../harness/verticals/retail/retail_host.py#L377) |  |  |
| [chat_run_lane](../harness/verticals/retail/retail_host.py#L392) | chat_id | The lane of the host run active in this conversation; a person's own turn is live. |
| [covers](../harness/verticals/retail/retail_host.py#L402) | definition, event | This saved definition tracks the observation: its business and its profiles. |
| [tracker_alert](../harness/verticals/retail/retail_host.py#L407) | definition, event | Host alert delivery: the committed event is this Tracking Agent's processed alert, revision 1. |
| [emit_monitoring_event](../harness/verticals/retail/retail_host.py#L416) | event |  |
| [phone_catch_up](../harness/verticals/retail/retail_host.py#L436) |  | Read again each covering observation of the last 900 seconds that holds no fan-out receipt. |
| [lifespan](../harness/verticals/retail/retail_host.py#L474) | app, host |  |
| [tick](../harness/verticals/retail/retail_host.py#L477) |  |  |
| [register_routes](../harness/verticals/retail/retail_host.py#L492) | app, host, http |  |
| [public_request](../harness/verticals/retail/retail_host.py#L503) | request |  |
| [request_body_limit](../harness/verticals/retail/retail_host.py#L508) | request |  |
| [query_request](../harness/verticals/retail/retail_host.py#L516) | request |  |
| [scope_change](../harness/verticals/retail/retail_host.py#L521) | request |  |
| [local_services](../harness/verticals/retail/retail_host.py#L534) | *args, **kwargs |  |
| [read_workspace](../harness/verticals/retail/retail_host.py#L539) | host, selected | Install bounded retail reads without scheduler, messaging or runtime recovery. |

### harness/verticals/retail/retail_http.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [web_asset](../harness/verticals/retail/retail_http.py#L11) | relative |  |
| [register_routes](../harness/verticals/retail/retail_http.py#L39) | app, host, http |  |
| [search](../harness/verticals/retail/retail_http.py#L69) | request |  |
| [review_cameras](../harness/verticals/retail/retail_http.py#L77) | body, request |  |
| [run_review](../harness/verticals/retail/retail_http.py#L108) |  |  |
| [source_frames_only](../harness/verticals/retail/retail_http.py#L110) | maximum |  |
| [prepare_export](../harness/verticals/retail/retail_http.py#L126) | body, request |  |
| [export_scope_allowed](../harness/verticals/retail/retail_http.py#L147) | request, payload_id, principal |  |
| [require_export_scope](../harness/verticals/retail/retail_http.py#L160) | request, payload_id, principal |  |
| [list_exports](../harness/verticals/retail/retail_http.py#L167) | request, dataset |  |
| [inspection_preview](../harness/verticals/retail/retail_http.py#L176) | receipt_id, index, request |  |
| [unavailable](../harness/verticals/retail/retail_http.py#L183) |  |  |
| [get_export](../harness/verticals/retail/retail_http.py#L212) | payload_id, request |  |
| [download_export](../harness/verticals/retail/retail_http.py#L223) | payload_id, request |  |
| [cameras](../harness/verticals/retail/retail_http.py#L236) | request, collection |  |
| [camera_details](../harness/verticals/retail/retail_http.py#L244) | camera_id, request, collection |  |
| [camera_context_draft](../harness/verticals/retail/retail_http.py#L252) | camera_id, body, request, collection |  |
| [confirm_camera_context](../harness/verticals/retail/retail_http.py#L263) | camera_id, body, request, collection |  |
| [source_library](../harness/verticals/retail/retail_http.py#L274) | request, collection, folder |  |
| [source_asset](../harness/verticals/retail/retail_http.py#L284) | asset_id, request, collection |  |
| [visible_clip](../harness/verticals/retail/retail_http.py#L293) | request, clip_id |  |
| [evidence_clip](../harness/verticals/retail/retail_http.py#L309) | clip_id, request |  |
| [thumbnail](../harness/verticals/retail/retail_http.py#L324) | clip_id, request |  |
| [download_clip](../harness/verticals/retail/retail_http.py#L340) | clip_id, request |  |
| [clip_manifest](../harness/verticals/retail/retail_http.py#L358) | record, resolved, source_cut_available |  |
| [clip_focus](../harness/verticals/retail/retail_http.py#L387) | state, clip_id, focus_id |  |
| [download_manifest](../harness/verticals/retail/retail_http.py#L399) | clip_id, request, focus_id |  |
| [clip_details](../harness/verticals/retail/retail_http.py#L422) | clip_id, request, focus_id |  |
| [file_authorization](../harness/verticals/retail/retail_http.py#L458) | request, file_id, principal |  |
| [original_source](../harness/verticals/retail/retail_http.py#L464) | asset_id, request, collection |  |
| [sij_acroni_logo](../harness/verticals/retail/retail_http.py#L477) |  |  |
| [control_room_script](../harness/verticals/retail/retail_http.py#L482) |  |  |
| [camera_provider_asset](../harness/verticals/retail/retail_http.py#L487) | filename |  |
| [retail_scope_component](../harness/verticals/retail/retail_http.py#L498) | request |  |
| [retail_component](../harness/verticals/retail/retail_http.py#L509) | request |  |

### harness/verticals/retail/retail_mcp_services.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [local_services](../harness/verticals/retail/retail_mcp_services.py#L8) | state, principal_id, dataset, derivatives_enabled, index_factory |  |
| [local_result](../harness/verticals/retail/retail_mcp_services.py#L46) | name, value |  |
| [local_authority](../harness/verticals/retail/retail_mcp_services.py#L49) | self, actor, collection |  |
| [collection_names](../harness/verticals/retail/retail_mcp_services.py#L53) | self, principal |  |
| [local_read_names](../harness/verticals/retail/retail_mcp_services.py#L56) | self |  |
| [read_admission](../harness/verticals/retail/retail_mcp_services.py#L59) | self, actor, collection |  |
| [bind](../harness/verticals/retail/retail_mcp_services.py#L77) |  |  |

### harness/verticals/retail/retail_records.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__post_init__](../harness/verticals/retail/retail_records.py#L60) | self |  |
| [display_owner_agent](../harness/verticals/retail/retail_records.py#L64) | self, create | Actual agent identity supplied by the host; legacy data keeps its principal owner. |
| [id](../harness/verticals/retail/retail_records.py#L73) | self |  |
| [actor](../harness/verticals/retail/retail_records.py#L77) | self |  |
| [open_company](../harness/verticals/retail/retail_records.py#L81) | state, owner, collection, member | Open a company's stores. `member(principal)` is the host's membership lookup. |
| [company_from_access](../harness/verticals/retail/retail_records.py#L93) | state, access_state, environment_id, owner, collection | Open a company through its access registry, as the host commands do. |
| [member](../harness/verticals/retail/retail_records.py#L98) | principal |  |
| [digest](../harness/verticals/retail/retail_records.py#L106) | value, length |  |
| [rows](../harness/verticals/retail/retail_records.py#L110) | company, kind, location_id |  |
| [stamp](../harness/verticals/retail/retail_records.py#L116) | company, location_id, value, camera_id |  |
| [put_many](../harness/verticals/retail/retail_records.py#L121) | company, kind, location_id, values, replace_all, keep | One transaction per kind. `replace_all` rebuilds a derived kind for the location. |
| [cameras](../harness/verticals/retail/retail_records.py#L137) | company, location_id |  |
| [ensure_camera](../harness/verticals/retail/retail_records.py#L142) | company, location_id, room_id, name, source_ids | Create the named camera in the location, or add recordings to it. One scope write. |
| [register_zone](../harness/verticals/retail/retail_records.py#L156) | company, location_id, camera_id, key, kind, label, data_basis |  |
| [source_clocks](../harness/verticals/retail/retail_records.py#L165) | company | Capture start (epoch seconds) of each registered recording that has one. |
| [iso](../harness/verticals/retail/retail_records.py#L176) | epoch |  |
| [record_till_sales](../harness/verticals/retail/retail_records.py#L180) | company, location_id, transactions | Write till transactions into the same sale tables with `basis: "pos"`. |
| [catalog](../harness/verticals/retail/retail_records.py#L205) | company, location_id | Catalog products of the location: the ones a catalog source or the finder supplied. |
| [derive](../harness/verticals/retail/retail_records.py#L212) | company, location_id | Accumulate committed events into items, baskets, estimated sales, shelves and queues. |
| [line](../harness/verticals/retail/retail_records.py#L301) | entry |  |

### harness/verticals/retail/retail_scope.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [install_scope](../harness/verticals/retail/retail_scope.py#L26) | selected, messaging_member, members | Callbacks: member(selected, principal), members(selected), both current. |
| [source_authorized](../harness/verticals/retail/retail_scope.py#L31) | actor, collection, source |  |
| [_owned_views](../harness/verticals/retail/retail_scope.py#L53) | selected, principal, collection |  |
| [filter_view](../harness/verticals/retail/retail_scope.py#L68) | selected, view, principal, collection, chat_id, observer | Return an immutable narrowed index with a synchronous current() fence. |
| [public_revisions](../harness/verticals/retail/retail_scope.py#L85) |  |  |
| [public_current](../harness/verticals/retail/retail_scope.py#L91) |  |  |
| [shared_collections](../harness/verticals/retail/retail_scope.py#L108) |  |  |
| [current](../harness/verticals/retail/retail_scope.py#L144) |  |  |
| [scope_current](../harness/verticals/retail/retail_scope.py#L175) | view | Explicitly fail closed for unbound/invalid views at host dispatch seams. |
| [history_allowed](../harness/verticals/retail/retail_scope.py#L183) | selected, record, principal | Whole-chat admission: historical context never widens current membership. |
| [turn_actor](../harness/verticals/retail/retail_scope.py#L217) | agent, chat_id, sender |  |
| [agent_scope](../harness/verticals/retail/retail_scope.py#L228) | agent, chat_id, dataset, sender, admit | Fresh tool authority, cumulative history admission and native isolation. |
| [read](../harness/verticals/retail/retail_scope.py#L239) | function, *args, **kwargs |  |
| [active_scope_current](../harness/verticals/retail/retail_scope.py#L315) | agent, chat_id |  |
| [history_within_view](../harness/verticals/retail/retail_scope.py#L327) | selected, record, view | Old derived files/context require the whole admitted historical scope. |
| [__init__](../harness/verticals/retail/retail_scope.py#L348) | self, selected |  |
| [history_allowed](../harness/verticals/retail/retail_scope.py#L351) | self, record, principal |  |
| [filter_view](../harness/verticals/retail/retail_scope.py#L354) | self, view, principal, collection, chat_id, observer |  |
| [owned_views](../harness/verticals/retail/retail_scope.py#L357) | self, principal, collection |  |
| [history_within_view](../harness/verticals/retail/retail_scope.py#L360) | self, record, view |  |
| [source_options](../harness/verticals/retail/retail_scope.py#L363) | self, principal, collection |  |
| [agent_scope](../harness/verticals/retail/retail_scope.py#L375) | self, agent, chat_id, dataset, sender, admit |  |
| [request_scope](../harness/verticals/retail/retail_scope.py#L379) | self, request |  |
| [bind](../harness/verticals/retail/retail_scope.py#L390) | self, view |  |
| [bound](../harness/verticals/retail/retail_scope.py#L394) |  |  |

### harness/verticals/retail/retail_scope_routes.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [call](../harness/verticals/retail/retail_scope_routes.py#L20) | callback, *args, **kwargs |  |
| [body](../harness/verticals/retail/retail_scope_routes.py#L24) | request, fields |  |
| [pairs](../harness/verticals/retail/retail_scope_routes.py#L37) | items |  |
| [result](../harness/verticals/retail/retail_scope_routes.py#L49) | function, *args, **kwargs |  |
| [register_scope_routes](../harness/verticals/retail/retail_scope_routes.py#L58) | app, store_for_workspace, actor_for_request, collection_for_request, chat_for_request, describe_for_request |  |
| [selected](../harness/verticals/retail/retail_scope_routes.py#L61) | request, collection, write |  |
| [graph](../harness/verticals/retail/retail_scope_routes.py#L70) | request, collection |  |
| [graph_events](../harness/verticals/retail/retail_scope_routes.py#L77) | request, collection, after, limit |  |
| [change](../harness/verticals/retail/retail_scope_routes.py#L82) | kind, request |  |
| [chat_scope](../harness/verticals/retail/retail_scope_routes.py#L90) | chat_id, request |  |
| [change_chat_scope](../harness/verticals/retail/retail_scope_routes.py#L96) | chat_id, request |  |
| [register_host_routes](../harness/verticals/retail/retail_scope_routes.py#L103) | app | Register private graph/selector APIs using the host's current session ACL. |
| [actor](../harness/verticals/retail/retail_scope_routes.py#L105) | request, write |  |
| [collection](../harness/verticals/retail/retail_scope_routes.py#L118) | request, value |  |
| [chat](../harness/verticals/retail/retail_scope_routes.py#L127) | request, key, write |  |
| [describe](../harness/verticals/retail/retail_scope_routes.py#L141) | request, value |  |

### harness/verticals/retail/retail_scope_views.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [scoped_index_view](../harness/verticals/retail/retail_scope_views.py#L5) | index, effective | Narrow an ALREADY owner/Ready-filtered index; this never grants ownership. |
| [selected_index_view](../harness/verticals/retail/retail_scope_views.py#L21) | index, positions | Copy already-admitted row positions and rebuild the aligned public index. |

### harness/verticals/retail/retail_script_signals.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [digest](../harness/verticals/retail/retail_script_signals.py#L24) | value |  |
| [__init__](../harness/verticals/retail/retail_script_signals.py#L29) | self, store, company, sandbox, clock |  |
| [_snapshot](../harness/verticals/retail/retail_script_signals.py#L41) | self, record |  |
| [_save](../harness/verticals/retail/retail_script_signals.py#L49) | self, company, tracker, value |  |
| [save](../harness/verticals/retail/retail_script_signals.py#L55) | head, put |  |
| [_update](../harness/verticals/retail/retail_script_signals.py#L72) | self, record, **changes |  |
| [authorized](../harness/verticals/retail/retail_script_signals.py#L86) | self, record |  |
| [processor](../harness/verticals/retail/retail_script_signals.py#L122) | self, tracker, company, location_id, period, data |  |
| [execute](../harness/verticals/retail/retail_script_signals.py#L127) | self, company, tracker, document, source, context, perform, current |  |
| [run](../harness/verticals/retail/retail_script_signals.py#L186) | self, payload, config, context |  |
| [cancel](../harness/verticals/retail/retail_script_signals.py#L208) | self, context |  |
| [_cleanup](../harness/verticals/retail/retail_script_signals.py#L217) | self, context |  |
| [recover_pending](../harness/verticals/retail/retail_script_signals.py#L232) | self | Settle interrupted original jobs before another location pass is admitted. |
| [reconcile](../harness/verticals/retail/retail_script_signals.py#L246) | self, context |  |
| [__init__](../harness/verticals/retail/retail_script_signals.py#L256) | self, adapter, signal |  |
| [opened](../harness/verticals/retail/retail_script_signals.py#L263) | self, job |  |
| [closed](../harness/verticals/retail/retail_script_signals.py#L269) | self, job |  |
| [before_publish](../harness/verticals/retail/retail_script_signals.py#L272) | self |  |
| [delivery](../harness/verticals/retail/retail_script_signals.py#L281) | self, wanted, text |  |
| [install](../harness/verticals/retail/retail_script_signals.py#L286) | selected | Register against the actual host store so later delivery retains producer authority. |
| [company](../harness/verticals/retail/retail_script_signals.py#L290) | owner, collection |  |
| [processor](../harness/verticals/retail/retail_script_signals.py#L297) | app_state, sandbox |  |
| [run](../harness/verticals/retail/retail_script_signals.py#L298) | tracker, company, location_id, period, data |  |

### harness/verticals/retail/retail_settings.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [value](../harness/verticals/retail/retail_settings.py#L30) | name, default, environ |  |
| [remove](../harness/verticals/retail/retail_settings.py#L36) | name, environ |  |

### harness/verticals/retail/retail_stream_import.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [load](../harness/verticals/retail/retail_stream_import.py#L28) | path |  |
| [timestamp](../harness/verticals/retail/retail_stream_import.py#L32) | value |  |
| [final_events](../harness/verticals/retail/retail_stream_import.py#L39) | text |  |
| [event_key](../harness/verticals/retail/retail_stream_import.py#L52) | source_id, output_index, event_index, raw |  |
| [audit_event](../harness/verticals/retail/retail_stream_import.py#L56) | raw, source_id, output_index, event_index, start_s, end_s, observed_start_s, observed_end_s, tracks, profile_id, profile_revision, review, vocabulary |  |
| [build_import](../harness/verticals/retail/retail_stream_import.py#L123) | run_root, profile_id, profile_revision, reviews, vocabulary |  |
| [main](../harness/verticals/retail/retail_stream_import.py#L187) |  |  |

### harness/verticals/retail/retail_tool_context.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [state](../harness/verticals/retail/retail_tool_context.py#L14) | self |  |
| [allowed](../harness/verticals/retail/retail_tool_context.py#L16) | self, location_id, camera_ids | Whether the reader's present access covers a location and, with `camera_ids`, those cameras of it. A tracker's definition belongs to its location; its output is the record of the cameras it read, so an output is read with its own cameras. |
| [manages](../harness/verticals/retail/retail_tool_context.py#L37) | self, location_id | Whether the reader manages a location in the scope this read arrived with. |
| [source](../harness/verticals/retail/retail_tool_context.py#L43) | self, source_id | Whether the reader's present access covers a recording. |
| [require](../harness/verticals/retail/retail_tool_context.py#L48) | self, location_id |  |
| [organization](../harness/verticals/retail/retail_tool_context.py#L61) | self | Whether this is the company's Organization conversation. |
| [company](../harness/verticals/retail/retail_tool_context.py#L66) | self | The acting member's handle on the company's stores, under the host's current scope. |

### harness/verticals/retail/retail_tools.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [bridge_specs](../harness/verticals/retail/retail_tools.py#L16) | write |  |
| [result_fields](../harness/verticals/retail/retail_tools.py#L74) | name, content, success |  |
| [bridge_call](../harness/verticals/retail/retail_tools.py#L79) | context, name, args |  |
| [preview_current](../harness/verticals/retail/retail_tools.py#L270) |  |  |
| [plans](../harness/verticals/retail/retail_tools.py#L349) | self |  |
| [public_clip](../harness/verticals/retail/retail_tools.py#L356) | record |  |
| [inspection_metadata](../harness/verticals/retail/retail_tools.py#L362) | self, record, frames, include_observations |  |
| [clip_attachments](../harness/verticals/retail/retail_tools.py#L380) | self, ids, dataset |  |
| [context](../harness/verticals/retail/retail_tools.py#L392) | admitted |  |
| [catalog_call](../harness/verticals/retail/retail_tools.py#L411) | context, name, arguments |  |
| [connector_details](../harness/verticals/retail/retail_tools.py#L438) | agent, saved, connector_id, owner, collection |  |
| [external_read](../harness/verticals/retail/retail_tools.py#L446) | context, name, arguments |  |
| [local_call](../harness/verticals/retail/retail_tools.py#L466) | context, name, arguments |  |

### harness/verticals/retail/retail_urls.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [legacy_path](../harness/verticals/retail/retail_urls.py#L164) | path, method | Classify current paths through their established admission policy. |
| [__init__](../harness/verticals/retail/retail_urls.py#L178) | self, app |  |
| [__getattr__](../harness/verticals/retail/retail_urls.py#L181) | self, name |  |
| [register](../harness/verticals/retail/retail_urls.py#L184) | path, **options |  |
| [decorate](../harness/verticals/retail/retail_urls.py#L188) | endpoint |  |
| [retail_router](../harness/verticals/retail/retail_urls.py#L198) | app |  |

### harness/verticals/retail/retail_usage.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [read](../harness/verticals/retail/retail_usage.py#L11) | self, approval_path |  |
| [validate](../harness/verticals/retail/retail_usage.py#L22) | self, path |  |

### harness/verticals/retail/retired_tools.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [require_active_tool](../harness/verticals/retail/retired_tools.py#L13) | name |  |
| [active_specs](../harness/verticals/retail/retired_tools.py#L18) | specs |  |
| [is_retired_archive_agent](../harness/verticals/retail/retired_tools.py#L25) | definition | Saved camera_footage scheduler definitions use the retired archive workflow. |

### harness/verticals/retail/retrieval.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_slug](../harness/verticals/retail/retrieval.py#L30) | value |  |
| [load_sources](../harness/verticals/retail/retrieval.py#L34) | sources, manifests | Read local paths only. Descriptions in manifests never become embeddings. |
| [__init__](../harness/verticals/retail/retrieval.py#L67) | self, state |  |
| [_reload](../harness/verticals/retail/retrieval.py#L77) | self |  |
| [_load_model](../harness/verticals/retail/retrieval.py#L92) | self |  |
| [_encode_images](../harness/verticals/retail/retrieval.py#L118) | self, images |  |
| [_encode_text](../harness/verticals/retail/retrieval.py#L127) | self, query |  |
| [build](../harness/verticals/retail/retrieval.py#L136) | self, sources, interval |  |
| [search](../harness/verticals/retail/retrieval.py#L235) | self, query, limit, dataset |  |
| [get_clip](../harness/verticals/retail/retrieval.py#L258) | self, clip_id | Private server lookup; includes filesystem paths, never a public API body. |
| [get_video](../harness/verticals/retail/retrieval.py#L262) | self, video_id | Private server lookup for controlled media serving. |
| [inspect_clip](../harness/verticals/retail/retrieval.py#L266) | self, clip_id | Decode up to three frames for the agent to inspect; makes no verdict. |
| [status](../harness/verticals/retail/retrieval.py#L307) | self |  |
| [main](../harness/verticals/retail/retrieval.py#L313) |  |  |

### harness/verticals/retail/run_stock_commissioning.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [probe_clock](../harness/verticals/retail/run_stock_commissioning.py#L32) | path | CPU-only decoder preflight before importing vLLM or creating a model. |
| [capture](../harness/verticals/retail/run_stock_commissioning.py#L66) | pad, info, target |  |
| [main](../harness/verticals/retail/run_stock_commissioning.py#L105) |  |  |
| [result](../harness/verticals/retail/run_stock_commissioning.py#L248) | element, sid, start, end, text |  |
| [message](../harness/verticals/retail/run_stock_commissioning.py#L264) | bus, msg |  |
| [tick](../harness/verticals/retail/run_stock_commissioning.py#L276) |  |  |

### harness/verticals/retail/seal_playback_media.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/verticals/retail/seal_playback_media.py#L94) | self, code, message |  |
| [unique_views](../harness/verticals/retail/seal_playback_media.py#L117) | self |  |
| [_sha](../harness/verticals/retail/seal_playback_media.py#L124) | content |  |
| [_open_evidence](../harness/verticals/retail/seal_playback_media.py#L130) | path |  |
| [_chunks](../harness/verticals/retail/seal_playback_media.py#L141) | source |  |
| [_measure](../harness/verticals/retail/seal_playback_media.py#L150) | path, maximum, code | SHA-256 and length of one file, read once within the bound of its kind. |
| [_content](../harness/verticals/retail/seal_playback_media.py#L163) | path, maximum, code |  |
| [_resolve](../harness/verticals/retail/seal_playback_media.py#L172) | root, value |  |
| [load_selection](../harness/verticals/retail/seal_playback_media.py#L181) | path |  |
| [selection_from_import](../harness/verticals/retail/seal_playback_media.py#L189) | path, face_redaction | Every view of one completed historical import, in the importer's own identifiers. |
| [_boxes](../harness/verticals/retail/seal_playback_media.py#L217) | data, start, end |  |
| [_one](../harness/verticals/retail/seal_playback_media.py#L232) | data, bounds, kind |  |
| [_movie_header](../harness/verticals/retail/seal_playback_media.py#L239) | path |  |
| [probe_recording](../harness/verticals/retail/seal_playback_media.py#L262) | path | Width, height, frame count and constant frame rate of the one video track of an MP4. |
| [sidecar_digest](../harness/verticals/retail/seal_playback_media.py#L298) | items | One digest for a per-frame KITTI directory: the sorted listing of each file's hash and name. |
| [read_tracker_sidecar](../harness/verticals/retail/seal_playback_media.py#L309) | directory, frame_count | Every reported box of every frame, and each raw tracker ID's first reported frame. |
| [geometry_document](../harness/verticals/retail/seal_playback_media.py#L353) | recording, source_sha256, tracker_namespace, frames, births | What the player paints from: one entry per frame, each box with its ID and birth identity. |
| [_context](../harness/verticals/retail/seal_playback_media.py#L375) | company_id, principal_id |  |
| [_lineage](../harness/verticals/retail/seal_playback_media.py#L387) | selection | The current binding of every selected recording, and each tracker epoch's visitors. |
| [reported_births](../harness/verticals/retail/seal_playback_media.py#L411) | view, binding, recording, first, sidecar_sha256, visitors | Each raw tracker ID's reported birth identity, proven equal to the one PostgreSQL holds. |
| [_service_identity](../harness/verticals/retail/seal_playback_media.py#L434) | state | The service identity owns the private state and runs this command; the reader requires both. |
| [_private_directory](../harness/verticals/retail/seal_playback_media.py#L445) | path | True for a private real directory of this identity, False for an absent one. |
| [_sealed](../harness/verticals/retail/seal_playback_media.py#L456) | path, sha256, size | True for an intact sealed file, False for an absent one; any other state is refused. |
| [plan](../harness/verticals/retail/seal_playback_media.py#L469) | options | Verify the whole selection and describe the sealed catalog. This writes nothing. |
| [place](../harness/verticals/retail/seal_playback_media.py#L492) | kind, sha256, size, source |  |
| [_write](../harness/verticals/retail/seal_playback_media.py#L614) | target, sha256, size, source, replace | One sealed regular file of its own bytes: written beside its name, checked, then named. |
| [_sync](../harness/verticals/retail/seal_playback_media.py#L638) | path |  |
| [seal](../harness/verticals/retail/seal_playback_media.py#L646) | planned, prune | Copy, check through the reader's own code, then replace the catalog in one rename. |
| [_reserve](../harness/verticals/retail/seal_playback_media.py#L699) | path |  |
| [run](../harness/verticals/retail/seal_playback_media.py#L706) | options | The dry run or the real seal over an open restricted pool; returns the receipt. |
| [run_with_database](../harness/verticals/retail/seal_playback_media.py#L743) | options, dsn | Open the one restricted pool this command reads through, seal, and close the pool. |
| [parser](../harness/verticals/retail/seal_playback_media.py#L761) |  |  |
| [main](../harness/verticals/retail/seal_playback_media.py#L782) | argv, environ |  |

### harness/verticals/retail/seed_control_room.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [seed_location](../harness/verticals/retail/seed_control_room.py#L18) | state, access_path, environment_id, owner, lifecycle, collection, name, address, cover_image, coordinates |  |
| [member](../harness/verticals/retail/seed_control_room.py#L28) | key |  |

### harness/verticals/retail/seed_retail_demo.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [seed_day](../harness/verticals/retail/seed_retail_demo.py#L38) | company, requested | The day the preserved clips sit on: the one already registered, else the requested or latest full day. |
| [seed](../harness/verticals/retail/seed_retail_demo.py#L50) | state, access_state, environment_id, owner, lifecycle, archive, found_products, day, history_days, product_types_output, collection, name, address, coordinates, publish_media |  |
| [main](../harness/verticals/retail/seed_retail_demo.py#L99) | argv |  |

### harness/verticals/retail/sftp_intake.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [drain](../harness/verticals/retail/sftp_intake.py#L20) | task |  |
| [offload](../harness/verticals/retail/sftp_intake.py#L27) | fn, *args, **kwargs |  |
| [callback](../harness/verticals/retail/sftp_intake.py#L34) | fn, *args, **kwargs |  |
| [__init__](../harness/verticals/retail/sftp_intake.py#L39) | self, store |  |
| [db](../harness/verticals/retail/sftp_intake.py#L52) | self |  |
| [bind](../harness/verticals/retail/sftp_intake.py#L57) | self, config |  |
| [status](../harness/verticals/retail/sftp_intake.py#L70) | self, config |  |
| [scan](../harness/verticals/retail/sftp_intake.py#L75) | self, config, page, cursor, now |  |
| [rows](../harness/verticals/retail/sftp_intake.py#L93) | self, config |  |
| [cursor](../harness/verticals/retail/sftp_intake.py#L95) | self, config |  |
| [block](../harness/verticals/retail/sftp_intake.py#L97) | self, config, name |  |
| [missing](../harness/verticals/retail/sftp_intake.py#L99) | self, config, name |  |
| [reset](../harness/verticals/retail/sftp_intake.py#L101) | self, config, name, now |  |
| [upload](../harness/verticals/retail/sftp_intake.py#L103) | self, config, name, upload |  |
| [sealed](../harness/verticals/retail/sftp_intake.py#L105) | self, config, name, upload, now |  |
| [finish](../harness/verticals/retail/sftp_intake.py#L109) | self, config, now, error |  |
| [__init__](../harness/verticals/retail/sftp_intake.py#L119) | self, store, connector, clock, max_active, begin_upload |  |
| [_owned](../harness/verticals/retail/sftp_intake.py#L133) | self, config, actor |  |
| [status](../harness/verticals/retail/sftp_intake.py#L138) | self, config, actor |  |
| [pull](../harness/verticals/retail/sftp_intake.py#L141) | self, config, actor, credentials, current, cancelled, max_seconds |  |
| [alive](../harness/verticals/retail/sftp_intake.py#L148) |  |  |
| [watch](../harness/verticals/retail/sftp_intake.py#L153) |  |  |
| [_pull](../harness/verticals/retail/sftp_intake.py#L165) | self, config, actor, credentials, current, seconds |  |
| [_acquire](../harness/verticals/retail/sftp_intake.py#L227) | self, config, actor, row, item, reader, current |  |
| [stop](../harness/verticals/retail/sftp_intake.py#L253) | self, config, actor |  |
| [close](../harness/verticals/retail/sftp_intake.py#L261) | self |  |

### harness/verticals/retail/sftp_transport.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [require](../harness/verticals/retail/sftp_transport.py#L17) | value, code |  |
| [digest](../harness/verticals/retail/sftp_transport.py#L19) | value |  |
| [text](../harness/verticals/retail/sftp_transport.py#L20) | value, maximum |  |
| [validate_target](../harness/verticals/retail/sftp_transport.py#L22) | value |  |
| [__post_init__](../harness/verticals/retail/sftp_transport.py#L48) | self |  |
| [sha256](../harness/verticals/retail/sftp_transport.py#L56) | self |  |
| [target_sha256](../harness/verticals/retail/sftp_transport.py#L58) | self |  |
| [fingerprint](../harness/verticals/retail/sftp_transport.py#L60) | self |  |
| [__post_init__](../harness/verticals/retail/sftp_transport.py#L69) | self |  |
| [from_attrs](../harness/verticals/retail/sftp_transport.py#L84) | cls, name, attrs |  |
| [version](../harness/verticals/retail/sftp_transport.py#L91) | self |  |
| [public_socket](../harness/verticals/retail/sftp_transport.py#L98) | config, current |  |
| [__init__](../harness/verticals/retail/sftp_transport.py#L110) | self, config, client, current, private_values |  |
| [metadata](../harness/verticals/retail/sftp_transport.py#L113) | self, value |  |
| [check](../harness/verticals/retail/sftp_transport.py#L115) | self |  |
| [path](../harness/verticals/retail/sftp_transport.py#L116) | self, name |  |
| [list_page](../harness/verticals/retail/sftp_transport.py#L123) | self, cursor, limit |  |
| [open](../harness/verticals/retail/sftp_transport.py#L142) | self, expected |  |
| [read](../harness/verticals/retail/sftp_transport.py#L157) | self, handle, offset, length |  |
| [connect](../harness/verticals/retail/sftp_transport.py#L163) | config, credentials, current, socket_factory | socket_factory is host-only fixture injection, never a serialized setting. |

### harness/verticals/retail/shelf_catalog.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [valid_box](../harness/verticals/retail/shelf_catalog.py#L27) | self |  |
| [__init__](../harness/verticals/retail/shelf_catalog.py#L42) | self, state, setup, locations, provider, enabled, funding_ready, clock |  |
| [connect](../harness/verticals/retail/shelf_catalog.py#L50) | self |  |
| [_status](../harness/verticals/retail/shelf_catalog.py#L53) | self, owner, photo, status, detail |  |
| [process](../harness/verticals/retail/shelf_catalog.py#L57) | self, owner, photo_id |  |
| [drain](../harness/verticals/retail/shelf_catalog.py#L132) | self, limit |  |
| [image](../harness/verticals/retail/shelf_catalog.py#L145) | self, owner, key, index |  |

### harness/verticals/retail/source_derivatives.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_json](../harness/verticals/retail/source_derivatives.py#L48) | value, maximum |  |
| [_digest](../harness/verticals/retail/source_derivatives.py#L55) | value |  |
| [_require](../harness/verticals/retail/source_derivatives.py#L58) | value, code |  |
| [__init__](../harness/verticals/retail/source_derivatives.py#L63) | self, state, company_id, media_client, enabled |  |
| [_authorize](../harness/verticals/retail/source_derivatives.py#L71) | self, record, owner, purpose, frame_seconds |  |
| [_published](../harness/verticals/retail/source_derivatives.py#L87) | self, asset_id, owner |  |
| [_initialize](../harness/verticals/retail/source_derivatives.py#L107) | self |  |
| [_db](../harness/verticals/retail/source_derivatives.py#L125) | self, write |  |
| [_row](../harness/verticals/retail/source_derivatives.py#L146) | self, identity, key |  |
| [_admit](../harness/verticals/retail/source_derivatives.py#L155) | self, record, binding |  |
| [_update](../harness/verticals/retail/source_derivatives.py#L166) | self, identity, expected_generation, **fields |  |
| [_locked](../harness/verticals/retail/source_derivatives.py#L174) | self, identity |  |
| [_scope](../harness/verticals/retail/source_derivatives.py#L190) | self, row, binding |  |
| [_validate_files](../harness/verticals/retail/source_derivatives.py#L193) | self, manifest, files, binding, scope |  |
| [read_receipt](../harness/verticals/retail/source_derivatives.py#L210) | self, receipt_id, record, owner_principal_id, purpose |  |
| [_read_receipt](../harness/verticals/retail/source_derivatives.py#L216) | self, receipt_id, record, owner_principal_id, purpose |  |
| [_read](../harness/verticals/retail/source_derivatives.py#L221) | self, row, record, owner, purpose |  |
| [derive](../harness/verticals/retail/source_derivatives.py#L248) | self, record, purpose, owner_principal_id, frame_seconds |  |
| [_derive](../harness/verticals/retail/source_derivatives.py#L255) | self, record, purpose, owner_principal_id, frame_seconds |  |
| [_cleanup](../harness/verticals/retail/source_derivatives.py#L279) | self, row, binding, handle |  |
| [_reconcile](../harness/verticals/retail/source_derivatives.py#L289) | self, row, binding |  |
| [_receive](../harness/verticals/retail/source_derivatives.py#L300) | self, row, binding, handle, result |  |
| [_run](../harness/verticals/retail/source_derivatives.py#L333) | self, row, record, binding, resolved |  |

### harness/verticals/retail/source_embedding.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [require](../harness/verticals/retail/source_embedding.py#L45) | ok, code |  |
| [encode](../harness/verticals/retail/source_embedding.py#L49) | value |  |
| [checksum](../harness/verticals/retail/source_embedding.py#L53) | data |  |
| [private_directory](../harness/verticals/retail/source_embedding.py#L57) | path |  |
| [fsync_directory](../harness/verticals/retail/source_embedding.py#L67) | path |  |
| [atomic_json](../harness/verticals/retail/source_embedding.py#L73) | path, value |  |
| [read_private](../harness/verticals/retail/source_embedding.py#L84) | path, maximum |  |
| [read_json](../harness/verticals/retail/source_embedding.py#L95) | path |  |
| [locked](../harness/verticals/retail/source_embedding.py#L100) | path |  |
| [utc](../harness/verticals/retail/source_embedding.py#L109) |  |  |
| [runtime](../harness/verticals/retail/source_embedding.py#L113) | python, config |  |
| [implementation_identity](../harness/verticals/retail/source_embedding.py#L130) |  |  |
| [batch_identity](../harness/verticals/retail/source_embedding.py#L136) | context, batch, company, idempotency_key, profile |  |
| [public](../harness/verticals/retail/source_embedding.py#L169) | record |  |
| [drain](../harness/verticals/retail/source_embedding.py#L173) | task |  |
| [owned_thread](../harness/verticals/retail/source_embedding.py#L181) | function, *args |  |
| [__init__](../harness/verticals/retail/source_embedding.py#L191) | self, state, company_id, approval_path, modal_python, modal_config, profile, runner |  |
| [admit](../harness/verticals/retail/source_embedding.py#L197) | self, context, batch, idempotency_key |  |
| [_admit](../harness/verticals/retail/source_embedding.py#L200) | self, context, batch, idempotency_key |  |
| [_directory](../harness/verticals/retail/source_embedding.py#L229) | self, admission |  |
| [_stage](../harness/verticals/retail/source_embedding.py#L237) | self, directory, record, inputs |  |
| [run](../harness/verticals/retail/source_embedding.py#L249) | self, admission, inputs, cancelled |  |
| [stop](../harness/verticals/retail/source_embedding.py#L280) | self, admission | Host-only crash reconciliation; leaves the full budget hold intact. |
| [receipt](../harness/verticals/retail/source_embedding.py#L286) | self, admission | Host-only audit; approval paths/identities are never an HTTP response. |
| [validate_result](../harness/verticals/retail/source_embedding.py#L293) | result, record |  |
| [__init__](../harness/verticals/retail/source_embedding.py#L309) | self, python, config |  |
| [_stop](../harness/verticals/retail/source_embedding.py#L312) | self, directory, interpreter, environment |  |
| [stop_attempt](../harness/verticals/retail/source_embedding.py#L324) | self, directory, record |  |
| [run](../harness/verticals/retail/source_embedding.py#L333) | self, directory, record, cancelled |  |
| [cleanup](../harness/verticals/retail/source_embedding.py#L352) |  |  |
| [verify_workspace](../harness/verticals/retail/source_embedding.py#L372) | modal |  |
| [app_name](../harness/verticals/retail/source_embedding.py#L378) | record |  |
| [provider_update](../harness/verticals/retail/source_embedding.py#L382) | directory, record, **values |  |
| [stop_own_app](../harness/verticals/retail/source_embedding.py#L396) | modal, directory, record, timeout_seconds | Verify this exact attempt's app and wait for provider-confirmed absence. |
| [stop](../harness/verticals/retail/source_embedding.py#L407) |  |  |
| [verified_info](../harness/verticals/retail/source_embedding.py#L409) |  |  |
| [child_record](../harness/verticals/retail/source_embedding.py#L437) | directory |  |
| [child_run](../harness/verticals/retail/source_embedding.py#L447) | directory, modal_module, worker_factory, stop_function |  |
| [watch_app](../harness/verticals/retail/source_embedding.py#L473) |  |  |
| [child_stop](../harness/verticals/retail/source_embedding.py#L512) | directory |  |
| [main](../harness/verticals/retail/source_embedding.py#L519) |  |  |
| [interrupted](../harness/verticals/retail/source_embedding.py#L525) | signum, frame |  |

### harness/verticals/retail/source_intake.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_text](../harness/verticals/retail/source_intake.py#L30) | value, maximum |  |
| [_sha](../harness/verticals/retail/source_intake.py#L36) | value |  |
| [_integer](../harness/verticals/retail/source_intake.py#L42) | value, lower, upper |  |
| [__post_init__](../harness/verticals/retail/source_intake.py#L53) | self |  |
| [require_write](../harness/verticals/retail/source_intake.py#L58) | self |  |
| [__post_init__](../harness/verticals/retail/source_intake.py#L74) | self |  |
| [__post_init__](../harness/verticals/retail/source_intake.py#L91) | self |  |
| [__init__](../harness/verticals/retail/source_intake.py#L106) | self, company_state, limits, clock |  |
| [_directory](../harness/verticals/retail/source_intake.py#L162) | path |  |
| [_open](../harness/verticals/retail/source_intake.py#L172) | path, flags, mode |  |
| [_connect](../harness/verticals/retail/source_intake.py#L183) | self |  |
| [_write](../harness/verticals/retail/source_intake.py#L201) | self, current |  |
| [_read](../harness/verticals/retail/source_intake.py#L226) | self |  |
| [_writer](../harness/verticals/retail/source_intake.py#L236) | actor |  |
| [_owned](../harness/verticals/retail/source_intake.py#L242) | db, table, identity, actor |  |
| [_sync_directory](../harness/verticals/retail/source_intake.py#L251) | path |  |
| [_public_upload](../harness/verticals/retail/source_intake.py#L259) | row |  |
| [_public_job](../harness/verticals/retail/source_intake.py#L264) | row |  |
| [create_source](../harness/verticals/retail/source_intake.py#L267) | self, actor, collection, name, kind |  |
| [lookup_connection_source](../harness/verticals/retail/source_intake.py#L279) | self, actor, collection, connection_id, target_sha256 |  |
| [ensure_connection_source](../harness/verticals/retail/source_intake.py#L287) | self, actor, collection, connection_id, target_sha256, name, kind, current | Host connection identity maps retries to one owner-scoped source. |
| [get_source](../harness/verticals/retail/source_intake.py#L305) | self, actor, source_id |  |
| [ensure_upload_source](../harness/verticals/retail/source_intake.py#L312) | self, actor, collection | Host-validated collection; one durable default per uploader/collection. |
| [list_sources](../harness/verticals/retail/source_intake.py#L333) | self, actor, collection |  |
| [_import_view](../harness/verticals/retail/source_intake.py#L346) | cls, db, row |  |
| [get_import](../harness/verticals/retail/source_intake.py#L356) | self, actor, upload_id |  |
| [list_imports](../harness/verticals/retail/source_intake.py#L361) | self, actor, collection, limit, offset |  |
| [cancel_import](../harness/verticals/retail/source_intake.py#L373) | self, actor, upload_id | Fence acquisition and every unfinished stage in one transaction. |
| [_quota](../harness/verticals/retail/source_intake.py#L410) | self, db |  |
| [begin_upload](../harness/verticals/retail/source_intake.py#L415) | self, actor, source_id, filename, size, idempotency_key, object_key, source_version, current |  |
| [get_upload](../harness/verticals/retail/source_intake.py#L458) | self, actor, upload_id |  |
| [_upload_file](../harness/verticals/retail/source_intake.py#L462) | self, row |  |
| [append_chunk](../harness/verticals/retail/source_intake.py#L473) | self, actor, upload_id, offset, data, sha256, current |  |
| [append_stream](../harness/verticals/retail/source_intake.py#L478) | self, actor, upload_id, offset, size, stream, sha256, current | Read one bounded chunk, with at most 64 KiB in the copy buffer. |
| [seal_upload](../harness/verticals/retail/source_intake.py#L537) | self, actor, upload_id, expected_sha256, current |  |
| [_verify_blob](../harness/verticals/retail/source_intake.py#L564) | self, path, size, checksum |  |
| [_finish_seal](../harness/verticals/retail/source_intake.py#L569) | self, db, row |  |
| [cancel_upload](../harness/verticals/retail/source_intake.py#L596) | self, actor, upload_id |  |
| [get_asset](../harness/verticals/retail/source_intake.py#L610) | self, actor, asset_id |  |
| [list_uploads](../harness/verticals/retail/source_intake.py#L617) | self, actor, source_id |  |
| [_queue_job](../harness/verticals/retail/source_intake.py#L622) | self, db, asset_id, stage |  |
| [_result](../harness/verticals/retail/source_intake.py#L628) | value |  |
| [_event](../harness/verticals/retail/source_intake.py#L639) | self, db, row, kind, body |  |
| [_expire_jobs](../harness/verticals/retail/source_intake.py#L643) | self, db |  |
| [claim_job](../harness/verticals/retail/source_intake.py#L650) | self, worker_id, lease_seconds, stages, asset_id | Host worker only. Expired attempts require explicit reconciliation. |
| [_leased](../harness/verticals/retail/source_intake.py#L671) | self, db, lease |  |
| [heartbeat_job](../harness/verticals/retail/source_intake.py#L682) | self, lease, lease_seconds |  |
| [job_context](../harness/verticals/retail/source_intake.py#L690) | self, lease | Private worker input, including durable evidence from earlier stages. |
| [checkpoint_job](../harness/verticals/retail/source_intake.py#L707) | self, lease, checkpoint | Private host attempt identity before work; never a completion receipt. |
| [open_job_original](../harness/verticals/retail/source_intake.py#L715) | self, lease | Host worker gets a verified read-only descriptor, never a public host path. |
| [finish_job](../harness/verticals/retail/source_intake.py#L728) | self, lease, result | Result is trusted worker evidence, not model/browser-supplied metadata. |
| [_finish_job_locked](../harness/verticals/retail/source_intake.py#L738) | self, db, row, result |  |
| [finish_publication](../harness/verticals/retail/source_intake.py#L751) | self, lease, publish | Fence bounded local publication and its Ready receipt together. |
| [fail_job](../harness/verticals/retail/source_intake.py#L772) | self, lease, error_code, uncertain |  |
| [cancel_job](../harness/verticals/retail/source_intake.py#L783) | self, actor, job_id |  |
| [reconcile_job](../harness/verticals/retail/source_intake.py#L802) | self, job_id, expected_generation, outcome, evidence_reference | Trusted worker/operator settles uncertain work after actual stop/billing checks. |
| [recover](../harness/verticals/retail/source_intake.py#L823) | self | Reconcile local transfer crashes; uncertain running jobs remain fenced. |

### harness/verticals/retail/source_routes.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__post_init__](../harness/verticals/retail/source_routes.py#L42) | self |  |
| [_deny](../harness/verticals/retail/source_routes.py#L75) | status, code |  |
| [_header](../harness/verticals/retail/source_routes.py#L79) | request, name, required |  |
| [_number_header](../harness/verticals/retail/source_routes.py#L89) | request, name, maximum, required |  |
| [_encoding](../harness/verticals/retail/source_routes.py#L98) | request |  |
| [_offload](../harness/verticals/retail/source_routes.py#L105) | function, *args, **kwargs | Keep private streams open until their finite disk transaction finishes. |
| [_call](../harness/verticals/retail/source_routes.py#L119) | function, *args, **kwargs |  |
| [_duplicates](../harness/verticals/retail/source_routes.py#L137) | pairs |  |
| [_json_body](../harness/verticals/retail/source_routes.py#L145) | request, model, policy, empty |  |
| [register_source_routes](../harness/verticals/retail/source_routes.py#L168) | app, store_for_workspace, policy_for_workspace, admission_for_workspace, projection_for_workspace | Register once after the host's authenticated workspace middleware. |
| [context](../harness/verticals/retail/source_routes.py#L185) | request, write, continuation, projected |  |
| [collection](../harness/verticals/retail/source_routes.py#L215) | value, allowed |  |
| [view_for](../harness/verticals/retail/source_routes.py#L218) | store, actor, identity, allowed |  |
| [response](../harness/verticals/retail/source_routes.py#L224) | view, store, status_code |  |
| [imports](../harness/verticals/retail/source_routes.py#L231) | request |  |
| [begin](../harness/verticals/retail/source_routes.py#L259) | request |  |
| [detail](../harness/verticals/retail/source_routes.py#L277) | upload_id, request |  |
| [content](../harness/verticals/retail/source_routes.py#L282) | upload_id, request |  |
| [complete](../harness/verticals/retail/source_routes.py#L319) | upload_id, request |  |
| [cancel](../harness/verticals/retail/source_routes.py#L328) | upload_id, request |  |
| [sources](../harness/verticals/retail/source_routes.py#L335) | request |  |
| [add_source](../harness/verticals/retail/source_routes.py#L345) | request |  |
| [source](../harness/verticals/retail/source_routes.py#L353) | source_id, request |  |

### harness/verticals/retail/source_service.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [code_identity](../harness/verticals/retail/source_service.py#L40) |  | Bind readiness to the worker's local source closure, including paid admission. |
| [digest](../harness/verticals/retail/source_service.py#L60) | value |  |
| [require](../harness/verticals/retail/source_service.py#L64) | ok, code |  |
| [private_dir](../harness/verticals/retail/source_service.py#L68) | path |  |
| [read](../harness/verticals/retail/source_service.py#L77) | path, uid, public |  |
| [lock](../harness/verticals/retail/source_service.py#L92) | path, exclusive |  |
| [load](../harness/verticals/retail/source_service.py#L116) | cls, state, company |  |
| [fingerprint](../harness/verticals/retail/source_service.py#L135) | self |  |
| [__init__](../harness/verticals/retail/source_service.py#L140) | self, state, company_id, clock, read_only |  |
| [configuration](../harness/verticals/retail/source_service.py#L148) | self |  |
| [code_current](../harness/verticals/retail/source_service.py#L150) | self |  |
| [records](../harness/verticals/retail/source_service.py#L154) | self |  |
| [save](../harness/verticals/retail/source_service.py#L171) | self, record |  |
| [healthy](../harness/verticals/retail/source_service.py#L176) | self, config |  |
| [policy](../harness/verticals/retail/source_service.py#L189) | self |  |
| [approval](../harness/verticals/retail/source_service.py#L195) | self, config |  |
| [collections](../harness/verticals/retail/source_service.py#L203) | self, actor |  |
| [readiness](../harness/verticals/retail/source_service.py#L208) | self, actor, collection | Safe observed admission state; continuation survives config removal. |
| [capabilities](../harness/verticals/retail/source_service.py#L234) | self, actor |  |
| [begin_remote](../harness/verticals/retail/source_service.py#L240) | self, store, actor, source_id, filename, size, idempotency_key, object_key, source_version, current | Host callback for fixed storage readers; reserve the ordinary file allowance. |
| [begin](../harness/verticals/retail/source_service.py#L259) | self, store, actor, collection, filename, size, idempotency_key, source_id, current, _remote |  |
| [_bind](../harness/verticals/retail/source_service.py#L306) | self, store, record, current |  |
| [authorize](../harness/verticals/retail/source_service.py#L320) | self, actor, view, operation |  |
| [recover_admissions](../harness/verticals/retail/source_service.py#L331) | self, store |  |
| [root_bytes](../harness/verticals/retail/source_service.py#L337) | path, expected_uid |  |
| [__init__](../harness/verticals/retail/source_service.py#L349) | self, host, config, media, qdrant, receipt_path, root_reader |  |
| [installed](../harness/verticals/retail/source_service.py#L353) | self |  |
| [__call__](../harness/verticals/retail/source_service.py#L375) | self |  |
| [__init__](../harness/verticals/retail/source_service.py#L388) | self, host, store, worker, probe, sleep_seconds |  |
| [write_health](../harness/verticals/retail/source_service.py#L394) | self |  |
| [pulse](../harness/verticals/retail/source_service.py#L402) | self |  |
| [_jobs](../harness/verticals/retail/source_service.py#L418) | self |  |
| [_attempts](../harness/verticals/retail/source_service.py#L430) | self, job |  |
| [reconcile](../harness/verticals/retail/source_service.py#L444) | self | Stop stale owned effects; retries and financial holds remain explicit. |
| [step](../harness/verticals/retail/source_service.py#L488) | self |  |
| [run](../harness/verticals/retail/source_service.py#L512) | self |  |
| [main_async](../harness/verticals/retail/source_service.py#L539) | state |  |
| [main](../harness/verticals/retail/source_service.py#L557) |  |  |

### harness/verticals/retail/source_visibility.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_imported](../harness/verticals/retail/source_visibility.py#L32) | row |  |
| [_receipt](../harness/verticals/retail/source_visibility.py#L36) | value |  |
| [_authority](../harness/verticals/retail/source_visibility.py#L43) | store, principal, asset_ids | One source-store read snapshot; no index lock or media decoder is held. |
| [_allowed](../harness/verticals/retail/source_visibility.py#L75) | row, authority, store |  |
| [_report](../harness/verticals/retail/source_visibility.py#L87) | rows, original |  |
| [_read_only](../harness/verticals/retail/source_visibility.py#L102) | *args, **kwargs |  |
| [ready_index_view](../harness/verticals/retail/source_visibility.py#L106) | index, store, principal_id | Capture one principal's coherent read-only view without changing the index. |
| [__init__](../harness/verticals/retail/source_visibility.py#L153) | self, index, company_state |  |
| [_store](../harness/verticals/retail/source_visibility.py#L160) | self |  |
| [snapshot](../harness/verticals/retail/source_visibility.py#L167) | self, principal_id, source, refresh, apply_scope |  |
| [bind](../harness/verticals/retail/source_visibility.py#L182) | self, view, check_exit |  |
| [current](../harness/verticals/retail/source_visibility.py#L193) | self |  |
| [refresh](../harness/verticals/retail/source_visibility.py#L197) | self |  |
| [__copy__](../harness/verticals/retail/source_visibility.py#L201) | self |  |
| [__getattr__](../harness/verticals/retail/source_visibility.py#L204) | self, name |  |
| [chat_source_view](../harness/verticals/retail/source_visibility.py#L210) | index, principal_id | Bind saved chat ownership and preserve any narrower native/scheduler view. |

### harness/verticals/retail/source_worker.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__post_init__](../harness/verticals/retail/source_worker.py#L55) | self |  |
| [_thread](../harness/verticals/retail/source_worker.py#L67) | function, *args, **kwargs |  |
| [_settle](../harness/verticals/retail/source_worker.py#L79) | awaitable | Finish finite cleanup despite another cancellation of its owner. |
| [_original](../harness/verticals/retail/source_worker.py#L89) | store, lease |  |
| [_hash](../harness/verticals/retail/source_worker.py#L103) | path |  |
| [_finite](../harness/verticals/retail/source_worker.py#L107) | value, low, high |  |
| [_regular](../harness/verticals/retail/source_worker.py#L113) | path |  |
| [_directory](../harness/verticals/retail/source_worker.py#L120) | path |  |
| [_fsync_dir](../harness/verticals/retail/source_worker.py#L128) | path |  |
| [validate_manifest](../harness/verticals/retail/source_worker.py#L134) | value, context, recipe | Verify source binding, bounded numeric claims and the exact file catalogue. |
| [__init__](../harness/verticals/retail/source_worker.py#L188) | self, store, limits |  |
| [acquire](../harness/verticals/retail/source_worker.py#L192) | self, size, entries |  |
| [stage](../harness/verticals/retail/source_worker.py#L213) | self, asset_id, label |  |
| [allocation](../harness/verticals/retail/source_worker.py#L222) | self, size, entries |  |
| [load](../harness/verticals/retail/source_worker.py#L233) | self, asset_id, receipt |  |
| [seal](../harness/verticals/retail/source_worker.py#L245) | identity, path |  |
| [__init__](../harness/verticals/retail/source_worker.py#L254) | self, client, deadline |  |
| [request](../harness/verticals/retail/source_worker.py#L255) | self, *args, **kwargs |  |
| [__init__](../harness/verticals/retail/source_worker.py#L264) | self, state, resolver_ready, client, seconds |  |
| [publish](../harness/verticals/retail/source_worker.py#L268) | self, records, vectors, metadata |  |
| [before_commit](../harness/verticals/retail/source_worker.py#L271) | snapshot, promote |  |
| [__init__](../harness/verticals/retail/source_worker.py#L285) | self, store, company_id, media_client, media_image, embedding_adapter, publisher, enabled, limits, scope_factory |  |
| [checkpoint](../harness/verticals/retail/source_worker.py#L295) | self, lease, **body |  |
| [run_once](../harness/verticals/retail/source_worker.py#L299) | self, worker_id, stages, asset_id |  |
| [heartbeat](../harness/verticals/retail/source_worker.py#L308) |  |  |
| [_scope](../harness/verticals/retail/source_worker.py#L341) | self, context, lease |  |
| [prepare](../harness/verticals/retail/source_worker.py#L349) | self, lease, context, stop |  |
| [receive_prepared](../harness/verticals/retail/source_worker.py#L396) | self, lease, context, scope, handle, result |  |
| [prepared](../harness/verticals/retail/source_worker.py#L449) | self, context |  |
| [embed](../harness/verticals/retail/source_worker.py#L459) | self, lease, context, stop |  |
| [records](../harness/verticals/retail/source_worker.py#L517) | self, context |  |
| [publish](../harness/verticals/retail/source_worker.py#L553) | self, lease, context |  |

### harness/verticals/retail/stock_commissioning.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [canonical](../harness/verticals/retail/stock_commissioning.py#L16) | value |  |
| [digest](../harness/verticals/retail/stock_commissioning.py#L20) | value |  |
| [file_sha](../harness/verticals/retail/stock_commissioning.py#L24) | path |  |
| [load](../harness/verticals/retail/stock_commissioning.py#L29) | path, limit |  |
| [save](../harness/verticals/retail/stock_commissioning.py#L36) | path, value, immutable |  |
| [finite](../harness/verticals/retail/stock_commissioning.py#L69) | value |  |
| [result_key](../harness/verticals/retail/stock_commissioning.py#L73) | stream_id, start, end |  |
| [verify_prepared](../harness/verticals/retail/stock_commissioning.py#L79) | row |  |
| [sampling_recipe](../harness/verticals/retail/stock_commissioning.py#L162) | name, requested | Reject unsupported/different settings; never silently drop a recipe knob. |
| [sampling_evidence](../harness/verticals/retail/stock_commissioning.py#L177) | params | Snapshot actual vLLM object attributes, including defaults not forwarded. |
| [reasoning_prompt](../harness/verticals/retail/stock_commissioning.py#L186) | prepared | Keep the business schema and host binding; append only the user directive. |
| [clock_receipt](../harness/verticals/retail/stock_commissioning.py#L195) | model_input_sha256, encoded_pts, decoded_pts, running_pts, segments | Verify actual before/after identity probes against encoded presentation PTS. |
| [finite_segment_preflight](../harness/verticals/retail/stock_commissioning.py#L235) | clock, segment_seconds | Stock finalizes at current_pts-1ns; an endpoint frame alone cannot flush. |
| [build_config](../harness/verticals/retail/stock_commissioning.py#L257) | rows, base, prepared, recipe_name, segment_seconds |  |
| [__init__](../harness/verticals/retail/stock_commissioning.py#L296) | self, folder, prepared, plans, clocks, recipe_name |  |
| [receive](../harness/verticals/retail/stock_commissioning.py#L306) | self, kind, value |  |
| [reject](../harness/verticals/retail/stock_commissioning.py#L368) | self, key, reason |  |
| [validate_supervisor](../harness/verticals/retail/stock_commissioning.py#L374) | receipt, worker_pid, worker_pgid, worker_sid, parent_pid, parent_pgid, deadline_epoch, manifest_sha256 | Require an explicit host-owned teardown contract for this isolated worker. |

### harness/verticals/retail/stock_commissioning_observer.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/verticals/retail/stock_commissioning_observer.py#L13) | self, folder, prepared, joiner |  |
| [simple](../harness/verticals/retail/stock_commissioning_observer.py#L21) | self, v |  |
| [hook](../harness/verticals/retail/stock_commissioning_observer.py#L34) | self, frame, event, arg |  |
| [safe_hook](../harness/verticals/retail/stock_commissioning_observer.py#L159) | self, frame, event, arg |  |
| [install](../harness/verticals/retail/stock_commissioning_observer.py#L171) | self |  |

### harness/verticals/retail/stock_supervisor.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_prctl](../harness/verticals/retail/stock_supervisor.py#L38) | option, arg |  |
| [install_group_filter](../harness/verticals/retail/stock_supervisor.py#L45) |  | Called only inside the isolated child, before the worker can fork. |
| [_private_json](../harness/verticals/retail/stock_supervisor.py#L95) | path, expected_sha |  |
| [validate_provider_reference](../harness/verticals/retail/stock_supervisor.py#L115) | path, expected_sha, deadline_epoch, manifest_sha256, now | Validate a prior host attestation's binding, not the remote provider state. |
| [_group_signal](../harness/verticals/retail/stock_supervisor.py#L148) | pid, signum |  |
| [_group_present](../harness/verticals/retail/stock_supervisor.py#L153) | pid |  |
| [_gated_worker](../harness/verticals/retail/stock_supervisor.py#L161) | gate, ready, parent_pid, command |  |
| [supervise](../harness/verticals/retail/stock_supervisor.py#L178) | command, manifest, output, deadline_epoch, provider_receipt, provider_sha256, max_log_bytes | Host-only launch primitive; CLI below pins command to the stock runner. |
| [main](../harness/verticals/retail/stock_supervisor.py#L388) |  |  |

### harness/verticals/retail/storage_connections.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [initialize_schema](../harness/verticals/retail/storage_connections.py#L21) | db |  |
| [public_values](../harness/verticals/retail/storage_connections.py#L34) | db, key |  |
| [_grant](../harness/verticals/retail/storage_connections.py#L39) | db, key |  |
| [validate_target](../harness/verticals/retail/storage_connections.py#L45) | target, declared |  |
| [metadata](../harness/verticals/retail/storage_connections.py#L77) | self |  |
| [config](../harness/verticals/retail/storage_connections.py#L81) | self |  |
| [sha256](../harness/verticals/retail/storage_connections.py#L86) | self |  |
| [__init__](../harness/verticals/retail/storage_connections.py#L91) | self, store, sources |  |
| [_owned](../harness/verticals/retail/storage_connections.py#L97) | self, db, key, owner, collection |  |
| [propose](../harness/verticals/retail/storage_connections.py#L103) | self, key, target, reason, expected_revision, owner, collection |  |
| [approve](../harness/verticals/retail/storage_connections.py#L127) | self, key, proposal_id, owner, collection |  |
| [pause](../harness/verticals/retail/storage_connections.py#L147) | self, key, expected_generation, owner, collection |  |
| [describe](../harness/verticals/retail/storage_connections.py#L156) | self, key, owner, collection |  |
| [_binding](../harness/verticals/retail/storage_connections.py#L171) | self, db, key, owner, collection |  |
| [snapshot](../harness/verticals/retail/storage_connections.py#L183) | self, key, owner, collection |  |
| [_current](../harness/verticals/retail/storage_connections.py#L199) | self, db, snapshot |  |
| [current](../harness/verticals/retail/storage_connections.py#L216) | self, snapshot | Read-only, zero-busy probe for the transport's event-loop guard. |
| [credentials](../harness/verticals/retail/storage_connections.py#L260) | self, snapshot |  |

### harness/verticals/retail/storage_routes.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [register_storage_routes](../harness/verticals/retail/storage_routes.py#L9) | app, identity, runtime_for_workspace, owner_for_connector |  |
| [selected](../harness/verticals/retail/storage_routes.py#L12) | request, key, write |  |
| [public](../harness/verticals/retail/storage_routes.py#L21) | value, request |  |
| [status](../harness/verticals/retail/storage_routes.py#L25) | connector_id, request |  |
| [approve](../harness/verticals/retail/storage_routes.py#L29) | connector_id, request |  |
| [run](../harness/verticals/retail/storage_routes.py#L38) | connector_id, request |  |
| [pause](../harness/verticals/retail/storage_routes.py#L47) | connector_id, request |  |

### harness/verticals/retail/storage_runtime.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [code_identity](../harness/verticals/retail/storage_runtime.py#L31) |  |  |
| [load](../harness/verticals/retail/storage_runtime.py#L53) | cls, state |  |
| [sha256](../harness/verticals/retail/storage_runtime.py#L70) | self |  |
| [__init__](../harness/verticals/retail/storage_runtime.py#L74) | self, state |  |
| [db](../harness/verticals/retail/storage_runtime.py#L83) | self |  |
| [get](../harness/verticals/retail/storage_runtime.py#L88) | self, key, owner, collection |  |
| [records](../harness/verticals/retail/storage_runtime.py#L92) | self |  |
| [request](../harness/verticals/retail/storage_runtime.py#L94) | self, snapshot |  |
| [stop_intent](../harness/verticals/retail/storage_runtime.py#L106) | self, key, owner, collection |  |
| [lock](../harness/verticals/retail/storage_runtime.py#L110) | self, key |  |
| [current](../harness/verticals/retail/storage_runtime.py#L116) | self, row |  |
| [update](../harness/verticals/retail/storage_runtime.py#L125) | self, row, status, cleanup, error, retire |  |
| [reconcile](../harness/verticals/retail/storage_runtime.py#L131) | self, row |  |
| [__init__](../harness/verticals/retail/storage_runtime.py#L148) | self, authority, source_host, clock, access_state, environment |  |
| [healthy](../harness/verticals/retail/storage_runtime.py#L154) | self |  |
| [member_current](../harness/verticals/retail/storage_runtime.py#L165) | self, owner |  |
| [current](../harness/verticals/retail/storage_runtime.py#L178) | self, snapshot |  |
| [_source](../harness/verticals/retail/storage_runtime.py#L180) | self, key, value, owner, collection |  |
| [funded](../harness/verticals/retail/storage_runtime.py#L186) | self, owner, collection, source |  |
| [describe](../harness/verticals/retail/storage_runtime.py#L199) | self, key, owner, collection |  |
| [fingerprint](../harness/verticals/retail/storage_runtime.py#L205) | key |  |
| [approve](../harness/verticals/retail/storage_runtime.py#L233) | self, key, proposal_id, owner, collection |  |
| [run](../harness/verticals/retail/storage_runtime.py#L237) | self, key, owner, collection, expected_generation |  |
| [request](../harness/verticals/retail/storage_runtime.py#L239) |  |  |
| [pause](../harness/verticals/retail/storage_runtime.py#L250) | self, key, owner, collection, expected_generation, timeout |  |
| [revoke](../harness/verticals/retail/storage_runtime.py#L251) |  |  |

### harness/verticals/retail/storage_service.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../harness/verticals/retail/storage_service.py#L22) | self, runtime, acquirer, tick_seconds |  |
| [configured](../harness/verticals/retail/storage_service.py#L29) | self |  |
| [health](../harness/verticals/retail/storage_service.py#L34) | self |  |
| [pulse](../harness/verticals/retail/storage_service.py#L40) | self |  |
| [acquire](../harness/verticals/retail/storage_service.py#L45) | self, row |  |
| [current](../harness/verticals/retail/storage_service.py#L51) |  |  |
| [step](../harness/verticals/retail/storage_service.py#L73) | self |  |
| [run](../harness/verticals/retail/storage_service.py#L92) | self |  |
| [main_async](../harness/verticals/retail/storage_service.py#L116) | state |  |
| [main](../harness/verticals/retail/storage_service.py#L127) |  |  |

### harness/verticals/retail/stream_ingestion.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [canonical](../harness/verticals/retail/stream_ingestion.py#L28) | value |  |
| [explicit_association](../harness/verticals/retail/stream_ingestion.py#L42) | self |  |
| [intervals](../harness/verticals/retail/stream_ingestion.py#L67) | self |  |
| [__init__](../harness/verticals/retail/stream_ingestion.py#L90) | self, state, monitoring, clock |  |
| [connect](../harness/verticals/retail/stream_ingestion.py#L116) | self |  |
| [_authorize](../harness/verticals/retail/stream_ingestion.py#L121) | self, owner, spec |  |
| [accept_model_response](../harness/verticals/retail/stream_ingestion.py#L133) | self, owner, context, raw_response, adapter_receipt | Host adapter for the actual JSON response, without model-supplied trust flags. |
| [model_claim](../harness/verticals/retail/stream_ingestion.py#L148) | self, owner, event_id | Read a committed claim with current source authorization and exact raw bytes. |
| [accept](../harness/verticals/retail/stream_ingestion.py#L171) | self, owner, window, _model_response, _adapter_receipt | Recoverable inbox → immutable events → durable downstream work. |
| [history](../harness/verticals/retail/stream_ingestion.py#L259) | self, owner, stream_id, limit |  |
| [drain](../harness/verticals/retail/stream_ingestion.py#L281) | self, owner, handlers, limit | Run bounded host handlers; failed remote work stays explicit for review. |

### harness/verticals/retail/stream_runtime.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [setup_catalog_inspection](../harness/verticals/retail/stream_runtime.py#L11) | selected |  |
| [authorized](../harness/verticals/retail/stream_runtime.py#L13) | owner, event |  |
| [resolve](../harness/verticals/retail/stream_runtime.py#L18) | owner, source_id |  |
| [setup_shelf_catalog](../harness/verticals/retail/stream_runtime.py#L46) | selected | Explicit commissioning plus per-photo consent precede paid photo egress. |
| [funded](../harness/verticals/retail/stream_runtime.py#L57) |  |  |
| [drain_stream](../harness/verticals/retail/stream_runtime.py#L67) | selected |  |
| [stream_tick](../harness/verticals/retail/stream_runtime.py#L85) | selected |  |

### harness/verticals/retail/tracker_presentation.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [specs](../harness/verticals/retail/tracker_presentation.py#L34) | write |  |
| [tracker_of](../harness/verticals/retail/tracker_presentation.py#L57) | state, owner, collection, tracker_id | The tracker record an id names: the record's own id, or the id of its Tracking Agent. |
| [agent_tracker_record](../harness/verticals/retail/tracker_presentation.py#L66) | company, agent, change, profiles, expected_revision, allowed | The tracker record a save for a Tracking Agent writes to. |
| [describe](../harness/verticals/retail/tracker_presentation.py#L102) | state, owner, collection, tracker, covered, revision | What `get_tracker_presentation` answers for one tracker record. |
| [save](../harness/verticals/retail/tracker_presentation.py#L136) | company, tracker, change, expected_revision, saved_by | Save a tracker's presentation and carry it into the published page. One function for the harness tool and for a person's route. |
| [read](../harness/verticals/retail/tracker_presentation.py#L150) | context, name, args |  |
| [call](../harness/verticals/retail/tracker_presentation.py#L163) | context, name, args |  |
| [_profiles](../harness/verticals/retail/tracker_presentation.py#L179) | monitoring, owner, agent |  |
| [save_for_agent](../harness/verticals/retail/tracker_presentation.py#L189) | selected, agent, change, expected_revision | A person's save for a Tracking Agent's tracker, from the host's own stores. |

### harness/verticals/retail/tracker_runner.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [canonical](../harness/verticals/retail/tracker_runner.py#L106) | value |  |
| [digest](../harness/verticals/retail/tracker_runner.py#L110) | value |  |
| [iso](../harness/verticals/retail/tracker_runner.py#L114) | epoch |  |
| [read_only](../harness/verticals/retail/tracker_runner.py#L121) | path | A read-only connection to a company store, or None while the store has no file yet. |
| [engine_sources](../harness/verticals/retail/tracker_runner.py#L138) |  | Every file that decides what a pass computes: the recipe, its processors, the accumulation step, the basket reducer, the product types and the page publisher. |
| [engine_revision](../harness/verticals/retail/tracker_runner.py#L146) | sources | The revision of the maintained code this process runs a pass with. A release that changes any of it moves every location's stamp, so each location recomputes once. |
| [installed_locations](../harness/verticals/retail/tracker_runner.py#L161) | state | Every (owner, collection, location) of this company that has installed trackers. |
| [input_stamp](../harness/verticals/retail/tracker_runner.py#L175) | state, owner, collection, location_id | A stamp of everything a pass reads for one location. It moves when an input row is added, rewritten or removed, when the location's place in the company changes, and with a new revision of the maintained processors. What a pass writes itself (derived rows, outputs) stays out. |
| [scope_revision](../harness/verticals/retail/tracker_runner.py#L206) | state, collection | The revision of the collection's place graph: its locations, rooms, cameras and members. |
| [script_wake_authorizer](../harness/verticals/retail/tracker_runner.py#L213) | selected | Bind the retail script signal's authority to this workspace's current stores. |
| [authorize](../harness/verticals/retail/tracker_runner.py#L215) | definition, wake, admit |  |
| [location_cameras](../harness/verticals/retail/tracker_runner.py#L253) | state, collection, location_id | Every camera the place graph has at a location: the cameras whose rows a pass reads. |
| [projection_pending](../harness/verticals/retail/tracker_runner.py#L260) | state, owner | How many of the owner's queued stream projections wait to reach the location store. |
| [drain_projections](../harness/verticals/retail/tracker_runner.py#L270) | company, limit | Bring the owner's queued projections into the location store, oldest first; returns how many. |
| [commit_count](../harness/verticals/retail/tracker_runner.py#L305) | state, owner | How many observations the owner has committed. The commit store only ever grows. |
| [committed_after](../harness/verticals/retail/tracker_runner.py#L313) | state, owner, collection, cursor, limit | The owner's committed observations of a collection past a cursor, in the order they were committed: [(position, observation)]. The position is the commit store's own row number, which only grows, so a commit is read once whatever the host clock said when it was made. |
| [committed_events](../harness/verticals/retail/tracker_runner.py#L325) | state, owner, event_ids | The owner's committed observations with these ids, in commit order. |
| [saved_zone](../harness/verticals/retail/tracker_runner.py#L337) | state, owner, location_id | The timezone of the location's saved coordinates, when it has them. |
| [current_outputs](../harness/verticals/retail/tracker_runner.py#L344) | state, owner, collection, location_id | The current output of each tracker the owner has: its tile, canvas and revision. |
| [output_cameras](../harness/verticals/retail/tracker_runner.py#L357) | state, owner, collection, location_id | Every camera the location's current outputs read, without their tiles and canvases. |
| [output_revisions](../harness/verticals/retail/tracker_runner.py#L367) | state, owner, location_id | Each current output's tracker key, location and revision, read without its tile and canvas. |
| [prune_output_revisions](../harness/verticals/retail/tracker_runner.py#L380) | company, location_id, keep | Keep each tracker's newest output revisions at a location; returns how many rows went. The current output is a row of its own and stays whole. |
| [page_directory](../harness/verticals/retail/tracker_runner.py#L396) | state, owner |  |
| [page_location](../harness/verticals/retail/tracker_runner.py#L401) | state, owner | The location the owner's published page shows, once a host import has published one. |
| [page_digest](../harness/verticals/retail/tracker_runner.py#L411) | state, owner | The sha256 of the owner's page data as it is published now, read once per file version. |
| [ledger_mark](../harness/verticals/retail/tracker_runner.py#L431) | state | A mark that moves with every write to the company's run ledger: one file stat. |
| [clean_policy](../harness/verticals/retail/tracker_runner.py#L440) | value | A location's run policy, checked: the fields `set_tracker_schedule` writes. |
| [__init__](../harness/verticals/retail/tracker_runner.py#L470) | self, state, clock |  |
| [connect](../harness/verticals/retail/tracker_runner.py#L478) | self, write |  |
| [state](../harness/verticals/retail/tracker_runner.py#L523) | self, owner, collection, location_id, **options |  |
| [policy](../harness/verticals/retail/tracker_runner.py#L526) | self, owner, collection, location_id, **options |  |
| [set_policy](../harness/verticals/retail/tracker_runner.py#L529) | self, owner, collection, location_id, changes, **options |  |
| [request](../harness/verticals/retail/tracker_runner.py#L532) | self, owner, collection, location_id, **options |  |
| [pending_location_jobs](../harness/verticals/retail/tracker_runner.py#L535) | self, owner, collection, location_id | An admitted signal job retains its location until original cleanup confirms. |
| [claim](../harness/verticals/retail/tracker_runner.py#L557) | self, owner, collection, location_id, **options |  |
| [finish](../harness/verticals/retail/tracker_runner.py#L562) | self, run_id, lease_token, **options |  |
| [reap](../harness/verticals/retail/tracker_runner.py#L571) | self, owner, collection, location_id, **options |  |
| [record](../harness/verticals/retail/tracker_runner.py#L574) | self, owner, collection, location_id, **options |  |
| [runs](../harness/verticals/retail/tracker_runner.py#L577) | self, owner, collection, location_id, **options |  |
| [forget_tracker](../harness/verticals/retail/tracker_runner.py#L580) | self, owner, collection, location_id, key |  |
| [job_open](../harness/verticals/retail/tracker_runner.py#L583) | self, job, owner, collection, location_id, tracker_id |  |
| [last_run](../harness/verticals/retail/tracker_runner.py#L586) | self, owner, location_id |  |
| [projection](../harness/verticals/retail/tracker_runner.py#L590) | self, owner, collection | Where the reading of the owner's commits stands: how many commits were counted, the position of the last one read, the place graph's revision at that reading and how many observations wait for their recording's camera. |
| [unplaced](../harness/verticals/retail/tracker_runner.py#L605) | self, owner, collection | The observations that wait for their recording's camera: {observation id: recording id}. |
| [set_projection](../harness/verticals/retail/tracker_runner.py#L616) | self, owner, collection, commits, cursor, scope, placed, unplaced | Record one reading of the commits: the cursor, which waiting observations found their place and which new ones wait. The newest UNPLACED_KEEP waiting observations are kept. |
| [service](../harness/verticals/retail/tracker_runner.py#L629) | self | The service's note for this company: `on` once a sweep has read it, `off` when the host started the service switched off, `waiting` until either; and the fault of the last sweep. |
| [note_service](../harness/verticals/retail/tracker_runner.py#L641) | self, state, fault | Write the service's note when it changes. |
| [home_revision](../harness/verticals/retail/tracker_runner.py#L652) | state, owner, location_id | What a page polls: the revision of the owner's published page data, the trackers' output revisions, the location's schedule as the tools set it and the newest run. The revision moves once the new page data is in place. |
| [location_name](../harness/verticals/retail/tracker_runner.py#L674) | company, location_id | The location's own name in the company's records. |
| [projection_due](../harness/verticals/retail/tracker_runner.py#L680) | runs, state, owner, collection, drain | Whether a sweep has observations to bring into the location store for this owner and collection. |
| [project_observations](../harness/verticals/retail/tracker_runner.py#L687) | company, runs, drain, limit | Bring the owner's committed observations of this collection into the location store. |
| [at_daily_time](../harness/verticals/retail/tracker_runner.py#L746) | zone, daily_at, now | Whether the location's daily time has come on its own clock at `now`. A location with no daily time has its day from the first moment of it. |
| [due](../harness/verticals/retail/tracker_runner.py#L760) | runs, state, owner, collection, location_id, now, pending_since | Why this location's trackers should run now: (trigger, stamp, day), else None. |
| [pass_access](../harness/verticals/retail/tracker_runner.py#L789) | company, location_id | Confirm that the member a pass acts as manages the location and reaches every camera of it. |
| [run_location](../harness/verticals/retail/tracker_runner.py#L803) | company, location_id, runs, trigger, stamp, day, budget_seconds, custom, clock | One pass of one location, under its lease. Returns the closed run, or None while another pass holds the lease. |
| [script_phase](../harness/verticals/retail/tracker_runner.py#L897) | company, location_id, runs, claimed, result, custom, trigger, day, daily, published, clock | The script trackers of a pass, after its own work: its Core Trackers have run and its page data is published. |
| [__init__](../harness/verticals/retail/tracker_runner.py#L934) | self, company, location_id, stamp |  |
| [mark](../harness/verticals/retail/tracker_runner.py#L938) | self | Call right before the run: the inputs present now are the ones this run reads. |
| [done](../harness/verticals/retail/tracker_runner.py#L942) | self, result, page, covers_inputs | The run's result. `covers_inputs` says the run was the location's whole pass with its page. |
| [host_pass](../harness/verticals/retail/tracker_runner.py#L949) | company, location_id, runs, wait_seconds, lease_seconds, beat_seconds, hold_seconds, clock, sleep | The lease a host command holds while it derives, runs or publishes a location. |
| [renew](../harness/verticals/retail/tracker_runner.py#L975) |  |  |
| [pass_company](../harness/verticals/retail/tracker_runner.py#L1018) | state, access_state, environment, owner, collection | The handle an unattended pass acts through: the installing owner, with the membership the server itself reads. A member is a person of the access registry who is an owner or operator of this company; anyone else is no member, whatever one leftover row says. |
| [member](../harness/verticals/retail/tracker_runner.py#L1027) | principal |  |
| [environments](../harness/verticals/retail/tracker_runner.py#L1036) | access_state | Every company environment in the access registry. |
| [environment_state](../harness/verticals/retail/tracker_runner.py#L1047) | root, environment | The state directory of one company environment. |
| [note_fault](../harness/verticals/retail/tracker_runner.py#L1052) | root, environment, runs, error | One company's stores stopped its sweep. The fault is logged once, where an operator reads it, and kept in that company's service note, where its tools read it. |
| [note_swept](../harness/verticals/retail/tracker_runner.py#L1065) | root, environment, runs | One company was read whole: its service note says `on`, and an earlier fault is over. |
| [tracker_pass](../harness/verticals/retail/tracker_runner.py#L1072) | root, access_state, clock, custom, limit, stop, pending_since, served | One sweep over every company environment: project, probe, and run what is due. |
| [company](../harness/verticals/retail/tracker_runner.py#L1090) | owner, collection, environment, state, opened |  |
| [runner_state](../harness/verticals/retail/tracker_runner.py#L1148) | root, access_state, environ | The server's handle on this job, made once at startup. ROCOTO_TILE_RUNNER=off stops it, and each company with trackers then reads `off` in its service note, so a tool that takes a request says the request waits. |
| [tracker_start](../harness/verticals/retail/tracker_runner.py#L1174) | app_state, sandbox | Called once on the server's event loop as it starts: script trackers join the passes. |
| [recover_script_jobs](../harness/verticals/retail/tracker_runner.py#L1199) | root, access_state, box | Clear the sandbox jobs each company's ledger still lists as open. Returns how many were cleared. |
| [tracker_tick](../harness/verticals/retail/tracker_runner.py#L1217) | app_state | Called every second by the server loop: one sweep at a time, a new one every PROBE_SECONDS. |
| [tracker_stop](../harness/verticals/retail/tracker_runner.py#L1246) | app_state | At shutdown: ask the sweep to stop between locations and wait for the pass in hand to close its run row. |

### harness/verticals/retail/tracker_scripts.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [_listed](../harness/verticals/retail/tracker_scripts.py#L183) | names |  |
| [__init__](../harness/verticals/retail/tracker_scripts.py#L267) | self, errors |  |
| [canonical](../harness/verticals/retail/tracker_scripts.py#L272) | value | The sandbox's own canonical JSON (`custom_worker.canonical`). |
| [iso](../harness/verticals/retail/tracker_scripts.py#L277) | epoch |  |
| [fault](../harness/verticals/retail/tracker_scripts.py#L281) | code, message, **more |  |
| [named](../harness/verticals/retail/tracker_scripts.py#L288) | name, period |  |
| [job_periods](../harness/verticals/retail/tracker_scripts.py#L292) | company, location_id, data, day | The periods of one job: the day, then the week, the month and the year the page reads. |
| [prior_of](../harness/verticals/retail/tracker_scripts.py#L300) | output | What a script reads of the output published before its run. |
| [without_internal](../harness/verticals/retail/tracker_scripts.py#L309) | value | A host row as a script reads it: the host's own provenance fields left out at every depth. |
| [build_input](../harness/verticals/retail/tracker_scripts.py#L318) | data, tracker, periods, connections, prior, seconds | The JSON document one job reads: the periods, the tracker's own events and bounded location rows. |
| [input_digest](../harness/verticals/retail/tracker_scripts.py#L372) | document | The identity of a job's input: everything a script computes from. The prior output stays out, so a script that reads it still settles on one result for the same events and records. |
| [input_parts](../harness/verticals/retail/tracker_scripts.py#L378) | document | The input as the files a job mounts: [('input/000.json', bytes), …], each within one file's size. |
| [snapshot_for](../harness/verticals/retail/tracker_scripts.py#L386) | company_id, owner, collection, tracker_id, revision, source, parts, runtime | The sandbox bundle of one job: the entry, the script and the input, as the broker checks it. |
| [_number](../harness/verticals/retail/tracker_scripts.py#L408) | value | A number an output may carry: a finite float, or a whole number inside NUMBER_LIMIT. |
| [_text](../harness/verticals/retail/tracker_scripts.py#L415) | value, most, least |  |
| [host_field](../harness/verticals/retail/tracker_scripts.py#L419) | name | Whether a page reads this name as a picture, a clip or a link. |
| [_free](../harness/verticals/retail/tracker_scripts.py#L424) | value, path, errors, depth | A value under a key of the script's own: numbers, words and lists and objects of them, up to six levels. An object here is the script's own data and never an evidence row: the fields a page reads as a picture, a clip or a link, and the fields of a row's identity, are refused at every depth. |
| [_shown](../harness/verticals/retail/tracker_scripts.py#L455) | key | A key of the script's own as an error path names it: its first 40 characters. |
| [point_time](../harness/verticals/retail/tracker_scripts.py#L463) | value | A point's time as the host stores it: UTC, ending in Z, the form the Core Trackers write. None for a text that is another form of time, or none. |
| [_points](../harness/verticals/retail/tracker_scripts.py#L474) | value, path, errors |  |
| [_rows](../harness/verticals/retail/tracker_scripts.py#L489) | value, path, most, events, visits, errors | Evidence rows, rebuilt from the host's own records: the script chooses ids and words. |
| [validate_output](../harness/verticals/retail/tracker_scripts.py#L523) | value, tracker, document | One period's output, checked against the contract. Returns what `publish_output` stores. |
| [_size](../harness/verticals/retail/tracker_scripts.py#L613) | value | The bytes of a value's canonical JSON; past every size for a value JSON cannot hold. |
| [slot_texts](../harness/verticals/retail/tracker_scripts.py#L621) | slots, *written | Each marked slot with the text written for the same facts, where one was written. |
| [publish_output](../harness/verticals/retail/tracker_scripts.py#L635) | data, tracker, period, accepted, script_revision, texts | Write a validated output through the one writer of every tracker's output. |
| [content_of](../harness/verticals/retail/tracker_scripts.py#L650) | tile, canvas | The content hash `common.publish` gives a tile and canvas: their revision stays out of it. |
| [evaluate](../harness/verticals/retail/tracker_scripts.py#L814) | result, tracker, document | What a sandbox job amounts to: its status and, for a job whose every period is valid, the accepted outputs in period order. |
| [validate_source](../harness/verticals/retail/tracker_scripts.py#L863) | text |  |
| [__init__](../harness/verticals/retail/tracker_scripts.py#L868) | self, path, clock |  |
| [__init__](../harness/verticals/retail/tracker_scripts.py#L876) | self, **options |  |
| [run](../harness/verticals/retail/tracker_scripts.py#L884) | self, tracker_id, **options |  |
| [switches](../harness/verticals/retail/tracker_scripts.py#L891) | environ | The two host switches of script runs: the sandbox, and runs on the `events` trigger. |
| [box](../harness/verticals/retail/tracker_scripts.py#L900) |  | This process's sandbox handle. It stays switched off until `configure` has read the host's switches. |
| [configure](../harness/verticals/retail/tracker_scripts.py#L911) | loop, environ, sandbox, root | Called once as the service starts: the event loop script jobs run on, the host's switches and, with `root`, the service's state root, where the count of script jobs is kept. |
| [script_id](../harness/verticals/retail/tracker_scripts.py#L926) | tracker |  |
| [_suffix](../harness/verticals/retail/tracker_scripts.py#L930) | tracker |  |
| [_saved](../harness/verticals/retail/tracker_scripts.py#L934) | state, owner, kind, key | One record of the location store, read without opening the company for writing. |
| [__init__](../harness/verticals/retail/tracker_scripts.py#L962) | self, company, clock |  |
| [_get](../harness/verticals/retail/tracker_scripts.py#L965) | self, kind, key |  |
| [head](../harness/verticals/retail/tracker_scripts.py#L971) | self, tracker |  |
| [revision](../harness/verticals/retail/tracker_scripts.py#L974) | self, tracker, revision |  |
| [output](../harness/verticals/retail/tracker_scripts.py#L980) | self, tracker |  |
| [proposal](../harness/verticals/retail/tracker_scripts.py#L983) | self, tracker |  |
| [_change](../harness/verticals/retail/tracker_scripts.py#L986) | self, tracker, change | Apply `change(head, put)` to the head inside one transaction and return what it returns. |
| [put](../harness/verticals/retail/tracker_scripts.py#L995) | kind, value |  |
| [drop](../harness/verticals/retail/tracker_scripts.py#L998) | kind, key |  |
| [get](../harness/verticals/retail/tracker_scripts.py#L1000) | kind, key |  |
| [save](../harness/verticals/retail/tracker_scripts.py#L1006) | self, tracker, source, expected_revision, policy, chat_id | Store the source as the next draft revision. `expected_revision` is the revision read, 0 for the first. |
| [change](../harness/verticals/retail/tracker_scripts.py#L1012) | head, put |  |
| [set_policy](../harness/verticals/retail/tracker_scripts.py#L1035) | self, tracker, changes, expected_revision |  |
| [change](../harness/verticals/retail/tracker_scripts.py#L1036) | head, put |  |
| [admit_job](../harness/verticals/retail/tracker_scripts.py#L1049) | self, tracker, most | Count one sandbox job against the tracker's day. False once the day's number is reached. |
| [change](../harness/verticals/retail/tracker_scripts.py#L1053) | head, put |  |
| [refund_job](../harness/verticals/retail/tracker_scripts.py#L1064) | self, tracker | Give the day its count back for a job the sandbox never took. |
| [change](../harness/verticals/retail/tracker_scripts.py#L1066) | head, put |  |
| [record_test](../harness/verticals/retail/tracker_scripts.py#L1072) | self, tracker, revision, status, run_id | Keep the last test of the head revision. A passing test of the paused revision starts the script again. |
| [change](../harness/verticals/retail/tracker_scripts.py#L1074) | head, put |  |
| [publish](../harness/verticals/retail/tracker_scripts.py#L1085) | self, tracker, expected_revision | Make the head revision the one that runs. It needs the passing test of that very revision. |
| [change](../harness/verticals/retail/tracker_scripts.py#L1087) | head, put |  |
| [after_run](../harness/verticals/retail/tracker_scripts.py#L1101) | self, tracker, revision, detail, error, input_sha256 | Carry a run into the script's health: its last run, its last good run, and the pause after PAUSE_AFTER stopped runs in a row. `error` is the run's own fault with the script's words; the health keeps it for the readers `get_tracker_script` shows it to. |
| [change](../harness/verticals/retail/tracker_scripts.py#L1108) | head, put |  |
| [note_day](../harness/verticals/retail/tracker_scripts.py#L1128) | self, tracker, day, done, retry | Keep how the script stands for a local day of its location: whether its run for that day is done, and how many passes the tracker service has asked for by itself. |
| [change](../harness/verticals/retail/tracker_scripts.py#L1140) | head, put |  |
| [propose](../harness/verticals/retail/tracker_scripts.py#L1153) | self, tracker, proposal |  |
| [change](../harness/verticals/retail/tracker_scripts.py#L1154) | head, put |  |
| [drop_proposal](../harness/verticals/retail/tracker_scripts.py#L1159) | self, tracker, proposal_id |  |
| [change](../harness/verticals/retail/tracker_scripts.py#L1160) | head, put |  |
| [put_readings](../harness/verticals/retail/tracker_scripts.py#L1169) | self, tracker, output, readings, script_revision | Store the week, month and year readings of the published output. They follow the output that stands now: a text written meanwhile gave it a newer revision. |
| [change](../harness/verticals/retail/tracker_scripts.py#L1172) | head, put |  |
| [clean_policy](../harness/verticals/retail/tracker_scripts.py#L1179) | value | A script's two policies, checked: when a valid output is published and when the agent is woken. |
| [saved_readings](../harness/verticals/retail/tracker_scripts.py#L1186) | company, location_id, trackers | The week, month and year readings of each script tracker's published output: {key: {name: {tile, canvas}}}. |
| [pause_reason](../harness/verticals/retail/tracker_scripts.py#L1195) | paused, words | Why a script is paused. With `words` the sentence carries the script's own message; a reader outside the location's cameras gets the code and the line. |
| [_plain_stop](../harness/verticals/retail/tracker_scripts.py#L1207) | error | A stopped run in this host's own words: its code and its line. |
| [health_of](../harness/verticals/retail/tracker_scripts.py#L1215) | head, words | A script's health as the tools return it. |
| [describe](../harness/verticals/retail/tracker_scripts.py#L1239) | head, words | What `get_tracker` returns of a tracker's script: its revision, policy, health and last test. |
| [describe_saved](../harness/verticals/retail/tracker_scripts.py#L1247) | state, owner, tracker | `describe` for a reader without a company handle: the head is read from the store's file. |
| [_bundle](../harness/verticals/retail/tracker_scripts.py#L1254) | periods, accepted |  |
| [readings_of](../harness/verticals/retail/tracker_scripts.py#L1259) | data, tracker, bundle, script_revision | The week, month and year readings of a job, as the page reads them. Nothing is stored. |
| [writing](../harness/verticals/retail/tracker_scripts.py#L1273) | tracker | The lock of one tracker's output in this service. A run's publish reads the output that stands and writes its next revision, and so does a written text: each holds this lock for the whole of that, so one never writes over the other. |
| [publish_bundle](../harness/verticals/retail/tracker_scripts.py#L1283) | scripts, data, tracker, bundle, script_revision, written | Publish a job's day output and store its week, month and year readings beside it. |
| [preview_bundle](../harness/verticals/retail/tracker_scripts.py#L1294) | scripts, data, tracker, bundle, script_revision, written | The tile and canvas a bundle would publish for its day, their content hash, and the hash of the same content before any text is written: (shown, content, unwritten). Nothing is stored. |
| [_sentence](../harness/verticals/retail/tracker_scripts.py#L1311) | error | A run row's words for a script that stopped: this host's own. The script's message stays with the script's health, where `get_tracker_script` reads it with the location's cameras. |
| [_public_error](../harness/verticals/retail/tracker_scripts.py#L1320) | error | A run's fault as a run row keeps it: the code, the line, the period and this host's sentence for the code. |
| [show_on_page](../harness/verticals/retail/tracker_scripts.py#L1328) | company, tracker | Carry one tracker's stored output and readings into the owner's published page, without a pass: the page publisher assembles that one row again. Returns whether the page data changed. |
| [wake_agent](../harness/verticals/retail/tracker_scripts.py#L1338) | company, tracker, event_id, text, clock, camera_ids | Enqueue one wake for the tracker's Tracking Agent through the durable wake queue, inside its bounds. |
| [current_producer_authority](../harness/verticals/retail/tracker_scripts.py#L1351) | definition, actor |  |
| [wake_text](../harness/verticals/retail/tracker_scripts.py#L1373) | tracker, detail, head, error, output, proposal | One short factual message for the agent a run wakes. The agent is the tracker's own: the message carries the script's words for a run that stopped. |
| [run_script_tracker](../harness/verticals/retail/tracker_scripts.py#L1403) | company, location_id, tracker, period, data, sandbox, clock, signals | One script tracker inside a pass. Synchronous: the pass calls it in its thread. |
| [closed](../harness/verticals/retail/tracker_scripts.py#L1433) | status, **more |  |
| [later](../harness/verticals/retail/tracker_scripts.py#L1437) | message, retry | A run that waits: its day stays owed, and with `retry` the service asks for the next pass. |
| [perform](../harness/verticals/retail/tracker_scripts.py#L1468) | control |  |
| [opened](../harness/verticals/retail/tracker_scripts.py#L1481) | job |  |
| [job_closed](../harness/verticals/retail/tracker_scripts.py#L1485) | job |  |
| [sandbox_processor](../harness/verticals/retail/tracker_scripts.py#L1572) | sandbox | The `custom` callback of `run_trackers`: a company's script tracker, run in the sandbox. |
| [custom](../harness/verticals/retail/tracker_scripts.py#L1574) | tracker, company, location_id, period, data |  |
| [test_script](../harness/verticals/retail/tracker_scripts.py#L1579) | company, tracker, expected_revision, cancelled, sandbox, clock | Run the head revision in the sandbox over the location's present data. Nothing is published. |
| [prepare](../harness/verticals/retail/tracker_scripts.py#L1598) |  |  |
| [conclude](../harness/verticals/retail/tracker_scripts.py#L1622) |  |  |
| [publish_script](../harness/verticals/retail/tracker_scripts.py#L1668) | company, tracker, expected_revision | Make the head revision the one that runs: the script's record, then the tracker's processor layer. |
| [approve_output](../harness/verticals/retail/tracker_scripts.py#L1681) | company, tracker, proposal_id | Publish the proposal a review-mode script is waiting with. Returns the stored output. |
| [write_text](../harness/verticals/retail/tracker_scripts.py#L1701) | company, tracker, slot, text, output_revision, proposal_id, clock | Store a written text in one slot of the published output, or of the waiting proposal. |
| [named](../harness/verticals/retail/tracker_scripts.py#L1722) | entries |  |
| [change](../harness/verticals/retail/tracker_scripts.py#L1728) | head, put |  |
| [_tool](../harness/verticals/retail/tracker_scripts.py#L1763) | name, description, properties, required |  |
| [specs](../harness/verticals/retail/tracker_scripts.py#L1768) | write |  |
| [_record](../harness/verticals/retail/tracker_scripts.py#L1810) | context, tracker_id | The saved tracker record a tool names: by its own id, or by the id of its Tracking Agent. |
| [_script_runs](../harness/verticals/retail/tracker_scripts.py#L1817) | context, record, limit | The tracker's newest script runs, each as one entry of the location's run history. |
| [_unlinked](../harness/verticals/retail/tracker_scripts.py#L1831) | context, tracker_id | A Tracking Agent of the reader that has yet to get its tracker record, by the id `list_trackers` gives it. |
| [script_camera_ids](../harness/verticals/retail/tracker_scripts.py#L1839) | state, owner, record | The cameras whose data a script's current output, proposal or run message may contain. |
| [reads_cameras](../harness/verticals/retail/tracker_scripts.py#L1849) | context, record, *records_ | Whether the reader's present access covers every camera a script's words come from: the cameras of the location, and the ones a stored output or proposal names. A script copies what it reads into its summary, its facts and the message of its own exception, so each of those is read with the cameras, like a Core Tracker's output. |
| [read](../harness/verticals/retail/tracker_scripts.py#L1860) | context, name, args |  |
| [_installed](../harness/verticals/retail/tracker_scripts.py#L1906) | context | The locations whose Core Trackers the writer installed: where that member's trackers run. |
| [_writable](../harness/verticals/retail/tracker_scripts.py#L1913) | context, company, args, link | The company's own tracker a write names, with the writer's authority over it checked. |
| [link_check](../harness/verticals/retail/tracker_scripts.py#L1941) | context, company, location_id, installed | Whether the writer may give a Tracking Agent its tracker record at a location: a location in their access that they manage and whose Core Trackers they installed, with room for one more. Raises with the sentence that says what is needed. |
| [link_agent](../harness/verticals/retail/tracker_scripts.py#L1959) | context, company, location_id, agent, installed | The tracker record of a Tracking Agent, written at a location through `add_tracker` the first time. |
| [promote_link](../harness/verticals/retail/tracker_scripts.py#L1980) | context, company, agent, location_id | After a chat became a Tracking Agent: its tracker record, where a location is named or the writer has one installed location. Returns {'tracker': record or None, 'next_step': sentence or None}. |
| [_public_head](../harness/verticals/retail/tracker_scripts.py#L1993) | head |  |
| [_page](../harness/verticals/retail/tracker_scripts.py#L1997) | company, record | What a tool says of the page after it changed an output: the tracker's own row is assembled again from the stored output, with no pass and no script run. |
| [call](../harness/verticals/retail/tracker_scripts.py#L2004) | context, name, args | The family's writes, in the hosted parent conversation. A Core Tracker answers each with LOCKED. |
| [acall](../harness/verticals/retail/tracker_scripts.py#L2044) | context, name, args | The family's awaited write: a test runs its sandbox job on the event loop of the turn. |

### harness/verticals/retail/visit_basket.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [counted](../harness/verticals/retail/visit_basket.py#L37) | self |  |
| [evidence_key](../harness/verticals/retail/visit_basket.py#L45) | owner, event_id |  |
| [item_key](../harness/verticals/retail/visit_basket.py#L49) | owner, collection, recording, reference |  |
| [project](../harness/verticals/retail/visit_basket.py#L53) | events, receipts, products, visit_id, at_s, valuation_at | Pure reducer over already-authorized inputs; quantities are absolute counts. |
| [describe](../harness/verticals/retail/visit_basket.py#L116) | item |  |
| [__init__](../harness/verticals/retail/visit_basket.py#L188) | self, locations, verifier |  |
| [_visit](../harness/verticals/retail/visit_basket.py#L191) | self, owner, visit_id |  |
| [admit](../harness/verticals/retail/visit_basket.py#L206) | self, owner, definition | Host-only receipt admission; verifier is executable host policy, not input. |
| [admit_model](../harness/verticals/retail/visit_basket.py#L231) | self, owner, event_id, pipeline | Produce an immutable qualified estimate from an admitted raw response. |
| [at](../harness/verticals/retail/visit_basket.py#L304) | self, owner, visit_id, at_s, valuation_at |  |

### harness/verticals/retail/watch_screening.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [nonempty](../harness/verticals/retail/watch_screening.py#L32) | self |  |
| [bounds](../harness/verticals/retail/watch_screening.py#L45) | self |  |
| [digest](../harness/verticals/retail/watch_screening.py#L51) | value |  |
| [source_key](../harness/verticals/retail/watch_screening.py#L55) | clip |  |
| [encoder_identity](../harness/verticals/retail/watch_screening.py#L59) | index |  |
| [author_plan](../harness/verticals/retail/watch_screening.py#L68) | state, plan, revision, owner, context |  |
| [validate_plan](../harness/verticals/retail/watch_screening.py#L84) | record, state |  |
| [coalesce](../harness/verticals/retail/watch_screening.py#L95) | records |  |
| [__init__](../harness/verticals/retail/watch_screening.py#L107) | self, state, index |  |
| [screen](../harness/verticals/retail/watch_screening.py#L113) | self, record, sources, snapshot |  |

### harness/verticals/retail/web/camera-streams.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [render](../harness/verticals/retail/web/camera-streams.js#L4) | { connections = [], query = '', loading = false, error = '', canManage = false, onSetup, onRetry }, { node, icon } |  |

### harness/verticals/retail/web/control-room.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [create](../harness/verticals/retail/web/control-room.js#L30) | options = {} |  |
| [read](../harness/verticals/retail/web/control-room.js#L45) | path |  |
| [profileName](../harness/verticals/retail/web/control-room.js#L59) | agent |  |
| [agentById](../harness/verticals/retail/web/control-room.js#L65) | id |  |
| [agentFrequency](../harness/verticals/retail/web/control-room.js#L66) | agent |  |
| [savePick](../harness/verticals/retail/web/control-room.js#L82) | id, family |  |
| [carryFormerPick](../harness/verticals/retail/web/control-room.js#L112) | id |  |
| [home](../harness/verticals/retail/web/control-room.js#L124) |  |  |
| [buildHome](../harness/verticals/retail/web/control-room.js#L128) |  |  |
| [incidentCard](../harness/verticals/retail/web/control-room.js#L139) | incident, index |  |
| [legacyDetail](../harness/verticals/retail/web/control-room.js#L144) | agent |  |
| [syncPhone](../harness/verticals/retail/web/control-room.js#L150) | focused |  |
| [applyPeriod](../harness/verticals/retail/web/control-room.js#L162) | period, source |  |
| [closeDetail](../harness/verticals/retail/web/control-room.js#L172) |  |  |
| [mountCanvas](../harness/verticals/retail/web/control-room.js#L178) | agent |  |
| [mountLegacy](../harness/verticals/retail/web/control-room.js#L186) | agent |  |
| [watch](../harness/verticals/retail/web/control-room.js#L194) |  |  |
| [render](../harness/verticals/retail/web/control-room.js#L199) |  |  |
| [openTracker](../harness/verticals/retail/web/control-room.js#L216) | id |  |
| [openCore](../harness/verticals/retail/web/control-room.js#L225) | tracker |  |
| [openFrom](../harness/verticals/retail/web/control-room.js#L233) | detail |  |
| [fromFrame](../harness/verticals/retail/web/control-room.js#L242) | event |  |
| [loadObservations](../harness/verticals/retail/web/control-room.js#L253) | id |  |
| [load](../harness/verticals/retail/web/control-room.js#L273) |  |  |
| [goHome](../harness/verticals/retail/web/control-room.js#L294) |  |  |
| [handle](../harness/verticals/retail/web/control-room.js#L300) | event |  |

### harness/verticals/retail/web/control-room/app.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [mappedTime](../harness/verticals/retail/web/control-room/app.js#L23) | time=decodedFrameTime |  |
| [geometryPerson](../harness/verticals/retail/web/control-room/app.js#L24) | track, time=decodedFrameTime |  |
| [maintainedChapters](../harness/verticals/retail/web/control-room/app.js#L25) |  |  |
| [maintainedEvents](../harness/verticals/retail/web/control-room/app.js#L26) |  |  |
| [continueSession](../harness/verticals/retail/web/control-room/app.js#L31) |  |  |
| [paintAmbient](../harness/verticals/retail/web/control-room/app.js#L44) |  |  |
| [sampleFrame](../harness/verticals/retail/web/control-room/app.js#L45) |  |  |
| [boxCrop](../harness/verticals/retail/web/control-room/app.js#L50) | box, tr |  |
| [capturePortrait](../harness/verticals/retail/web/control-room/app.js#L56) | identity, box, tr |  |
| [captureEventCrops](../harness/verticals/retail/web/control-room/app.js#L62) | t, tracks, tr |  |
| [heldRead](../harness/verticals/retail/web/control-room/app.js#L70) |  |  |
| [releasePicture](../harness/verticals/retail/web/control-room/app.js#L71) |  |  |
| [restorePicture](../harness/verticals/retail/web/control-room/app.js#L84) |  |  |
| [navigateChapter](../harness/verticals/retail/web/control-room/app.js#L85) | chapter |  |
| [navigateVisitor](../harness/verticals/retail/web/control-room/app.js#L86) | id |  |
| [noteActionCues](../harness/verticals/retail/web/control-room/app.js#L92) |  |  |
| [receiveMaintained](../harness/verticals/retail/web/control-room/app.js#L101) | state |  |
| [updateVisitBasket](../harness/verticals/retail/web/control-room/app.js#L107) | time |  |
| [playerWorkSuspended](../harness/verticals/retail/web/control-room/app.js#L115) |  |  |
| [allEvents](../harness/verticals/retail/web/control-room/app.js#L116) |  |  |
| [objectFrameTime](../harness/verticals/retail/web/control-room/app.js#L117) | e |  |
| [objectBox](../harness/verticals/retail/web/control-room/app.js#L118) | e |  |
| [markFramePending](../harness/verticals/retail/web/control-room/app.js#L119) |  |  |
| [acceptDecodedFrame](../harness/verticals/retail/web/control-room/app.js#L120) | time |  |
| [requestDecodedFrame](../harness/verticals/retail/web/control-room/app.js#L121) |  |  |
| [clearMedia](../harness/verticals/retail/web/control-room/app.js#L126) |  |  |
| [loadClipMedia](../harness/verticals/retail/web/control-room/app.js#L127) | clip |  |
| [sizeTrackOverlay](../harness/verticals/retail/web/control-room/app.js#L144) | width, height |  |
| [seek](../harness/verticals/retail/web/control-room/app.js#L146) | t, play=false, liveSeek=false |  |
| [indexTracks](../harness/verticals/retail/web/control-room/app.js#L147) | tr |  |
| [loadClipTracks](../harness/verticals/retail/web/control-room/app.js#L150) | clip |  |
| [setClip](../harness/verticals/retail/web/control-room/app.js#L159) | id, fromGrid=false, liveTransition=false |  |
| [renderGrid](../harness/verticals/retail/web/control-room/app.js#L174) |  |  |
| [tracksAt](../harness/verticals/retail/web/control-room/app.js#L179) | t |  |
| [smoothTrailPath](../harness/verticals/retail/web/control-room/app.js#L186) | points |  |
| [trailShapes](../harness/verticals/retail/web/control-room/app.js#L191) | tr, t |  |
| [objectShapes](../harness/verticals/retail/web/control-room/app.js#L209) | t, tr |  |
| [updateOverlay](../harness/verticals/retail/web/control-room/app.js#L217) | frameTime |  |
| [personTitle](../harness/verticals/retail/web/control-room/app.js#L237) | id |  |
| [selectPerson](../harness/verticals/retail/web/control-room/app.js#L238) | id |  |
| [enterRoomMode](../harness/verticals/retail/web/control-room/app.js#L243) |  |  |
| [cyclePerson](../harness/verticals/retail/web/control-room/app.js#L248) | direction |  |
| [videoPoint](../harness/verticals/retail/web/control-room/app.js#L254) | event |  |
| [choosePersonAtPointer](../harness/verticals/retail/web/control-room/app.js#L258) | event |  |
| [eventAnchor](../harness/verticals/retail/web/control-room/app.js#L264) | e |  |
| [clearTrailPreview](../harness/verticals/retail/web/control-room/app.js#L265) |  |  |
| [setTrailPreview](../harness/verticals/retail/web/control-room/app.js#L266) | key, source |  |
| [eventImage](../harness/verticals/retail/web/control-room/app.js#L270) | e |  |
| [renderContextualActivity](../harness/verticals/retail/web/control-room/app.js#L271) | t |  |
| [renderTrailAnnotations](../harness/verticals/retail/web/control-room/app.js#L282) | t |  |
| [activateTrailEvent](../harness/verticals/retail/web/control-room/app.js#L306) | node |  |
| [queueIntervals](../harness/verticals/retail/web/control-room/app.js#L310) | events, id=null |  |
| [stillnessIntervals](../harness/verticals/retail/web/control-room/app.js#L318) | id |  |
| [genericObservation](../harness/verticals/retail/web/control-room/app.js#L325) | e |  |
| [selectedEvents](../harness/verticals/retail/web/control-room/app.js#L326) |  |  |
| [displayEventLabel](../harness/verticals/retail/web/control-room/app.js#L327) | e |  |
| [eventTitle](../harness/verticals/retail/web/control-room/app.js#L328) | e |  |
| [eventDescription](../harness/verticals/retail/web/control-room/app.js#L329) | e |  |
| [sessionClip](../harness/verticals/retail/web/control-room/app.js#L330) | point |  |
| [personChapters](../harness/verticals/retail/web/control-room/app.js#L331) |  |  |
| [thumbnailMarkup](../harness/verticals/retail/web/control-room/app.js#L344) | at, extra='' |  |
| [visitorRecords](../harness/verticals/retail/web/control-room/app.js#L348) |  |  |
| [renderVisitorList](../harness/verticals/retail/web/control-room/app.js#L357) |  |  |
| [refreshVisitorHistory](../harness/verticals/retail/web/control-room/app.js#L369) |  |  |
| [observedItemGroups](../harness/verticals/retail/web/control-room/app.js#L375) | events |  |
| [renderPersonSummary](../harness/verticals/retail/web/control-room/app.js#L385) | rows |  |
| [renderJourney](../harness/verticals/retail/web/control-room/app.js#L398) |  |  |
| [updateJourneyActive](../harness/verticals/retail/web/control-room/app.js#L415) | active |  |
| [selectEvent](../harness/verticals/retail/web/control-room/app.js#L420) | e |  |
| [showEvidence](../harness/verticals/retail/web/control-room/app.js#L425) | e, origin='auto' |  |
| [updateAutomaticEvidence](../harness/verticals/retail/web/control-room/app.js#L431) | t |  |
| [expandEvidence](../harness/verticals/retail/web/control-room/app.js#L436) | crop=false |  |
| [updateLiveReplayStatus](../harness/verticals/retail/web/control-room/app.js#L448) |  |  |
| [leaveLiveReplay](../harness/verticals/retail/web/control-room/app.js#L455) |  |  |
| [initializeRoomReplay](../harness/verticals/retail/web/control-room/app.js#L456) | roomId=$('#roomSelect' |  |
| [returnToLiveReplay](../harness/verticals/retail/web/control-room/app.js#L465) |  |  |
| [syncLiveReplay](../harness/verticals/retail/web/control-room/app.js#L466) | force=false |  |
| [requestOverlayFrame](../harness/verticals/retail/web/control-room/app.js#L494) |  |  |
| [cancelOverlayFrame](../harness/verticals/retail/web/control-room/app.js#L499) |  |  |
| [syncExpandedPlayer](../harness/verticals/retail/web/control-room/app.js#L512) |  |  |
| [loadPlayer](../harness/verticals/retail/web/control-room/app.js#L516) |  |  |
| [icon](../harness/verticals/retail/web/control-room/app.js#L533) | name |  |
| [motionGroups](../harness/verticals/retail/web/control-room/app.js#L549) | tr, t |  |
| [renderDurationTimeline](../harness/verticals/retail/web/control-room/app.js#L557) |  |  |
| [updatePlayerUI](../harness/verticals/retail/web/control-room/app.js#L566) | t |  |
| [previewSeek](../harness/verticals/retail/web/control-room/app.js#L573) | t, x |  |
| [resumePlayback](../harness/verticals/retail/web/control-room/app.js#L578) |  |  |
| [togglePlay](../harness/verticals/retail/web/control-room/app.js#L579) |  |  |
| [flash](../harness/verticals/retail/web/control-room/app.js#L580) | message |  |
| [revealControls](../harness/verticals/retail/web/control-room/app.js#L582) |  |  |
| [initWatchUI](../harness/verticals/retail/web/control-room/app.js#L583) |  |  |

### harness/verticals/retail/web/control-room/control-room.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [refreshData](../harness/verticals/retail/web/control-room/control-room.js#L6) |  |  |
| [loadNext](../harness/verticals/retail/web/control-room/control-room.js#L12) |  |  |
| [placeWeather](../harness/verticals/retail/web/control-room/control-room.js#L24) | home |  |
| [showOverview](../harness/verticals/retail/web/control-room/control-room.js#L25) |  |  |
| [showCameras](../harness/verticals/retail/web/control-room/control-room.js#L26) |  |  |
| [closeSession](../harness/verticals/retail/web/control-room/control-room.js#L29) |  |  |
| [openSession](../harness/verticals/retail/web/control-room/control-room.js#L30) | target |  |
| [nameBack](../harness/verticals/retail/web/control-room/control-room.js#L37) | name |  |
| [applySnapshot](../harness/verticals/retail/web/control-room/control-room.js#L38) | snapshot |  |
| [askRevision](../harness/verticals/retail/web/control-room/control-room.js#L59) |  |  |
| [trackerState](../harness/verticals/retail/web/control-room/control-room.js#L66) | schedule, run |  |
| [showTrackers](../harness/verticals/retail/web/control-room/control-room.js#L74) | next |  |
| [refreshPage](../harness/verticals/retail/web/control-room/control-room.js#L84) |  |  |
| [checkRevision](../harness/verticals/retail/web/control-room/control-room.js#L95) |  |  |
| [init](../harness/verticals/retail/web/control-room/control-room.js#L112) |  |  |

### harness/verticals/retail/web/control-room/home-history.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [kindOf](../harness/verticals/retail/web/control-room/home-history.js#L66) | tile |  |
| [span](../harness/verticals/retail/web/control-room/home-history.js#L76) | seconds |  |
| [parts](../harness/verticals/retail/web/control-room/home-history.js#L85) | value, unit |  |
| [seriesText](../harness/verticals/retail/web/control-room/home-history.js#L97) | tile, value |  |
| [moment](../harness/verticals/retail/web/control-room/home-history.js#L105) | at, model, withDay |  |
| [day](../harness/verticals/retail/web/control-room/home-history.js#L115) | at, model |  |
| [waitsOf](../harness/verticals/retail/web/control-room/home-history.js#L127) | tile |  |
| [distributionOf](../harness/verticals/retail/web/control-room/home-history.js#L139) | tile |  |
| [shelvesOf](../harness/verticals/retail/web/control-room/home-history.js#L147) | tile |  |
| [moneyText](../harness/verticals/retail/web/control-room/home-history.js#L167) | amount, currency, model |  |
| [canvasShelf](../harness/verticals/retail/web/control-room/home-history.js#L175) | shelf |  |
| [resolve](../harness/verticals/retail/web/control-room/home-history.js#L185) | tile |  |
| [connectCopy](../harness/verticals/retail/web/control-room/home-history.js#L223) | tile, model |  |
| [send](../harness/verticals/retail/web/control-room/home-history.js#L235) | type, detail, cancelable=false |  |
| [openSession](../harness/verticals/retail/web/control-room/home-history.js#L241) | entry |  |
| [openAgent](../harness/verticals/retail/web/control-room/home-history.js#L251) |  |  |
| [thumb](../harness/verticals/retail/web/control-room/home-history.js#L262) | entry, list, index, model |  |
| [row](../harness/verticals/retail/web/control-room/home-history.js#L267) | entry, list, index, model, middle, lead, attributes='' |  |
| [eventRows](../harness/verticals/retail/web/control-room/home-history.js#L271) | events, tile, model |  |
| [shelfRows](../harness/verticals/retail/web/control-room/home-history.js#L281) | shelves, model |  |
| [groupRows](../harness/verticals/retail/web/control-room/home-history.js#L295) | groups, tile, model |  |
| [figures](../harness/verticals/retail/web/control-room/home-history.js#L309) | tile |  |
| [periodToggle](../harness/verticals/retail/web/control-room/home-history.js#L315) | tile, model |  |
| [compose](../harness/verticals/retail/web/control-room/home-history.js#L322) | tile, model |  |
| [stopPreviews](../harness/verticals/retail/web/control-room/home-history.js#L343) |  |  |
| [preview](../harness/verticals/retail/web/control-room/home-history.js#L346) | rowNode, on |  |
| [render](../harness/verticals/retail/web/control-room/home-history.js#L367) | change |  |
| [choosePeriod](../harness/verticals/retail/web/control-room/home-history.js#L390) | period, focus |  |
| [build](../harness/verticals/retail/web/control-room/home-history.js#L398) | surface |  |
| [morph](../harness/verticals/retail/web/control-room/home-history.js#L432) | dialog, element, opening |  |
| [open](../harness/verticals/retail/web/control-room/home-history.js#L461) | tile, model, element, opts |  |
| [finish](../harness/verticals/retail/web/control-room/home-history.js#L477) | restore |  |
| [close](../harness/verticals/retail/web/control-room/home-history.js#L488) |  |  |
| [update](../harness/verticals/retail/web/control-room/home-history.js#L495) | tile |  |

### harness/verticals/retail/web/control-room/home-marks.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [monotone](../harness/verticals/retail/web/control-room/home-marks.js#L11) | points |  |
| [clear](../harness/verticals/retail/web/control-room/home-marks.js#L27) | el, kind, opts |  |
| [line](../harness/verticals/retail/web/control-room/home-marks.js#L29) | el, points, opts={} |  |
| [ring](../harness/verticals/retail/web/control-room/home-marks.js#L45) | el, fraction, opts={} |  |
| [bars](../harness/verticals/retail/web/control-room/home-marks.js#L53) | el, values, opts={} |  |

### harness/verticals/retail/web/control-room/home-model.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [isoTime](../harness/verticals/retail/web/control-room/home-model.js#L41) | value |  |
| [eventRow](../harness/verticals/retail/web/control-room/home-model.js#L47) | e, index |  |
| [visitorRow](../harness/verticals/retail/web/control-room/home-model.js#L54) | v, index |  |
| [format](../harness/verticals/retail/web/control-room/home-model.js#L60) | kind, value, currency |  |
| [seriesRows](../harness/verticals/retail/web/control-room/home-model.js#L73) | rows |  |
| [bucketed](../harness/verticals/retail/web/control-room/home-model.js#L80) | events, period, now, measure |  |
| [queueWait](../harness/verticals/retail/web/control-room/home-model.js#L95) | events |  |
| [suppliedTile](../harness/verticals/retail/web/control-room/home-model.js#L109) | row, period, index, currency |  |
| [from](../harness/verticals/retail/web/control-room/home-model.js#L124) | input, options |  |

### harness/verticals/retail/web/control-room/journey-model.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [configure](../harness/verticals/retail/web/control-room/journey-model.js#L28) | profile |  |
| [clean](../harness/verticals/retail/web/control-room/journey-model.js#L36) | value |  |
| [canonicalActionTitle](../harness/verticals/retail/web/control-room/journey-model.js#L37) | event |  |
| [eventDescription](../harness/verticals/retail/web/control-room/journey-model.js#L48) | event |  |
| [personKey](../harness/verticals/retail/web/control-room/journey-model.js#L59) | recordingId, personId |  |
| [stableEventId](../harness/verticals/retail/web/control-room/journey-model.js#L62) | recordingId, windowIndex, eventIndex, event |  |
| [eventAnchorFromTracks](../harness/verticals/retail/web/control-room/journey-model.js#L66) | tr, personId, time_s |  |
| [activityAt](../harness/verticals/retail/web/control-room/journey-model.js#L81) | events, personId, time_s |  |
| [isProductInteraction](../harness/verticals/retail/web/control-room/journey-model.js#L103) | event |  |
| [majorInteractionAt](../harness/verticals/retail/web/control-room/journey-model.js#L104) | events, personId, time_s |  |

### harness/verticals/retail/web/control-room/location-data.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [isFixtureTarget](../harness/verticals/retail/web/control-room/location-data.js#L9) | event |  |
| [displayDescription](../harness/verticals/retail/web/control-room/location-data.js#L14) | value |  |
| [captureDate](../harness/verticals/retail/web/control-room/location-data.js#L24) | clip |  |
| [imageOf](../harness/verticals/retail/web/control-room/location-data.js#L25) | e |  |
| [metricSource](../harness/verticals/retail/web/control-room/location-data.js#L26) | value, needed |  |
| [build](../harness/verticals/retail/web/control-room/location-data.js#L27) | {clips=[], tracks={}, locationMetrics=null, model='8b', eventTypes=null, page=null}={} |  |
| [session](../harness/verticals/retail/web/control-room/location-data.js#L39) | personId |  |

### harness/verticals/retail/web/control-room/location-view.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [create](../harness/verticals/retail/web/control-room/location-view.js#L18) | options |  |
| [listen](../harness/verticals/retail/web/control-room/location-view.js#L59) | element, type, handler, opts |  |
| [renderPlace](../harness/verticals/retail/web/control-room/location-view.js#L62) |  |  |
| [renderFootage](../harness/verticals/retail/web/control-room/location-view.js#L75) |  |  |
| [release](../harness/verticals/retail/web/control-room/location-view.js#L84) |  |  |
| [play](../harness/verticals/retail/web/control-room/location-view.js#L86) |  |  |
| [rest](../harness/verticals/retail/web/control-room/location-view.js#L87) |  |  |
| [nextRecording](../harness/verticals/retail/web/control-room/location-view.js#L88) |  |  |
| [traceOf](../harness/verticals/retail/web/control-room/location-view.js#L91) | recording |  |
| [clearTags](../harness/verticals/retail/web/control-room/location-view.js#L97) |  |  |
| [drawTags](../harness/verticals/retail/web/control-room/location-view.js#L99) |  |  |
| [tagLoop](../harness/verticals/retail/web/control-room/location-view.js#L120) |  |  |
| [drawMark](../harness/verticals/retail/web/control-room/location-view.js#L126) | node, tile |  |
| [tileNode](../harness/verticals/retail/web/control-room/location-view.js#L146) | tile |  |
| [paintTile](../harness/verticals/retail/web/control-room/location-view.js#L152) | node, tile, fresh |  |
| [fitUnit](../harness/verticals/retail/web/control-room/location-view.js#L171) | node, tile |  |
| [tick](../harness/verticals/retail/web/control-room/location-view.js#L178) | node |  |
| [renderTiles](../harness/verticals/retail/web/control-room/location-view.js#L182) |  |  |
| [stampOf](../harness/verticals/retail/web/control-room/location-view.js#L210) | tile |  |
| [newTracker](../harness/verticals/retail/web/control-room/location-view.js#L211) |  |  |
| [open](../harness/verticals/retail/web/control-room/location-view.js#L216) | key, node |  |
| [openTile](../harness/verticals/retail/web/control-room/location-view.js#L236) | tile |  |
| [renderProducts](../harness/verticals/retail/web/control-room/location-view.js#L247) |  |  |
| [stopPreviews](../harness/verticals/retail/web/control-room/location-view.js#L257) |  |  |
| [clearPreviews](../harness/verticals/retail/web/control-room/location-view.js#L258) |  |  |
| [bindPreview](../harness/verticals/retail/web/control-room/location-view.js#L261) | row, video, event, start, end |  |
| [openProduct](../harness/verticals/retail/web/control-room/location-view.js#L302) | product |  |
| [renderNeighbourhood](../harness/verticals/retail/web/control-room/location-view.js#L315) |  |  |
| [catalogLocationParams](../harness/verticals/retail/web/control-room/location-view.js#L325) |  |  |
| [catalogMethodButton](../harness/verticals/retail/web/control-room/location-view.js#L326) | method |  |
| [openCatalogSetup](../harness/verticals/retail/web/control-room/location-view.js#L327) |  |  |
| [requestCatalogMethod](../harness/verticals/retail/web/control-room/location-view.js#L332) | method, setup |  |
| [renderCatalogImport](../harness/verticals/retail/web/control-room/location-view.js#L338) |  |  |
| [createPhotoHandoff](../harness/verticals/retail/web/control-room/location-view.js#L341) |  |  |
| [loadAgents](../harness/verticals/retail/web/control-room/location-view.js#L346) |  |  |
| [render](../harness/verticals/retail/web/control-room/location-view.js#L354) |  |  |

### harness/verticals/retail/web/control-room/maintained-player.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [windowRange](../harness/verticals/retail/web/control-room/maintained-player.js#L10) | value |  |
| [mapping](../harness/verticals/retail/web/control-room/maintained-player.js#L11) | clip |  |
| [streamTime](../harness/verticals/retail/web/control-room/maintained-player.js#L12) | clip, localTime |  |
| [localTime](../harness/verticals/retail/web/control-room/maintained-player.js#L13) | clip, time |  |
| [safeUrl](../harness/verticals/retail/web/control-room/maintained-player.js#L14) | value, base=root.location?.href |  |
| [point](../harness/verticals/retail/web/control-room/maintained-player.js#L18) | value |  |
| [place](../harness/verticals/retail/web/control-room/maintained-player.js#L19) | value |  |
| [bootstrap](../harness/verticals/retail/web/control-room/maintained-player.js#L25) | value, base=root.location?.href |  |
| [session](../harness/verticals/retail/web/control-room/maintained-player.js#L44) | clips, clip |  |
| [following](../harness/verticals/retail/web/control-room/maintained-player.js#L46) | clips, clip |  |
| [validate](../harness/verticals/retail/web/control-room/maintained-player.js#L47) | value, requested |  |
| [create](../harness/verticals/retail/web/control-room/maintained-player.js#L56) | {fetcher=(...args |  |
| [refill](../harness/verticals/retail/web/control-room/maintained-player.js#L61) |  |  |
| [notify](../harness/verticals/retail/web/control-room/maintained-player.js#L62) |  |  |
| [cancel](../harness/verticals/retail/web/control-room/maintained-player.js#L63) |  |  |
| [clear](../harness/verticals/retail/web/control-room/maintained-player.js#L64) | nextStatus='idle' |  |
| [schedule](../harness/verticals/retail/web/control-room/maintained-player.js#L65) | delay |  |
| [pump](../harness/verticals/retail/web/control-room/maintained-player.js#L66) |  |  |
| [update](../harness/verticals/retail/web/control-room/maintained-player.js#L82) | next |  |
| [suspend](../harness/verticals/retail/web/control-room/maintained-player.js#L90) | flag |  |
| [invalidate](../harness/verticals/retail/web/control-room/maintained-player.js#L91) |  |  |
| [destroy](../harness/verticals/retail/web/control-room/maintained-player.js#L92) |  |  |
| [visitors](../harness/verticals/retail/web/control-room/maintained-player.js#L95) | value |  |
| [visit](../harness/verticals/retail/web/control-room/maintained-player.js#L103) | value, visitId |  |
| [trackerVisit](../harness/verticals/retail/web/control-room/maintained-player.js#L104) | value, clip, track, at |  |
| [chapters](../harness/verticals/retail/web/control-room/maintained-player.js#L113) | value, visitId, clips |  |

### harness/verticals/retail/web/control-room/motion-timeline.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [profile](../harness/verticals/retail/web/control-room/motion-timeline.js#L4) | track, personId |  |
| [paths](../harness/verticals/retail/web/control-room/motion-timeline.js#L21) | groups, duration, width=1000, height=42 |  |
| [at](../harness/verticals/retail/web/control-room/motion-timeline.js#L32) | groups, time |  |

### harness/verticals/retail/web/control-room/person-outline-worker.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [edgeTexture](../harness/verticals/retail/web/control-room/person-outline-worker.js#L7) | values, size, rect |  |

### harness/verticals/retail/web/control-room/person-outline.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [finite](../harness/verticals/retail/web/control-room/person-outline.js#L24) | value, fallback |  |
| [normalizeBox](../harness/verticals/retail/web/control-room/person-outline.js#L28) | value |  |
| [area](../harness/verticals/retail/web/control-room/person-outline.js#L42) | box |  |
| [intersection](../harness/verticals/retail/web/control-room/person-outline.js#L46) | a, b |  |
| [create](../harness/verticals/retail/web/control-room/person-outline.js#L52) | options |  |
| [clear](../harness/verticals/retail/web/control-room/person-outline.js#L77) |  |  |
| [notify](../harness/verticals/retail/web/control-room/person-outline.js#L86) |  |  |
| [fail](../harness/verticals/retail/web/control-room/person-outline.js#L90) |  |  |
| [ensureCanvas](../harness/verticals/retail/web/control-room/person-outline.js#L97) | width, height |  |
| [buildEdgeTexture](../harness/verticals/retail/web/control-room/person-outline.js#L103) | message |  |
| [drawMask](../harness/verticals/retail/web/control-room/person-outline.js#L112) | mask, box, width, height |  |
| [significantOverlap](../harness/verticals/retail/web/control-room/person-outline.js#L128) | box, others |  |
| [acceptMask](../harness/verticals/retail/web/control-room/person-outline.js#L136) | message |  |
| [onWorkerMessage](../harness/verticals/retail/web/control-room/person-outline.js#L156) | event |  |
| [startWorker](../harness/verticals/retail/web/control-room/person-outline.js#L165) |  |  |
| [flushQueued](../harness/verticals/retail/web/control-room/person-outline.js#L181) |  |  |
| [submit](../harness/verticals/retail/web/control-room/person-outline.js#L188) | box, sourceWidth, sourceHeight, personId, time |  |
| [update](../harness/verticals/retail/web/control-room/person-outline.js#L219) | frame |  |
| [status](../harness/verticals/retail/web/control-room/person-outline.js#L245) |  |  |
| [stopEngine](../harness/verticals/retail/web/control-room/person-outline.js#L248) | nextState |  |
| [startEngine](../harness/verticals/retail/web/control-room/person-outline.js#L253) |  |  |
| [setSuspended](../harness/verticals/retail/web/control-room/person-outline.js#L254) | value |  |
| [setEnabled](../harness/verticals/retail/web/control-room/person-outline.js#L260) | value |  |
| [onVisibility](../harness/verticals/retail/web/control-room/person-outline.js#L265) |  |  |
| [destroy](../harness/verticals/retail/web/control-room/person-outline.js#L269) |  |  |

### harness/verticals/retail/web/control-room/player-lifecycle.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [create](../harness/verticals/retail/web/control-room/player-lifecycle.js#L4) | options |  |
| [hide](../harness/verticals/retail/web/control-room/player-lifecycle.js#L7) |  |  |
| [show](../harness/verticals/retail/web/control-room/player-lifecycle.js#L13) |  |  |
| [visibility](../harness/verticals/retail/web/control-room/player-lifecycle.js#L21) |  |  |
| [play](../harness/verticals/retail/web/control-room/player-lifecycle.js#L22) |  |  |

### harness/verticals/retail/web/control-room/room-loop.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [create](../harness/verticals/retail/web/control-room/room-loop.js#L4) | recordings, now=( |  |
| [positionAt](../harness/verticals/retail/web/control-room/room-loop.js#L8) | elapsed_s |  |

### harness/verticals/retail/web/control-room/visit-basket.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [create](../harness/verticals/retail/web/control-room/visit-basket.js#L6) | {host, fetcher=(...args |  |
| [clear](../harness/verticals/retail/web/control-room/visit-basket.js#L8) |  |  |
| [image](../harness/verticals/retail/web/control-room/visit-basket.js#L9) | url |  |
| [row](../harness/verticals/retail/web/control-room/visit-basket.js#L10) | item, uncertain=false |  |
| [render](../harness/verticals/retail/web/control-room/visit-basket.js#L15) | value |  |
| [showSnapshot](../harness/verticals/retail/web/control-room/visit-basket.js#L24) | next |  |
| [within](../harness/verticals/retail/web/control-room/visit-basket.js#L31) | value, time |  |
| [update](../harness/verticals/retail/web/control-room/visit-basket.js#L32) | next |  |
| [invalidate](../harness/verticals/retail/web/control-room/visit-basket.js#L57) |  |  |
| [destroy](../harness/verticals/retail/web/control-room/visit-basket.js#L59) |  |  |

### harness/verticals/retail/web/control-room/weather-widget.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [cityOf](../harness/verticals/retail/web/control-room/weather-widget.js#L50) | address, zone |  |
| [monotone](../harness/verticals/retail/web/control-room/weather-widget.js#L57) | points |  |
| [layout](../harness/verticals/retail/web/control-room/weather-widget.js#L78) | values, {width, height, top, bottom, left, right} |  |
| [lineMark](../harness/verticals/retail/web/control-room/weather-widget.js#L85) | values, box, {dots=false}={} |  |
| [ghostMark](../harness/verticals/retail/web/control-room/weather-widget.js#L93) | box, stretch |  |
| [create](../harness/verticals/retail/web/control-room/weather-widget.js#L102) | {host, onLocation, place:configured, enabled=true}={} |  |
| [drawChip](../harness/verticals/retail/web/control-room/weather-widget.js#L116) |  |  |
| [daily](../harness/verticals/retail/web/control-room/weather-widget.js#L138) | today |  |
| [figure](../harness/verticals/retail/web/control-room/weather-widget.js#L144) | now, full |  |
| [drawPreview](../harness/verticals/retail/web/control-room/weather-widget.js#L148) |  |  |
| [hidePreview](../harness/verticals/retail/web/control-room/weather-widget.js#L160) |  |  |
| [showPreview](../harness/verticals/retail/web/control-room/weather-widget.js#L161) |  |  |
| [hoursHtml](../harness/verticals/retail/web/control-room/weather-widget.js#L166) |  |  |
| [daysHtml](../harness/verticals/retail/web/control-room/weather-widget.js#L177) |  |  |
| [drawSheet](../harness/verticals/retail/web/control-room/weather-widget.js#L184) | force |  |
| [buildSheet](../harness/verticals/retail/web/control-room/weather-widget.js#L222) |  |  |
| [open](../harness/verticals/retail/web/control-room/weather-widget.js#L230) |  |  |
| [close](../harness/verticals/retail/web/control-room/weather-widget.js#L244) |  |  |
| [draw](../harness/verticals/retail/web/control-room/weather-widget.js#L253) |  |  |
| [refresh](../harness/verticals/retail/web/control-room/weather-widget.js#L254) | visible |  |
| [mountMap](../harness/verticals/retail/web/control-room/weather-widget.js#L271) |  |  |
| [map](../harness/verticals/retail/web/control-room/weather-widget.js#L306) | el, opts={} |  |

### harness/verticals/retail/web/retail-scope.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [render](../harness/verticals/retail/web/retail-scope.js#L9) | { data = null, loading = false, error = '', onSave, onRetry } = {}, { node = make } = {} |  |
| [draw](../harness/verticals/retail/web/retail-scope.js#L14) |  |  |
| [edit](../harness/verticals/retail/web/retail-scope.js#L60) | kind, original, opener |  |
| [input](../harness/verticals/retail/web/retail-scope.js#L66) | name, label, initial, required = false |  |
| [select](../harness/verticals/retail/web/retail-scope.js#L69) | name, label, rows, initial |  |
| [checks](../harness/verticals/retail/web/retail-scope.js#L74) | name, label, rows, selected, emptyText |  |
| [refresh](../harness/verticals/retail/web/retail-scope.js#L77) | nextRows |  |
| [renderSelector](../harness/verticals/retail/web/retail-scope.js#L124) | { data = null, locations = [], loading = false, error = '', busy = false, readOnly = false, onSave, onOpen, onRetry } = {}, { node = make } = {} |  |
| [isAll](../harness/verticals/retail/web/retail-scope.js#L131) |  |  |
| [label](../harness/verticals/retail/web/retail-scope.js#L132) |  |  |
| [drawChoices](../harness/verticals/retail/web/retail-scope.js#L136) |  |  |
| [position](../harness/verticals/retail/web/retail-scope.js#L145) |  |  |
| [stopWatching](../harness/verticals/retail/web/retail-scope.js#L148) |  |  |

### harness/verticals/retail/web/retail-shell.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [mountLocation](../harness/verticals/retail/web/retail-shell.js#L7) | slot, config |  |

### harness/verticals/retail/web/retail-ui.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [storageCurrent](../harness/verticals/retail/web/retail-ui.js#L7) | item, generation, detail |  |
| [resetStorageSetup](../harness/verticals/retail/web/retail-ui.js#L8) |  |  |
| [storageError](../harness/verticals/retail/web/retail-ui.js#L9) | error |  |
| [storageDate](../harness/verticals/retail/web/retail-ui.js#L11) | value |  |
| [storageStatus](../harness/verticals/retail/web/retail-ui.js#L12) | setup |  |
| [refreshStorageSetup](../harness/verticals/retail/web/retail-ui.js#L13) | item |  |
| [replaceStorageSetup](../harness/verticals/retail/web/retail-ui.js#L35) | item |  |
| [storageAction](../harness/verticals/retail/web/retail-ui.js#L41) | item, action, body |  |
| [reviewStorageFolder](../harness/verticals/retail/web/retail-ui.js#L61) | item, opener |  |
| [renderStorageSetup](../harness/verticals/retail/web/retail-ui.js#L79) | content, item |  |
| [renderImportProgress](../harness/verticals/retail/web/retail-ui.js#L106) | section, item, acquisition |  |
| [resetBusinessScopes](../harness/verticals/retail/web/retail-ui.js#L121) |  |  |
| [businessScopeKey](../harness/verticals/retail/web/retail-ui.js#L122) | collection |  |
| [businessScopeEntry](../harness/verticals/retail/web/retail-ui.js#L123) | collection |  |
| [scopeJSON](../harness/verticals/retail/web/retail-ui.js#L124) | response |  |
| [readBusinessScope](../harness/verticals/retail/web/retail-ui.js#L128) | collection, force = false |  |
| [loadBusinessScope](../harness/verticals/retail/web/retail-ui.js#L144) | collection = host.businessCollection |  |
| [businessScopeSurface](../harness/verticals/retail/web/retail-ui.js#L147) | collection |  |
| [chatLocationKey](../harness/verticals/retail/web/retail-ui.js#L159) | chat |  |
| [readChatLocations](../harness/verticals/retail/web/retail-ui.js#L160) | chat, force = false |  |
| [renderChatLocations](../harness/verticals/retail/web/retail-ui.js#L178) |  |  |
| [sourceCollections](../harness/verticals/retail/web/retail-ui.js#L200) | status |  |
| [preciseTime](../harness/verticals/retail/web/retail-ui.js#L206) | value |  |
| [toolFramePreviews](../harness/verticals/retail/web/retail-ui.js#L207) | tool |  |
| [saveClipDrafts](../harness/verticals/retail/web/retail-ui.js#L208) |  |  |
| [openCameraProviderPicker](../harness/verticals/retail/web/retail-ui.js#L295) | opener, collection = '' |  |
| [openConnectionEditor](../harness/verticals/retail/web/retail-ui.js#L303) | event |  |
| [startCameraSetup](../harness/verticals/retail/web/retail-ui.js#L305) | provider = null |  |
| [agentUsesCameraInput](../harness/verticals/retail/web/retail-ui.js#L311) | agent |  |
| [showCameras](../harness/verticals/retail/web/retail-ui.js#L313) | collection = null, id = '' |  |
| [reviewCameras](../harness/verticals/retail/web/retail-ui.js#L318) | ids |  |
| [chooseCameraReview](../harness/verticals/retail/web/retail-ui.js#L320) |  |  |
| [setCameraTab](../harness/verticals/retail/web/retail-ui.js#L322) | value |  |
| [loadCameraStreams](../harness/verticals/retail/web/retail-ui.js#L324) |  |  |
| [cameraSetup](../harness/verticals/retail/web/retail-ui.js#L331) | connection, opener |  |
| [recordingReferences](../harness/verticals/retail/web/retail-ui.js#L333) |  |  |
| [loadCameras](../harness/verticals/retail/web/retail-ui.js#L335) |  |  |
| [renderCameras](../harness/verticals/retail/web/retail-ui.js#L344) |  |  |
| [contextCard](../harness/verticals/retail/web/retail-ui.js#L361) | saved, draft = false |  |
| [field](../harness/verticals/retail/web/retail-ui.js#L367) | label, key, tag = 'input', value = '' |  |
| [clipDownloadUrl](../harness/verticals/retail/web/retail-ui.js#L407) | result |  |
| [clipManifestUrl](../harness/verticals/retail/web/retail-ui.js#L409) | result |  |
| [findEvidence](../harness/verticals/retail/web/retail-ui.js#L411) | id |  |
| [evidenceOpenScope](../harness/verticals/retail/web/retail-ui.js#L413) |  |  |
| [cancelEvidenceOpen](../harness/verticals/retail/web/retail-ui.js#L415) |  |  |
| [openEvidenceId](../harness/verticals/retail/web/retail-ui.js#L417) | id, opener, context = null |  |
| [mediaReferenceResult](../harness/verticals/retail/web/retail-ui.js#L426) | url |  |
| [messageMediaDependencies](../harness/verticals/retail/web/retail-ui.js#L432) | message |  |
| [evidencePresentation](../harness/verticals/retail/web/retail-ui.js#L441) | value |  |
| [inlineEvidence](../harness/verticals/retail/web/retail-ui.js#L447) | result, results, index, message |  |
| [evidenceCard](../harness/verticals/retail/web/retail-ui.js#L456) | result, results, index, message |  |
| [stopPreview](../harness/verticals/retail/web/retail-ui.js#L466) |  |  |
| [renderClipMetadata](../harness/verticals/retail/web/retail-ui.js#L476) | data, result |  |
| [prioritizedEvidence](../harness/verticals/retail/web/retail-ui.js#L503) | message |  |
| [openGallery](../harness/verticals/retail/web/retail-ui.js#L505) | message, opener |  |
| [openClip](../harness/verticals/retail/web/retail-ui.js#L507) | results, index, message, opener |  |
| [readDescriptions](../harness/verticals/retail/web/retail-ui.js#L523) |  |  |
| [renderObservations](../harness/verticals/retail/web/retail-ui.js#L539) | descriptions |  |
| [observation](../harness/verticals/retail/web/retail-ui.js#L546) | item, primary = false |  |
| [questionGroup](../harness/verticals/retail/web/retail-ui.js#L554) | group |  |
| [focusBox](../harness/verticals/retail/web/retail-ui.js#L558) | at |  |
| [drawFocus](../harness/verticals/retail/web/retail-ui.js#L566) |  |  |
| [animateFocus](../harness/verticals/retail/web/retail-ui.js#L579) |  |  |
| [setFocus](../harness/verticals/retail/web/retail-ui.js#L581) | enabled |  |
| [renderInterpretation](../harness/verticals/retail/web/retail-ui.js#L583) | message |  |
| [closeClip](../harness/verticals/retail/web/retail-ui.js#L585) |  |  |
| [renderEvidence](../harness/verticals/retail/web/retail-ui.js#L587) | article, message |  |
| [refreshEvidenceMessage](../harness/verticals/retail/web/retail-ui.js#L596) | message |  |
| [closeUploadDialog](../harness/verticals/retail/web/retail-ui.js#L618) |  |  |
| [openUploadDialog](../harness/verticals/retail/web/retail-ui.js#L620) | opener, collection |  |
| [loadSourceLinks](../harness/verticals/retail/web/retail-ui.js#L624) |  |  |
| [sourceLinkLabel](../harness/verticals/retail/web/retail-ui.js#L631) | link |  |
| [renderSourceLinks](../harness/verticals/retail/web/retail-ui.js#L633) |  |  |
| [addSourceLink](../harness/verticals/retail/web/retail-ui.js#L638) | event |  |
| [sourceLinkAction](../harness/verticals/retail/web/retail-ui.js#L644) | link, action |  |
| [uploadStorageKey](../harness/verticals/retail/web/retail-ui.js#L646) |  |  |
| [uploadTickets](../harness/verticals/retail/web/retail-ui.js#L648) |  |  |
| [saveUploadTicket](../harness/verticals/retail/web/retail-ui.js#L650) | ticket |  |
| [removeUploadTicket](../harness/verticals/retail/web/retail-ui.js#L652) | id |  |
| [resetImports](../harness/verticals/retail/web/retail-ui.js#L654) |  |  |
| [importWritable](../harness/verticals/retail/web/retail-ui.js#L656) |  |  |
| [importManageable](../harness/verticals/retail/web/retail-ui.js#L658) |  |  |
| [importCurrentScope](../harness/verticals/retail/web/retail-ui.js#L660) |  |  |
| [importFailure](../harness/verticals/retail/web/retail-ui.js#L662) | error |  |
| [importRequest](../harness/verticals/retail/web/retail-ui.js#L664) | path, {method = 'GET', body, headers = {}, work, retry = false, interruptible = true} = {} |  |
| [importPath](../harness/verticals/retail/web/retail-ui.js#L681) | id |  |
| [applyImport](../harness/verticals/retail/web/retail-ui.js#L683) | row |  |
| [loadImports](../harness/verticals/retail/web/retail-ui.js#L696) |  |  |
| [uploadStatus](../harness/verticals/retail/web/retail-ui.js#L718) | row, work |  |
| [renderImports](../harness/verticals/retail/web/retail-ui.js#L730) |  |  |
| [chooseUpload](../harness/verticals/retail/web/retail-ui.js#L776) | id = null |  |
| [fileFingerprint](../harness/verticals/retail/web/retail-ui.js#L780) | file, chunkBytes, work |  |
| [acceptUploadFiles](../harness/verticals/retail/web/retail-ui.js#L791) | dropped = null |  |
| [pumpUploads](../harness/verticals/retail/web/retail-ui.js#L809) |  |  |
| [sendUpload](../harness/verticals/retail/web/retail-ui.js#L815) | work |  |
| [cancelImport](../harness/verticals/retail/web/retail-ui.js#L857) | row, work |  |
| [renderHomeSearch](../harness/verticals/retail/web/retail-ui.js#L898) |  |  |
| [addClipSelection](../harness/verticals/retail/web/retail-ui.js#L908) | card, result, selected, changed |  |
| [searchHome](../harness/verticals/retail/web/retail-ui.js#L910) |  |  |
| [legacySearchHome](../harness/verticals/retail/web/retail-ui.js#L912) |  |  |
| [libraryUrl](../harness/verticals/retail/web/retail-ui.js#L922) | collection, folder = '', asset = '' |  |
| [galleryScopes](../harness/verticals/retail/web/retail-ui.js#L924) |  |  |
| [renderGalleryContext](../harness/verticals/retail/web/retail-ui.js#L926) |  |  |
| [showLibrary](../harness/verticals/retail/web/retail-ui.js#L928) | collection = null, folder = '', asset = '', tab = 'media' |  |
| [legacyLibraryRecordView](../harness/verticals/retail/web/retail-ui.js#L930) | collection = null, folder = '', asset = '', tab = 'media' |  |
| [loadLibrary](../harness/verticals/retail/web/retail-ui.js#L936) |  |  |
| [searchLibrary](../harness/verticals/retail/web/retail-ui.js#L949) | event |  |
| [legacySearchLibrary](../harness/verticals/retail/web/retail-ui.js#L951) | event |  |
| [applyGalleryView](../harness/verticals/retail/web/retail-ui.js#L960) |  |  |
| [setGalleryView](../harness/verticals/retail/web/retail-ui.js#L962) | value |  |
| [renderLibrary](../harness/verticals/retail/web/retail-ui.js#L964) |  |  |
| [clipChip](../harness/verticals/retail/web/retail-ui.js#L996) | clip, remove = null |  |
| [renderClipAttachments](../harness/verticals/retail/web/retail-ui.js#L998) |  |  |
| [openClipPicker](../harness/verticals/retail/web/retail-ui.js#L1000) |  |  |
| [loadClipPicker](../harness/verticals/retail/web/retail-ui.js#L1002) | folder = '', assetId = '' |  |
| [renderClipPicker](../harness/verticals/retail/web/retail-ui.js#L1004) |  |  |
| [searchClipPicker](../harness/verticals/retail/web/retail-ui.js#L1009) | event |  |
| [legacySearchClipPicker](../harness/verticals/retail/web/retail-ui.js#L1011) | event |  |
| [updateAgentEstimate](../harness/verticals/retail/web/retail-ui.js#L1029) |  |  |

### harness/verticals/retail/web/tracker-canvas.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [stateOf](../harness/verticals/retail/web/tracker-canvas.js#L25) | type |  |
| [shelves](../harness/verticals/retail/web/tracker-canvas.js#L26) | events, now |  |
| [ranking](../harness/verticals/retail/web/tracker-canvas.js#L53) | events |  |
| [outputShelves](../harness/verticals/retail/web/tracker-canvas.js#L65) | list, events, now |  |
| [outputRanking](../harness/verticals/retail/web/tracker-canvas.js#L81) | items, events |  |
| [stateCanvas](../harness/verticals/retail/web/tracker-canvas.js#L88) | view, ui, context |  |
| [rankingCanvas](../harness/verticals/retail/web/tracker-canvas.js#L102) | view, ui, context |  |

### harness/web/app.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [preferredChatId](../harness/web/app.js#L13) | records |  |
| [keptHarness](../harness/web/app.js#L46) |  |  |
| [keepHarness](../harness/web/app.js#L47) | shell |  |
| [applyHarness](../harness/web/app.js#L48) |  |  |
| [renderVerticalNavigation](../harness/web/app.js#L49) |  |  |
| [showVerticalTab](../harness/web/app.js#L57) | id |  |
| [loadHarness](../harness/web/app.js#L65) | attempt = 0 |  |
| [delegateIcon](../harness/web/app.js#L221) | id, active = false |  |
| [toolIcon](../harness/web/app.js#L226) | name |  |
| [childActivity](../harness/web/app.js#L227) | chat |  |
| [scopes](../harness/web/app.js#L235) |  |  |
| [currentCollection](../harness/web/app.js#L247) |  |  |
| [renderFounder](../harness/web/app.js#L252) |  |  |
| [openFounder](../harness/web/app.js#L253) |  |  |
| [renderFounderOptions](../harness/web/app.js#L254) |  |  |
| [selectFounderCollection](../harness/web/app.js#L258) | collection |  |
| [renderCollectionControl](../harness/web/app.js#L269) | id, value, choices, onSelect |  |
| [renderCollectionOptions](../harness/web/app.js#L274) |  |  |
| [workspaceEmpty](../harness/web/app.js#L275) | symbol, title, copy, actions=[] |  |
| [selectScope](../harness/web/app.js#L276) | dataset |  |
| [notice](../harness/web/app.js#L279) | text |  |
| [save](../harness/web/app.js#L280) |  |  |
| [saveQueue](../harness/web/app.js#L281) |  |  |
| [draftAttachments](../harness/web/app.js#L282) | items |  |
| [persistDraft](../harness/web/app.js#L285) | chatId=activeId, capture=true |  |
| [restoreDrafts](../harness/web/app.js#L291) | preserveLive=false |  |
| [clearSentDraft](../harness/web/app.js#L294) | chatId |  |
| [setSidebar](../harness/web/app.js#L298) | open |  |
| [chooseChat](../harness/web/app.js#L299) | chat |  |
| [showHome](../harness/web/app.js#L300) |  |  |
| [startAgentConversation](../harness/web/app.js#L301) | kind = null, agent = null |  |
| [openWorkspaceChat](../harness/web/app.js#L302) | chatId |  |
| [openWorkspaceChatList](../harness/web/app.js#L303) |  |  |
| [openWorkspaceAgent](../harness/web/app.js#L304) | agent |  |
| [ensureWorkspaceTabs](../harness/web/app.js#L305) |  |  |
| [newChat](../harness/web/app.js#L315) |  |  |
| [chatAgentKind](../harness/web/app.js#L317) | chat |  |
| [renderSidebar](../harness/web/app.js#L318) |  |  |
| [section](../harness/web/app.js#L327) | key |  |
| [row](../harness/web/app.js#L334) | container, { key, symbol, title, state = '', chat = null, current = false, archive = false, open } |  |
| [setPicker](../harness/web/app.js#L373) | name, open |  |
| [renderScopeOptions](../harness/web/app.js#L374) |  |  |
| [renderEnvironments](../harness/web/app.js#L380) |  |  |
| [normalizeRemoteMessage](../harness/web/app.js#L381) | message, index, chatId |  |
| [registerChild](../harness/web/app.js#L382) | event, answer, parent |  |
| [pollChild](../harness/web/app.js#L383) | chatId, navigate = false |  |
| [openChatId](../harness/web/app.js#L397) | chatId |  |
| [safeUrl](../harness/web/app.js#L398) | value |  |
| [sourceIcon](../harness/web/app.js#L401) | value |  |
| [addSourceIcon](../harness/web/app.js#L406) | anchor, url |  |
| [renderText](../harness/web/app.js#L409) | el, text, message = null |  |
| [renderSubagentGroup](../harness/web/app.js#L428) | children |  |
| [toolLabel](../harness/web/app.js#L429) | tool, working |  |
| [workDuration](../harness/web/app.js#L430) | message |  |
| [activityShimmer](../harness/web/app.js#L431) | element |  |
| [toolCall](../harness/web/app.js#L432) | tool, {working=false, label=toolLabel(tool, working |  |
| [toolReferences](../harness/web/app.js#L439) | message |  |
| [openFile](../harness/web/app.js#L443) | file, opener |  |
| [args](../harness/web/app.js#L448) | tool |  |
| [renderToolTrail](../harness/web/app.js#L458) | tools, pending=false, message=null |  |
| [disclosureState](../harness/web/app.js#L459) | article |  |
| [restoreDisclosures](../harness/web/app.js#L460) | article, saved |  |
| [providerResourceUrl](../harness/web/app.js#L462) | file |  |
| [providerResourceActions](../harness/web/app.js#L463) | file, container |  |
| [providerResourceCard](../harness/web/app.js#L464) | file |  |
| [pauseMedia](../harness/web/app.js#L465) | root |  |
| [nativeMediaType](../harness/web/app.js#L466) | file |  |
| [nativeMediaPlayer](../harness/web/app.js#L470) | file |  |
| [fileType](../harness/web/app.js#L474) | file |  |
| [artifactCard](../harness/web/app.js#L475) | file |  |
| [renderChatContext](../harness/web/app.js#L476) |  |  |
| [setChatContext](../harness/web/app.js#L477) | open |  |
| [credentialMetadata](../harness/web/app.js#L478) | request |  |
| [credentialRequestFor](../harness/web/app.js#L486) | chatId, requestId |  |
| [credentialOwnerChat](../harness/web/app.js#L487) | chat = activeChat( |  |
| [credentialKey](../harness/web/app.js#L491) | chatId, requestId |  |
| [credentialResolution](../harness/web/app.js#L492) | request |  |
| [credentialRequestCard](../harness/web/app.js#L499) | request |  |
| [scheduleCredentialSync](../harness/web/app.js#L508) |  |  |
| [syncCredentialRequests](../harness/web/app.js#L509) |  |  |
| [openCredentialRequest](../harness/web/app.js#L515) | chatId, requestId, opener = null |  |
| [closeCredentialRequest](../harness/web/app.js#L521) | restoreFocus = true |  |
| [finishCredentialClose](../harness/web/app.js#L524) |  |  |
| [renderCredentialModal](../harness/web/app.js#L528) |  |  |
| [mergeCredentialReply](../harness/web/app.js#L536) | chatId, raw |  |
| [submitCredentialRequest](../harness/web/app.js#L540) | action, values={} |  |
| [nativeApprovalMetadata](../harness/web/app.js#L551) | raw |  |
| [nativeApprovalFor](../harness/web/app.js#L558) | chatId, requestId |  |
| [canDecideApproval](../harness/web/app.js#L559) | request |  |
| [approvalResolution](../harness/web/app.js#L560) | request |  |
| [nativeApprovalCard](../harness/web/app.js#L561) | request |  |
| [submitNativeApproval](../harness/web/app.js#L580) | requestId, action |  |
| [nativeQuestionMetadata](../harness/web/app.js#L595) | raw |  |
| [nativeQuestionFor](../harness/web/app.js#L602) | chatId, requestId |  |
| [canAnswerQuestion](../harness/web/app.js#L603) | request |  |
| [questionResolution](../harness/web/app.js#L604) | request |  |
| [nativeQuestionCard](../harness/web/app.js#L605) | request |  |
| [scheduleQuestionSync](../harness/web/app.js#L614) |  |  |
| [syncNativeQuestions](../harness/web/app.js#L615) |  |  |
| [openNativeQuestion](../harness/web/app.js#L621) | chatId, requestId, opener = null |  |
| [closeNativeQuestion](../harness/web/app.js#L631) | restoreFocus = true |  |
| [finishQuestionClose](../harness/web/app.js#L632) |  |  |
| [mergeQuestionReply](../harness/web/app.js#L636) | chatId, raw |  |
| [submitNativeQuestion](../harness/web/app.js#L641) | action, answers=null |  |
| [messageActions](../harness/web/app.js#L648) | message, article |  |
| [messageChildren](../harness/web/app.js#L658) | message |  |
| [messageRenderSignature](../harness/web/app.js#L659) | message |  |
| [reconcileMessages](../harness/web/app.js#L663) | messages, scope |  |
| [renderMessage](../harness/web/app.js#L675) | message |  |
| [updateMessage](../harness/web/app.js#L711) | chat, message |  |
| [reserveTurnSpace](../harness/web/app.js#L720) | chat |  |
| [anchorSubmittedTurn](../harness/web/app.js#L725) | chat |  |
| [placeCompanyPicker](../harness/web/app.js#L731) |  |  |
| [focusCollection](../harness/web/app.js#L733) | key, inputId |  |
| [detailBreadcrumb](../harness/web/app.js#L734) | parent, title, back |  |
| [collectionNavigation](../harness/web/app.js#L735) |  |  |
| [render](../harness/web/app.js#L744) |  |  |
| [setRailChats](../harness/web/app.js#L805) | open |  |
| [syncMobileChatNavigation](../harness/web/app.js#L807) |  |  |
| [selectSessionStorage](../harness/web/app.js#L810) | data |  |
| [mergeRemoteChat](../harness/web/app.js#L842) | data |  |
| [loadServerChats](../harness/web/app.js#L854) |  |  |
| [updateChatPreferences](../harness/web/app.js#L860) | chat, fields |  |
| [loadObservers](../harness/web/app.js#L865) |  |  |
| [renderObserver](../harness/web/app.js#L866) |  |  |
| [changeObserver](../harness/web/app.js#L872) |  |  |
| [endObservation](../harness/web/app.js#L873) |  |  |
| [setProfileMenu](../harness/web/app.js#L874) | open |  |
| [showArchives](../harness/web/app.js#L875) |  |  |
| [renderArchives](../harness/web/app.js#L876) |  |  |
| [closeBusinessChat](../harness/web/app.js#L877) |  |  |
| [showMarketplace](../harness/web/app.js#L878) | tab = 'connections' |  |
| [loadAgentTemplates](../harness/web/app.js#L879) |  |  |
| [loadConnectionDrafts](../harness/web/app.js#L880) |  |  |
| [startAgentChat](../harness/web/app.js#L881) | agent = null, template = null |  |
| [agentItems](../harness/web/app.js#L882) | title, items |  |
| [marketplaceArt](../harness/web/app.js#L883) | id, kind, items |  |
| [openCatalogueDetail](../harness/web/app.js#L884) | kind, item |  |
| [openAgentTemplate](../harness/web/app.js#L885) | template |  |
| [agentTemplateContent](../harness/web/app.js#L886) | content, template |  |
| [renderCatalogueDetail](../harness/web/app.js#L887) | content |  |
| [renderMarketplace](../harness/web/app.js#L888) |  |  |
| [catalogueItem](../harness/web/app.js#L903) | card, label, action |  |
| [customerConnection](../harness/web/app.js#L904) | item |  |
| [renderCustomizeContext](../harness/web/app.js#L905) |  |  |
| [connectionLogoUrl](../harness/web/app.js#L915) | item |  |
| [connectionLogo](../harness/web/app.js#L916) | item, className = '' |  |
| [brokerFor](../harness/web/app.js#L917) | item |  |
| [providerCatalogueItem](../harness/web/app.js#L918) | connection |  |
| [providerCatalogueEntry](../harness/web/app.js#L926) | provider |  |
| [composerConnections](../harness/web/app.js#L927) |  |  |
| [connectionStatus](../harness/web/app.js#L928) | item |  |
| [connectionSource](../harness/web/app.js#L929) | item |  |
| [suggestedConnections](../harness/web/app.js#L931) |  |  |
| [loadConnectionCatalogue](../harness/web/app.js#L932) |  |  |
| [openConnectionDetail](../harness/web/app.js#L945) | item |  |
| [nativePluginFor](../harness/web/app.js#L946) | item |  |
| [pluginWritable](../harness/web/app.js#L947) |  |  |
| [pluginInstallable](../harness/web/app.js#L948) | item |  |
| [connectionCard](../harness/web/app.js#L949) | item |  |
| [pluginAvailability](../harness/web/app.js#L956) | item |  |
| [pluginViews](../harness/web/app.js#L957) |  |  |
| [openNativePluginDialog](../harness/web/app.js#L958) | item |  |
| [renderNativePluginDialog](../harness/web/app.js#L959) |  |  |
| [changeNativePlugin](../harness/web/app.js#L978) | item, action |  |
| [renderConnectionsCatalogue](../harness/web/app.js#L1005) | content |  |
| [renderConnectionDetail](../harness/web/app.js#L1015) | content, item |  |
| [customConnectorWritable](../harness/web/app.js#L1025) | item |  |
| [clearCustomCredentialInputs](../harness/web/app.js#L1027) |  |  |
| [customConnectorStatus](../harness/web/app.js#L1028) | item |  |
| [customConnectorCard](../harness/web/app.js#L1029) | item |  |
| [openCustomConnectorDialog](../harness/web/app.js#L1034) | opener, { collection = null, ...options } = {} |  |
| [createCustomConnector](../harness/web/app.js#L1046) | event |  |
| [openCustomConnector](../harness/web/app.js#L1058) | item |  |
| [loadCustomConnector](../harness/web/app.js#L1062) | item |  |
| [continueCustomConnector](../harness/web/app.js#L1071) | item |  |
| [customExecutionAction](../harness/web/app.js#L1074) | item, action, payload, button |  |
| [refreshCustomExecution](../harness/web/app.js#L1089) | item |  |
| [reviewCustomTarget](../harness/web/app.js#L1104) | item, opener |  |
| [renderCustomExecution](../harness/web/app.js#L1117) | content, item |  |
| [customSecretField](../harness/web/app.js#L1137) | item, field |  |
| [submitCredential](../harness/web/app.js#L1143) | revoke |  |
| [renderCustomConnectionDetail](../harness/web/app.js#L1154) | content, item |  |
| [openBundledSkill](../harness/web/app.js#L1169) | plugin, skill |  |
| [clearConnectionCredential](../harness/web/app.js#L1170) |  |  |
| [openConnectionSetup](../harness/web/app.js#L1173) | item |  |
| [renderConnectionFlow](../harness/web/app.js#L1216) |  |  |
| [renderAttachmentConnections](../harness/web/app.js#L1219) |  |  |
| [connectionStack](../harness/web/app.js#L1221) | dependencies |  |
| [loadSkills](../harness/web/app.js#L1226) |  |  |
| [renderSkillsCatalogue](../harness/web/app.js#L1232) | content |  |
| [openReusableSkill](../harness/web/app.js#L1236) | skill |  |
| [skillDetailContent](../harness/web/app.js#L1237) | content, skill, screen |  |
| [renderSelectedSkills](../harness/web/app.js#L1254) |  |  |
| [consumeMention](../harness/web/app.js#L1255) |  |  |
| [draftAdmitting](../harness/web/app.js#L1256) | chatId=activeId |  |
| [selectSkill](../harness/web/app.js#L1257) | id |  |
| [renderSkillsSubmenu](../harness/web/app.js#L1258) |  |  |
| [openSkillsSubmenu](../harness/web/app.js#L1259) |  |  |
| [closeSkillsSubmenu](../harness/web/app.js#L1260) |  |  |
| [createSkillChat](../harness/web/app.js#L1261) |  |  |
| [closeCommandMenu](../harness/web/app.js#L1263) |  |  |
| [consumeCommand](../harness/web/app.js#L1264) |  |  |
| [chooseCommand](../harness/web/app.js#L1265) | action |  |
| [connectionSkills](../harness/web/app.js#L1266) | connection |  |
| [renderCommandMenu](../harness/web/app.js#L1267) |  |  |
| [updateMentionMenu](../harness/web/app.js#L1274) |  |  |
| [handleCommandMenu](../harness/web/app.js#L1275) | event |  |
| [handleComposerMenu](../harness/web/app.js#L1276) | event |  |
| [businessMapMetadata](../harness/web/app.js#L1289) | value |  |
| [invalidateBusinessMaps](../harness/web/app.js#L1293) | collection |  |
| [resetBusinessMaps](../harness/web/app.js#L1294) |  |  |
| [expandBusinessMap](../harness/web/app.js#L1295) | entry, opener |  |
| [businessMapSurface](../harness/web/app.js#L1296) | collection, metadata=null, revision='' |  |
| [showBusiness](../harness/web/app.js#L1303) | collection = null |  |
| [loadBusiness](../harness/web/app.js#L1304) |  |  |
| [openOnboarding](../harness/web/app.js#L1305) |  |  |
| [renderBusiness](../harness/web/app.js#L1317) |  |  |
| [closeBusinessEditor](../harness/web/app.js#L1329) |  |  |
| [openBusinessEditor](../harness/web/app.js#L1330) | data, opener |  |
| [showStats](../harness/web/app.js#L1349) |  |  |
| [statsAllowed](../harness/web/app.js#L1350) |  |  |
| [renderStatsActivity](../harness/web/app.js#L1351) |  |  |
| [loadStatsActivity](../harness/web/app.js#L1356) |  |  |
| [loadWorkspaceCapabilities](../harness/web/app.js#L1363) | dataset = 'company' |  |
| [renderAgentSetupNotice](../harness/web/app.js#L1371) |  |  |
| [agentExecutionReady](../harness/web/app.js#L1379) | agent |  |
| [resetFiles](../harness/web/app.js#L1382) |  |  |
| [currentFilesScope](../harness/web/app.js#L1388) |  |  |
| [updateFilesSurface](../harness/web/app.js#L1389) |  |  |
| [setFilesPane](../harness/web/app.js#L1397) | open, opener = null |  |
| [loadFiles](../harness/web/app.js#L1398) |  |  |
| [renderFilesMessage](../harness/web/app.js#L1408) |  |  |
| [generatedFileCard](../harness/web/app.js#L1409) | file |  |
| [fileFormat](../harness/web/app.js#L1410) | file |  |
| [workspaceFileCard](../harness/web/app.js#L1411) | file |  |
| [markFileOpened](../harness/web/app.js#L1418) | file |  |
| [openFileRename](../harness/web/app.js#L1422) | file, opener |  |
| [renameFile](../harness/web/app.js#L1423) | event |  |
| [chatAboutFile](../harness/web/app.js#L1427) | file, question='' |  |
| [renderGeneratedFiles](../harness/web/app.js#L1429) |  |  |
| [openGeneratedFile](../harness/web/app.js#L1432) | file, opener |  |
| [previewTable](../harness/web/app.js#L1462) | text, name |  |
| [renderFilePreview](../harness/web/app.js#L1463) |  |  |
| [fileSize](../harness/web/app.js#L1491) | value |  |
| [agentFrequency](../harness/web/app.js#L1493) | agent |  |
| [agentDate](../harness/web/app.js#L1497) | value |  |
| [cadenceLabel](../harness/web/app.js#L1498) | seconds |  |
| [agentButton](../harness/web/app.js#L1499) | label, handler, primary = false, symbol = null |  |
| [agentState](../harness/web/app.js#L1500) | agent |  |
| [agentCardMetadata](../harness/web/app.js#L1502) | value |  |
| [normalizeAgentCards](../harness/web/app.js#L1506) | values |  |
| [agentConversationCard](../harness/web/app.js#L1507) | agent |  |
| [releaseLinkedAlert](../harness/web/app.js#L1509) |  |  |
| [showLinkedAlert](../harness/web/app.js#L1510) |  |  |
| [activePhoneAgentId](../harness/web/app.js#L1515) |  |  |
| [phoneParticipantName](../harness/web/app.js#L1516) | memberId |  |
| [loadAgentPhone](../harness/web/app.js#L1517) | id |  |
| [saveAgentPhone](../harness/web/app.js#L1523) | id, block |  |
| [renderPhoneContactNotice](../harness/web/app.js#L1524) |  |  |
| [syncAgentPhone](../harness/web/app.js#L1532) |  |  |
| [agentInfoPhone](../harness/web/app.js#L1533) | selected, detail |  |
| [renderAgentHeader](../harness/web/app.js#L1540) |  |  |
| [showAgents](../harness/web/app.js#L1546) | id = null |  |
| [openAgentConversation](../harness/web/app.js#L1549) | id |  |
| [loadAgents](../harness/web/app.js#L1554) | forSidebar = false |  |
| [closeAgentInfo](../harness/web/app.js#L1561) |  |  |
| [openAgentInfo](../harness/web/app.js#L1562) | id, opener |  |
| [refreshAgentInfo](../harness/web/app.js#L1567) |  |  |
| [agentFrequencyForm](../harness/web/app.js#L1568) | selected |  |
| [renderAgents](../harness/web/app.js#L1572) |  |  |
| [renderAgentDetails](../harness/web/app.js#L1585) | selected, detail |  |
| [openAgentEditor](../harness/web/app.js#L1621) | agent = null |  |
| [updateAgentMode](../harness/web/app.js#L1628) |  |  |
| [saveAgent](../harness/web/app.js#L1634) | event |  |
| [agentAction](../harness/web/app.js#L1643) | agent, action |  |
| [resizeComposer](../harness/web/app.js#L1649) |  |  |
| [updateMode](../harness/web/app.js#L1650) |  |  |
| [renderAttachments](../harness/web/app.js#L1660) |  |  |
| [pasteImages](../harness/web/app.js#L1666) | event |  |
| [uploadImages](../harness/web/app.js#L1671) | files |  |
| [toggleAttachmentMenu](../harness/web/app.js#L1685) | open, restoreFocus = false |  |
| [queueIcon](../harness/web/app.js#L1689) | name, className = '' |  |
| [queueWritable](../harness/web/app.js#L1695) | chatId = activeId |  |
| [queueEditable](../harness/web/app.js#L1699) | item |  |
| [editQueuedMessage](../harness/web/app.js#L1702) | item |  |
| [queuedThumbnail](../harness/web/app.js#L1710) | item |  |
| [renderQueue](../harness/web/app.js#L1717) |  |  |
| [drainQueue](../harness/web/app.js#L1735) | id, chatId = activeId |  |
| [steerMessage](../harness/web/app.js#L1736) | item |  |
| [stopChat](../harness/web/app.js#L1748) | chatId = activeId |  |
| [request](../harness/web/app.js#L1749) | url, data |  |
| [submit](../harness/web/app.js#L1754) | event |  |
| [continueAgentRun](../harness/web/app.js#L1765) | report |  |
| [runQuery](../harness/web/app.js#L1776) | chat, query, mode, dataset, attachments = [], extras = {}, skillIds = [], composerDraft = false |  |
| [receive](../harness/web/app.js#L1787) | line |  |
| [showSession](../harness/web/app.js#L1817) | message = '' |  |
| [renderOperator](../harness/web/app.js#L1818) |  |  |
| [contextText](../harness/web/app.js#L1819) |  |  |
| [renderContextRing](../harness/web/app.js#L1820) |  |  |
| [preferencesIdentity](../harness/web/app.js#L1821) |  |  |
| [savePreferences](../harness/web/app.js#L1822) | value |  |
| [teamMembers](../harness/web/app.js#L1823) |  |  |
| [renderWorkspaceSettings](../harness/web/app.js#L1829) |  |  |
| [showWorkspaceSettings](../harness/web/app.js#L1833) | view |  |
| [messagingScope](../harness/web/app.js#L1834) |  |  |
| [messagingViewData](../harness/web/app.js#L1835) | data=messagingData |  |
| [renderMessagingSettings](../harness/web/app.js#L1836) |  |  |
| [loadMessaging](../harness/web/app.js#L1840) | memberId=session?.principal?.id |  |
| [openMemberProfile](../harness/web/app.js#L1846) | member, page='profile', channel='' |  |
| [openOrganizationChat](../harness/web/app.js#L1852) | purpose, collection=currentCollection( |  |
| [renderProfileSettings](../harness/web/app.js#L1856) |  |  |
| [loadProfileSettings](../harness/web/app.js#L1859) |  |  |
| [showProfileSettings](../harness/web/app.js#L1865) |  |  |
| [renderPluginSettings](../harness/web/app.js#L1866) |  |  |
| [showPluginSettings](../harness/web/app.js#L1871) |  |  |
| [usageNumber](../harness/web/app.js#L1872) | value |  |
| [fundingNotice](../harness/web/app.js#L1873) |  |  |
| [renderFundingNotice](../harness/web/app.js#L1881) |  |  |
| [refreshUsage](../harness/web/app.js#L1885) |  |  |
| [setUsagePopover](../harness/web/app.js#L1886) | open, restoreFocus = false |  |
| [usageBar](../harness/web/app.js#L1887) | label, used, maximum, caption, suffix = '' |  |
| [renderUsagePopover](../harness/web/app.js#L1888) |  |  |
| [openUsage](../harness/web/app.js#L1894) |  |  |
| [renderUsage](../harness/web/app.js#L1895) |  |  |
| [closeMcpDialog](../harness/web/app.js#L1905) |  |  |
| [resetMcp](../harness/web/app.js#L1911) |  |  |
| [mcpRecord](../harness/web/app.js#L1912) | item |  |
| [mcpEndpoint](../harness/web/app.js#L1913) | value |  |
| [loadMcp](../harness/web/app.js#L1914) |  |  |
| [showMcp](../harness/web/app.js#L1926) |  |  |
| [copyMcp](../harness/web/app.js#L1927) | value, button, identity = mcpIdentity( |  |
| [renderMcp](../harness/web/app.js#L1928) |  |  |
| [mcpDialogShell](../harness/web/app.js#L1948) | title |  |
| [openMcpForm](../harness/web/app.js#L1952) |  |  |
| [openMcpKey](../harness/web/app.js#L1972) | token, connection |  |
| [openMcpRevoke](../harness/web/app.js#L1978) | item |  |
| [renderConnection](../harness/web/app.js#L1992) |  |  |
| [openInitialSession](../harness/web/app.js#L2003) |  |  |
| [loadSession](../harness/web/app.js#L2004) |  |  |
| [login](../harness/web/app.js#L2008) | event, demo = false |  |
| [loadStatus](../harness/web/app.js#L2009) | refresh = false |  |
| [openQuickSearch](../harness/web/app.js#L2024) |  |  |

### harness/web/business-map.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [safeURL](../harness/web/business-map.js#L45) | value |  |
| [validate](../harness/web/business-map.js#L71) | data |  |
| [geometry](../harness/web/business-map.js#L110) | value, allowed |  |
| [collection](../harness/web/business-map.js#L141) | value, allowed |  |
| [loadD3](../harness/web/business-map.js#L293) |  |  |
| [glyph](../harness/web/business-map.js#L311) | category |  |
| [dispose](../harness/web/business-map.js#L343) | root |  |
| [render](../harness/web/business-map.js#L352) | input, { node = make, icon, onExpand } = {} |  |
| [select](../harness/web/business-map.js#L405) | key, label, values |  |
| [renderSelection](../harness/web/business-map.js#L652) |  |  |
| [positionPins](../harness/web/business-map.js#L676) |  |  |
| [labels](../harness/web/business-map.js#L756) |  |  |
| [scaleBar](../harness/web/business-map.js#L785) |  |  |
| [updateLayers](../harness/web/business-map.js#L795) |  |  |
| [resize](../harness/web/business-map.js#L846) |  |  |

### harness/web/business-summary.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [render](../harness/web/business-summary.js#L5) | data, { node, icon, safeUrl, sourceIcon } |  |
| [reference](../harness/web/business-summary.js#L24) | value |  |
| [link](../harness/web/business-summary.js#L30) | href, label, symbol, className = 'business-summary-action' |  |
| [renderProfile](../harness/web/business-summary.js#L80) | data, helpers |  |
| [addList](../harness/web/business-summary.js#L112) | title, values, className |  |

### harness/web/display-canvas.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [create](../harness/web/display-canvas.js#L4) | extend = ( |  |
| [el](../harness/web/display-canvas.js#L23) | tag, props, ...kids |  |
| [svg](../harness/web/display-canvas.js#L36) | tag, props, ...kids |  |
| [safeUrl](../harness/web/display-canvas.js#L47) | value |  |
| [ownUrl](../harness/web/display-canvas.js#L52) | value |  |
| [stamp](../harness/web/display-canvas.js#L57) | value |  |
| [dayName](../harness/web/display-canvas.js#L71) | ms, now |  |
| [when](../harness/web/display-canvas.js#L75) | ms, now |  |
| [span](../harness/web/display-canvas.js#L80) | ms |  |
| [cadence](../harness/web/display-canvas.js#L90) | agent |  |
| [inline](../harness/web/display-canvas.js#L104) | text, inert |  |
| [rich](../harness/web/display-canvas.js#L119) | text, className = 'tc-rich', inert = false |  |
| [sections](../harness/web/display-canvas.js#L135) | text |  |
| [occurrence](../harness/web/display-canvas.js#L157) | raw, index, published |  |
| [family](../harness/web/display-canvas.js#L174) | agent, observations |  |
| [signals](../harness/web/display-canvas.js#L184) | events |  |
| [buckets](../harness/web/display-canvas.js#L189) | period, now |  |
| [metric](../harness/web/display-canvas.js#L209) | events, period, now |  |
| [memosOf](../harness/web/display-canvas.js#L223) | data, summary |  |
| [format](../harness/web/display-canvas.js#L234) | kind, value, currency |  |
| [written](../harness/web/display-canvas.js#L244) | row, other |  |
| [reading](../harness/web/display-canvas.js#L251) | out, period |  |
| [bound](../harness/web/display-canvas.js#L258) | canvas, name, text |  |
| [shownOutput](../harness/web/display-canvas.js#L265) | out, saved, kind, set, period |  |
| [outputMetric](../harness/web/display-canvas.js#L281) | series, events, period |  |
| [model](../harness/web/display-canvas.js#L293) | agent, observations, options = {} |  |
| [curve](../harness/web/display-canvas.js#L345) | points |  |
| [layout](../harness/web/display-canvas.js#L357) | values, box |  |
| [lineMark](../harness/web/display-canvas.js#L361) | values, box, className |  |
| [kitMark](../harness/web/display-canvas.js#L369) | kind, points, opts |  |
| [lineChart](../harness/web/display-canvas.js#L376) | { title, points, selected, onSelect, read } |  |
| [show](../harness/web/display-canvas.js#L398) | next |  |
| [spark](../harness/web/display-canvas.js#L422) | values |  |
| [stopPreview](../harness/web/display-canvas.js#L425) |  |  |
| [startPreview](../harness/web/display-canvas.js#L426) | frame, item |  |
| [thumb](../harness/web/display-canvas.js#L440) | item, host |  |
| [occurrenceRow](../harness/web/display-canvas.js#L456) | item, context, options = {} |  |
| [occurrenceList](../harness/web/display-canvas.js#L465) | items, context |  |
| [rail](../harness/web/display-canvas.js#L469) | title, count, body, extra |  |
| [facts](../harness/web/display-canvas.js#L475) | view |  |
| [periodToggle](../harness/web/display-canvas.js#L479) | current, onChange |  |
| [recommendation](../harness/web/display-canvas.js#L489) | text, inert = false |  |
| [metricCanvas](../harness/web/display-canvas.js#L495) | view, ui, context |  |
| [occurrenceCanvas](../harness/web/display-canvas.js#L506) | view, ui, context |  |
| [feedEntry](../harness/web/display-canvas.js#L512) | item, context, fresh |  |
| [feedList](../harness/web/display-canvas.js#L524) | items, context, fresh |  |
| [liveRail](../harness/web/display-canvas.js#L535) | view, ui, context |  |
| [liveCanvas](../harness/web/display-canvas.js#L545) | view, ui, context |  |
| [blockCanvas](../harness/web/display-canvas.js#L555) | view, ui, context |  |
| [restingCanvas](../harness/web/display-canvas.js#L615) |  |  |
| [mount](../harness/web/display-canvas.js#L622) | options = {} |  |
| [openPicker](../harness/web/display-canvas.js#L644) |  |  |
| [closePicker](../harness/web/display-canvas.js#L645) | keepFocus |  |
| [pick](../harness/web/display-canvas.js#L646) | id |  |
| [picker](../harness/web/display-canvas.js#L652) |  |  |
| [head](../harness/web/display-canvas.js#L668) |  |  |
| [place](../harness/web/display-canvas.js#L679) | name, node |  |
| [watchEarlier](../harness/web/display-canvas.js#L684) |  |  |
| [paint](../harness/web/display-canvas.js#L691) | force, focusKey |  |
| [tile](../harness/web/display-canvas.js#L742) | options = {} |  |
| [displayInput](../harness/web/display-canvas.js#L776) | display |  |
| [mountDisplay](../harness/web/display-canvas.js#L785) | options = {} |  |
| [tileDisplay](../harness/web/display-canvas.js#L791) | options = {} |  |

### harness/web/display-charts.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [valueOf](../harness/web/display-charts.js#L27) | point |  |
| [monotonePath](../harness/web/display-charts.js#L34) | points |  |
| [lineLayout](../harness/web/display-charts.js#L60) | samples, box |  |
| [polar](../harness/web/display-charts.js#L80) | cx, cy, r, degrees |  |
| [arcPath](../harness/web/display-charts.js#L81) | cx, cy, r, from, to |  |
| [barPath](../harness/web/display-charts.js#L87) | x, top, width, base, radius |  |
| [bezier](../harness/web/display-charts.js#L92) | x1, y1, x2, y2 |  |
| [parseEasing](../harness/web/display-charts.js#L101) | text, fallback |  |
| [parseDuration](../harness/web/display-charts.js#L105) | text, fallback |  |
| [tween](../harness/web/display-charts.js#L125) | ms, ease, step, done |  |
| [surfaceOf](../harness/web/display-charts.js#L138) | host, asked |  |
| [mount](../harness/web/display-charts.js#L146) | host, kind, fallback |  |
| [pointLabel](../harness/web/display-charts.js#L184) | point |  |
| [line](../harness/web/display-charts.js#L191) | host, points, opts |  |
| [place](../harness/web/display-charts.js#L218) | values |  |
| [drawIn](../harness/web/display-charts.js#L237) | ms |  |
| [settle](../harness/web/display-charts.js#L254) |  |  |
| [render](../harness/web/display-charts.js#L259) | reason |  |
| [valueText](../harness/web/display-charts.js#L281) | index |  |
| [showFocus](../harness/web/display-charts.js#L287) | index, announce=true |  |
| [hideFocus](../harness/web/display-charts.js#L300) | announce=true |  |
| [nearest](../harness/web/display-charts.js#L305) | clientX |  |
| [step](../harness/web/display-charts.js#L311) | delta |  |
| [gauge](../harness/web/display-charts.js#L362) | host, fraction, opts, kind |  |
| [box](../harness/web/display-charts.js#L377) |  |  |
| [place](../harness/web/display-charts.js#L386) | f |  |
| [render](../harness/web/display-charts.js#L395) | reason |  |
| [bars](../harness/web/display-charts.js#L423) | host, values, opts |  |
| [litIndex](../harness/web/display-charts.js#L435) |  |  |
| [place](../harness/web/display-charts.js#L443) | heights |  |
| [render](../harness/web/display-charts.js#L478) | reason |  |
| [ghost](../harness/web/display-charts.js#L514) | host, kind, opts |  |
| [render](../harness/web/display-charts.js#L520) |  |  |

### harness/web/harness-shell.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [parse](../harness/web/harness-shell.js#L8) | data |  |

### harness/web/messaging-settings.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [channelList](../harness/web/messaging-settings.js#L23) | data |  |
| [contactsFor](../harness/web/messaging-settings.js#L32) | member, data |  |
| [deliveryLabel](../harness/web/messaging-settings.js#L44) | delivery |  |
| [deliveryText](../harness/web/messaging-settings.js#L49) | delivery |  |
| [chipLabel](../harness/web/messaging-settings.js#L51) | delivery |  |
| [senderLabel](../harness/web/messaging-settings.js#L59) | sender, ownId |  |
| [api](../harness/web/messaging-settings.js#L65) | path, body |  |
| [button](../harness/web/messaging-settings.js#L72) | node, label, fn, className = 'messaging-button' |  |
| [avatar](../harness/web/messaging-settings.js#L73) | node, member, large = false |  |
| [labelValue](../harness/web/messaging-settings.js#L74) | node, label, value |  |
| [render](../harness/web/messaging-settings.js#L75) | data = {}, { node = make, icon, onMember, onSetup } = {} |  |
| [openMember](../harness/web/messaging-settings.js#L92) | { member, data = {}, page = 'profile', channel: wanted = '', purpose = '', onClose, onRequestCode, onVerifyCode, onSetup, node = make, icon } = {} |  |
| [selected](../harness/web/messaging-settings.js#L98) |  |  |
| [dispose](../harness/web/messaging-settings.js#L105) |  |  |
| [close](../harness/web/messaging-settings.js#L106) |  |  |
| [setup](../harness/web/messaging-settings.js#L107) |  |  |
| [show](../harness/web/messaging-settings.js#L108) | next |  |
| [focus](../harness/web/messaging-settings.js#L109) | key |  |
| [input](../harness/web/messaging-settings.js#L110) | label, value, key, { placeholder = '', autocomplete = '', maxLength = 30 } = {} |  |
| [run](../harness/web/messaging-settings.js#L111) | action, apply |  |
| [channelPicker](../harness/web/messaging-settings.js#L118) | active |  |
| [draw](../harness/web/messaging-settings.js#L128) | preferred |  |
| [valid](../harness/web/messaging-settings.js#L186) |  |  |
| [sync](../harness/web/messaging-settings.js#L187) |  |  |
| [openContactCard](../harness/web/messaging-settings.js#L205) | { block, participant, agentTitle = '', node = make, icon, onClose } = {} |  |
| [mountPhone](../harness/web/messaging-settings.js#L218) | { agentId, agentTitle = '', node = make, icon, readOnly = false, onChange } = {} |  |
| [schedule](../harness/web/messaging-settings.js#L224) |  |  |
| [load](../harness/web/messaging-settings.js#L225) | quiet = false |  |
| [change](../harness/web/messaging-settings.js#L231) | path, body, focusKey |  |
| [contactCard](../harness/web/messaging-settings.js#L239) | participant |  |
| [addNumber](../harness/web/messaging-settings.js#L243) | participant, key |  |
| [toggle](../harness/web/messaging-settings.js#L248) | label, checked, key, disabled, apply |  |
| [spendLine](../harness/web/messaging-settings.js#L252) | spend |  |
| [hold](../harness/web/messaging-settings.js#L261) | value |  |
| [participantRow](../harness/web/messaging-settings.js#L270) | person, manage |  |
| [draw](../harness/web/messaging-settings.js#L301) | preferred |  |
| [restore](../harness/web/messaging-settings.js#L333) | key |  |

### harness/web/plugin-settings.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [render](../harness/web/plugin-settings.js#L9) | data = {}, { node = nodeDefault, icon, logo, onOpen, onBrowse, onAdd } = {} |  |
| [action](../harness/web/plugin-settings.js#L14) | label, callback, primary = false |  |
| [show](../harness/web/plugin-settings.js#L27) | kind, focus = false |  |

### harness/web/profile-settings.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [render](../harness/web/profile-settings.js#L12) | data, { node = defaultNode, icon, scope = 'person', mode = 'daily', loading = false, error = '', onMode, onAgent } = {} |  |
| [chart](../harness/web/profile-settings.js#L39) | target, metric, label |  |
| [update](../harness/web/profile-settings.js#L83) | value |  |

### harness/web/question-box.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [element](../harness/web/question-box.js#L4) | tag, className = '', text = '' |  |
| [mount](../harness/web/question-box.js#L5) | container, request, helpers = {} |  |
| [update](../harness/web/question-box.js#L22) |  |  |
| [render](../harness/web/question-box.js#L28) |  |  |
| [proceed](../harness/web/question-box.js#L59) |  |  |
| [send](../harness/web/question-box.js#L65) | action |  |
| [tick](../harness/web/question-box.js#L77) |  |  |

### harness/web/rich-content.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [configure](../harness/web/rich-content.js#L13) | marked |  |
| [script](../harness/web/rich-content.js#L30) | path, global |  |
| [mathAssets](../harness/web/rich-content.js#L39) |  |  |
| [language](../harness/web/rich-content.js#L44) | code |  |
| [button](../harness/web/rich-content.js#L46) | node, icon, label, symbol, action |  |
| [copyButton](../harness/web/rich-content.js#L51) | node, icon, label, text |  |
| [toolbar](../harness/web/rich-content.js#L59) | node, label |  |
| [actions](../harness/web/rich-content.js#L60) | node, label |  |
| [displayLanguage](../harness/web/rich-content.js#L61) | lang |  |
| [expand](../harness/web/rich-content.js#L62) | node, icon, title, build, opener |  |
| [tableText](../harness/web/rich-content.js#L71) | table |  |
| [allowedDiagram](../harness/web/rich-content.js#L77) | source |  |
| [diagram](../harness/web/rich-content.js#L82) | source, target, node |  |
| [enrich](../harness/web/rich-content.js#L103) | root, { node = defaultNode, icon = null, pending = false } = {} |  |

### harness/web/settings-shell.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [mount](../harness/web/settings-shell.js#L28) | { node, icon } |  |
| [filter](../harness/web/settings-shell.js#L85) |  |  |

### harness/web/tool-trail.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [normalizeFramePreviews](../harness/web/tool-trail.js#L19) | value |  |
| [argumentsOf](../harness/web/tool-trail.js#L33) | tool |  |
| [references](../harness/web/tool-trail.js#L40) | tool, args |  |
| [safeThumbnail](../harness/web/tool-trail.js#L58) | value, doc |  |
| [measure](../harness/web/tool-trail.js#L66) | viewport |  |
| [refresh](../harness/web/tool-trail.js#L70) | root |  |
| [render](../harness/web/tool-trail.js#L85) | tools, { pending = false, renderTool, icon, resolveReference, resolveMedia } = {} |  |
| [individual](../harness/web/tool-trail.js#L111) | tool, index |  |
| [group](../harness/web/tool-trail.js#L162) | items |  |

### harness/web/wake-controls.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [create](../harness/web/wake-controls.js#L4) | {node, icon, scope} |  |
| [close](../harness/web/wake-controls.js#L6) | restore=true |  |
| [current](../harness/web/wake-controls.js#L12) | state |  |
| [sync](../harness/web/wake-controls.js#L15) |  |  |
| [open](../harness/web/wake-controls.js#L16) | opener |  |

### harness/web/workspace-extensions.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [register](../harness/web/workspace-extensions.js#L5) | id, factory |  |
| [install](../harness/web/workspace-extensions.js#L10) | context |  |

### harness/web/workspace-home.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [mount](../harness/web/workspace-home.js#L4) | root, context |  |

### harness/web/workspace-settings.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [normalize](../harness/web/workspace-settings.js#L5) | value = {} |  |
| [key](../harness/web/workspace-settings.js#L10) | identity |  |
| [read](../harness/web/workspace-settings.js#L11) | identity |  |
| [write](../harness/web/workspace-settings.js#L12) | identity, preferences |  |
| [apply](../harness/web/workspace-settings.js#L17) | preferences = defaults |  |
| [permission](../harness/web/workspace-settings.js#L23) |  |  |
| [requestPermission](../harness/web/workspace-settings.js#L24) |  |  |
| [notify](../harness/web/workspace-settings.js#L25) | preferences, title, onOpen |  |
| [render](../harness/web/workspace-settings.js#L34) | view, data = {}, { node, icon, onChange, onPermission, onUsage, onMember } = {} |  |

### harness/web/workspace-tabs.js

| Function | Arguments | Source description |
| --- | --- | --- |
| [register](../harness/web/workspace-tabs.js#L6) | id, tabs |  |
| [create](../harness/web/workspace-tabs.js#L14) | {root, context, defaultHome, onError=( |  |
| [configure](../harness/web/workspace-tabs.js#L17) | shell, workspaceIdentity |  |
| [open](../harness/web/workspace-tabs.js#L22) | id='home' |  |
| [setVisible](../harness/web/workspace-tabs.js#L41) | value |  |

### tools/authorize_local_budget.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [authorize](../tools/authorize_local_budget.py#L23) | state, amount_usd, days, acknowledged |  |
| [main](../tools/authorize_local_budget.py#L67) |  |  |

### tools/check-processed-sample.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [main](../tools/check-processed-sample.py#L23) |  |  |
| [get](../tools/check-processed-sample.py#L46) | path, headers |  |

### tools/configure.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [private_path](../tools/configure.py#L14) | path |  |
| [read_env](../tools/configure.py#L21) | path |  |
| [write_env](../tools/configure.py#L33) | path, values |  |
| [main](../tools/configure.py#L44) |  |  |

### tools/dev.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [main](../tools/dev.py#L6) |  |  |
| [record_attempt](../tools/dev.py#L19) |  |  |
| [local](../tools/dev.py#L23) | address |  |
| [connect](../tools/dev.py#L29) | s, address |  |
| [connect_ex](../tools/dev.py#L32) | s, address |  |
| [dns](../tools/dev.py#L35) | host, *a, **kw |  |

### tools/distribution.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [files](../tools/distribution.py#L7) |  |  |
| [main](../tools/distribution.py#L15) |  |  |

### tools/offline/sitecustomize.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [local](../tools/offline/sitecustomize.py#L4) | address |  |
| [check_connect](../tools/offline/sitecustomize.py#L9) | self, address |  |
| [check_connect_ex](../tools/offline/sitecustomize.py#L12) | self, address |  |
| [check_dns](../tools/offline/sitecustomize.py#L15) | host, *a, **kw |  |
| [__init__](../tools/offline/sitecustomize.py#L19) | self, args, *a, **kw |  |

### tools/preview_app.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [__init__](../tools/preview_app.py#L6) | self, app, secure |  |
| [admitted](../tools/preview_app.py#L12) | self |  |
| [__call__](../tools/preview_app.py#L24) | self, scope, receive, send |  |
| [observed](../tools/preview_app.py#L33) | message |  |
| [public_sample](../tools/preview_app.py#L49) | app, prefix, secure, public_origin |  |

### tools/processed_sample.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [digest](../tools/processed_sample.py#L17) | path |  |
| [verify_sample](../tools/processed_sample.py#L25) | directory |  |
| [download_sample](../tools/processed_sample.py#L45) |  |  |
| [install_sample](../tools/processed_sample.py#L85) | state, sample |  |
| [rebind](../tools/processed_sample.py#L109) | value |  |

### tools/render-fixture.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [box](../tools/render-fixture.py#L8) | t |  |
| [frame](../tools/render-fixture.py#L11) | t |  |

### tools/seed.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [private_state](../tools/seed.py#L11) | path |  |
| [write_json](../tools/seed.py#L21) | path, data |  |
| [seed](../tools/seed.py#L25) | path, issue_code |  |
| [main](../tools/seed.py#L69) |  |  |

### tools/serve.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [main](../tools/serve.py#L7) |  |  |

### tools/source-map.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [main](../tools/source-map.py#L6) |  |  |

### tools/verify.py

| Function | Arguments | Source description |
| --- | --- | --- |
| [main](../tools/verify.py#L12) |  |  |

[made by atelier neyra](https://atelierneyra.com)
