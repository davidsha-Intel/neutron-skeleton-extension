# Script run by devstack to setup this project

function neutron_skeleton_extension_configure_common {
    _neutron_service_plugin_class_add $NEUTRON_L2_EXT_PLUGIN
    _neutron_service_plugin_class_add $NEUTRON_L3_EXT_PLUGIN
    iniset /$Q_PLUGIN_CONF_FILE agent extensions "skeleton_port"
    iniset_multiline /$Q_L3_CONF_FILE AGENT extensions "skeleton_router"
    iniset $NEUTRON_CONF DEFAULT service_plugins $Q_SERVICE_PLUGIN_CLASSES
}

if [[ "$1" == "stack" && "$2" == "install" ]]; then
    setup_develop $NEUTRON_SKELETON_EXTENSION_DIR

elif [[ "$1" == "stack" && "$2" == "post-config" ]]; then
    echo_summary "Configuring neutron-skeleton-extension"
    neutron_skeleton_extension_configure_common
fi
