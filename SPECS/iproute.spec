%global             cbq_version v0.7.3

%define rpmversion 3.10.0
%define baserelease 55.el7
%define specrelease 74%{?dist}
%define pkg_release %{specrelease}%{?buildid}

Summary:            Advanced IP routing and network device configuration tools
Name:               iproute
Version:            %{rpmversion}
Release:            %{pkg_release}
Group:              Applications/System
URL:                http://kernel.org/pub/linux/utils/net/%{name}2/
Source0:            %{name}-%{rpmversion}-%{baserelease}.tar.xz
Source1:            cbq-0000.example
Source2:            avpkt
Patch0:             0001-man-lnstat-rewrite-manpage.patch
Patch1:             0002-lnstat-fix-header-displaying-mechanism.patch
Patch2:             0003-iproute2-Ignore-EADDRNOTAVAIL-errors-during-address-.patch
Patch3:             0004-libnetlink-introduce-nc_flags.patch
Patch4:             0005-ipaddress-simplify-ipaddr_flush.patch
Patch5:             0006-ipaddress-fix-ipaddr_flush-for-Linux-3.1.patch
Patch6:             0007-bridge-drop-reference-to-unused-option-embedded-from.patch
Patch7:             0008-bridge-drop-man-page-fragment.patch
Patch8:             0009-bridge-fdb-add-use-option-to-set-NTF_USE-flag-in-fdb.patch
Patch9:             0010-ip-allow-ip-address-show-to-list-addresses-with-cert.patch
Patch10:            0011-ip-extend-ip-address-man-page-to-reflect-the-recent-.patch
Patch11:            0012-ip-address-fix-and-extend-documentation.patch
Patch12:            0013-ip-address.8.in-fix-BNF-syntax-error.patch
Patch13:            0014-man-ip-address-align-synopsis-with-help-output.patch
Patch14:            0015-man-ip-address-document-mngtmpaddr-and-noprefixroute.patch
Patch15:            0016-ss-return-1-if-an-unrecognized-option-was-given.patch
Patch16:            0017-ss-add-support-for-bytes_acked-bytes_received.patch
Patch17:            0018-ss-add-support-for-segs_in-and-segs_out.patch
Patch18:            0019-ip-address-fix-oneline-mode-for-interfaces-with-VF.patch
Patch19:            0020-neighbor-check-return-values.patch
Patch20:            0021-gre-raising-the-size-of-the-buffer-holding-nl-messag.patch
Patch21:            0022-Allow-specifying-bridge-port-STP-state-by-name-rathe.patch
Patch22:            0023-fix-ip-force-batch-to-continue-on-errors.patch
Patch23:            0024-ip-fix-exit-code-for-addrlabel.patch
Patch24:            0025-link-dump-filter.patch
Patch25:            0026-ip-return-correct-exit-code-on-route-failure.patch
Patch26:            0027-ip-fix-exit-code-for-rule-failures.patch
Patch27:            0028-libnetlink-add-size-argument-to-rtnl_talk.patch
Patch28:            0029-libnetlink-don-t-confuse-variables-in-rtnl_talk.patch
Patch29:            0030-man-ss-Fix-explanation-when-no-options-specified.patch
Patch30:            0031-iproute-restrict-hoplimit-values-to-be-in-range-0-25.patch
Patch31:            0032-iproute2-ip-route.8.in-minor-fixes.patch
Patch32:            0033-ip-route-enable-per-route-ecn-settings-via-features-.patch
Patch33:            0034-ip-route-add-congestion-control-metric.patch
Patch34:            0035-ip-link-remove-warning-message.patch
Patch35:            0036-route-ignore-RTAX_HOPLIMIT-of-value-1.patch
Patch36:            0037-route-Fix-printing-of-locked-entries.patch
Patch37:            0038-man-tc-add-man-page-for-fq-pacer.patch
Patch38:            0039-man-fix-whatis-for-fq.patch
Patch39:            0040-batch-support-quoted-strings.patch
Patch40:            0041-tc-add-a-man-page-for-basic-filter.patch
Patch41:            0042-tc-add-a-man-page-for-cgroup-filter.patch
Patch42:            0043-tc-add-a-man-page-for-flow-filter.patch
Patch43:            0044-tc-add-a-man-page-for-fw-filter.patch
Patch44:            0045-tc-add-a-man-page-for-route-filter.patch
Patch45:            0046-tc-add-a-man-page-for-tcindex-filter.patch
Patch46:            0047-tc-add-a-man-page-for-u32-filter.patch
Patch47:            0048-tc-ship-filter-man-pages-and-refer-to-them-in-tc.8.patch
Patch48:            0049-xfrm-add-command-for-configuring-SPD-hash-table.patch
Patch49:            0050-xfrm-revise-man-page-and-document-ip-xfrm-policy-set.patch
Patch50:            0051-iplink-update-available-type-list.patch
Patch51:            0052-iplink-add-support-for-bonding-netlink.patch
Patch52:            0053-iproute2-finish-support-for-bonding-attributes.patch
Patch53:            0054-introduce-support-for-slave-info-data.patch
Patch54:            0055-iplink-add-support-for-bonding-slave.patch
Patch55:            0056-iplink_bond-fix-arp_all_targets-parameter-name-in-ou.patch
Patch56:            0057-iplink_bond-fix-parameter-value-matching.patch
Patch57:            0058-iplink_bond_slave-show-mii_status-only-once.patch
Patch58:            0059-iplink-can-fix-help-text-and-man-page.patch
Patch59:            0060-ip-add-nlmon-as-a-device-type-to-help-message.patch
Patch60:            0061-iproute2-allow-to-change-slave-options-via-type_slav.patch
Patch61:            0062-add-help-command-to-bonding-master.patch
Patch62:            0063-ip-link-Shortify-printing-the-usage-of-link-type.patch
Patch63:            0064-iplink_bond-add-support-for-ad_actor-and-port_key-op.patch
Patch64:            0065-bonding-export-3ad-actor-and-partner-port-state.patch
Patch65:            0066-iplink-bonding-add-support-for-IFLA_BOND_TLB_DYNAMIC.patch
Patch66:            0067-bond-fix-return-after-invarg.patch
Patch67:            0068-ip-link-missing-options-in-bond-usage.patch
Patch68:            0069-ip-remove-extra-newlines-at-end-of-file.patch
Patch69:            0070-iplink-bond_slave-fix-ad_actor-partner_oper_port_sta.patch
Patch70:            0071-add-bridge_slave-device-support.patch
Patch71:            0072-add-bridge-master-device-support.patch
Patch72:            0073-iplink_bridge-add-support-for-ageing_time.patch
Patch73:            0074-iplink_bridge-add-support-for-stp_state.patch
Patch74:            0075-iplink_bridge-add-support-for-priority.patch
Patch75:            0076-iplink-use-the-short-format-to-print-help-info.patch
Patch76:            0077-iplink-shortify-printing-the-usage-of-link-type.patch
Patch77:            0078-iplink-add-ageing_time-stp_state-and-priority-for-br.patch
Patch78:            0079-ip-link-consolidate-macvlan-and-macvtap.patch
Patch79:            0080-ip-macvlan-support-MACVLAN_FLAG_NOPROMISC-flag.patch
Patch80:            0081-iproute2-ip6gre-update-man-pages.patch
Patch81:            0082-iproute-Descriptions-of-fou-and-gue-options-in-ip-li.patch
Patch82:            0083-ip-link-Document-IPoIB-link-type-in-the-man-page.patch
Patch83:            0084-iproute2-ip-link.8.in-Spelling-fixes.patch
Patch84:            0085-man-ip-link-Add-missing-link-types-vti-ipvlan-nlmon.patch
Patch85:            0086-man-ip-link-fix-a-typo.patch
Patch86:            0087-man-ip-link-document-MACVLAN-MACVTAP-interface-types.patch
Patch87:            0088-iplink-macvtap-fix-man-page.patch
Patch88:            0089-iprule-Align-help-text-with-man-page-synopsis.patch
Patch89:            0090-ipl2tp-Print-help-even-on-systems-without-l2tp-suppo.patch
Patch90:            0091-ip-align-help-text-with-manpage.patch
Patch91:            0092-ipaddrlabel-Improve-help-text-precision.patch
Patch92:            0093-iplink-fix-help-text-syntax.patch
Patch93:            0094-ipneigh-add-missing-proxy-keyword-to-help-text.patch
Patch94:            0095-ipntable-Fix-typo-in-help-text.patch
Patch95:            0096-iproute-TYPE-keyword-is-not-optional-fix-help-text-a.patch
Patch96:            0097-iprule-add-missing-nat-keyword-to-help-text.patch
Patch97:            0098-man-ip-address.8-Minor-syntax-fixes.patch
Patch98:            0099-man-ip-link.8-minor-font-fix.patch
Patch99:            0100-man-ip-link.8-Fix-and-improve-synopsis.patch
Patch100:           0101-man-ip-neighbour-Fix-for-missing-NUD_STATE-descripti.patch
Patch101:           0102-man-ip-netns.8-Clarify-synopsis-a-bit.patch
Patch102:           0103-man-ip-ntable.8-Review-synopsis-section.patch
Patch103:           0104-man-ip-rule.8-Review-synopsis-section.patch
Patch104:           0105-man-ip-token.8-Review-synopsis-section.patch
Patch105:           0106-add-vti-vti6-tunnel-modes-to-ip-tunnel-manual-page.patch
Patch106:           0107-man-ip-tunnel.8-Document-missing-6rd-action.patch
Patch107:           0108-man-ip-xfrm.8-Document-missing-parameters.patch
Patch108:           0109-man-ip-add-h-uman-readable-option.patch
Patch109:           0110-man-ip.8-Add-missing-flags-and-token-subcommand-desc.patch
Patch110:           0111-man-ip-l2tp.8-Fix-BNF-syntax.patch
Patch111:           0112-fix-spelling-of-Kuznetsov.patch
Patch112:           0113-man-Spelling-fixes.patch
Patch113:           0114-man-tc-htb-Fix-HRB-HTB-typo.patch
Patch114:           0115-TBF-man-page-fix-tbf-is-not-classless.patch
Patch115:           0116-man8-scrub-trailing-whitespace.patch
Patch116:           0117-man-ip-.8-drop-any-reference-to-generic-ip-options.patch
Patch117:           0118-fix-indentation-of-ip-neighbour-man-page.patch
Patch118:           0119-man-ip-neighbour.8-Document-all-known-nud-states.patch
Patch119:           0120-libnetlink-Double-the-dump-buffer-size.patch
Patch120:           0121-man-ip-link-Beef-up-VXLAN-csum-options-a-bit.patch
Patch121:           0122-fix-print_ipt-segfault-if-more-then-one-filter-with-.patch
Patch122:           0123-man-rtpr-add-minimal-manpage.patch
Patch123:           0124-tc-introduce-simple-action.patch
Patch124:           0125-simple-print-newline.patch
Patch125:           0126-tc-minor-spelling-fixes.patch
Patch126:           0127-whitespace-cleanup.patch
Patch127:           0128-tc-fix-compilation-warning-on-32bits-arch.patch
Patch128:           0129-man-Add-a-man-page-for-the-csum-action.patch
Patch129:           0130-man-Add-a-man-page-for-the-mirred-action.patch
Patch130:           0131-man-Add-a-man-page-for-the-nat-action.patch
Patch131:           0132-man-Add-a-man-page-for-the-pedit-action.patch
Patch132:           0133-man-Add-a-man-page-for-the-police-action.patch
Patch133:           0134-man-Add-a-man-page-for-the-simple-action.patch
Patch134:           0135-man-Add-a-man-page-for-the-skbedit-action.patch
Patch135:           0136-man-Add-a-man-page-for-the-xt-action.patch
Patch136:           0137-man-tc-u32-Minor-syntax-fix.patch
Patch137:           0138-tc-pedit-document-branch-control-in-help-output.patch
Patch138:           0139-tc-connmark-pedit-Rename-BRANCH-to-CONTROL.patch
Patch139:           0140-man-tc-csum.8-Add-an-example.patch
Patch140:           0141-man-tc-mirred.8-Reword-man-page-a-bit-add-generic-mi.patch
Patch141:           0142-man-tc-police.8-Emphasize-on-the-two-rate-control-me.patch
Patch142:           0143-man-tc-skbedit.8-Elaborate-a-bit-on-TX-queues.patch
Patch143:           0144-man-ship-action-man-pages.patch
Patch144:           0145-doc-Add-my-article-about-tc-filters-and-actions.patch
Patch145:           0146-doc-tc-filters.tex-Drop-overly-subjective-paragraphs.patch
Patch146:           0147-ss-Fix-wrong-filter-behaviour.patch
Patch147:           0148-ss-Drop-silly-assignment.patch
Patch148:           0149-ss-Fix-accidental-state-filter-override.patch
Patch149:           0150-ip-enable-configuring-multicast-group-autojoin.patch
Patch150:           0151-man-ip-ip-link-Fix-ip-option-location.patch
Patch151:           0152-ip-link-Allow-to-filter-devices-by-master-dev.patch
Patch152:           0153-ip-link-Show-devices-by-type.patch
Patch153:           0154-man-ip-link-Small-example-of-ip-link-show-master.patch
Patch154:           0155-ipaddress-Allow-listing-addresses-by-type.patch
Patch155:           0156-add-new-IFLA_VF_TRUST-netlink-attribute.patch
Patch156:           0157-iplink-Support-VF-Trust.patch
Patch157:           0158-ip-link-Support-printing-VF-trust-setting.patch
Patch158:           0159-man-ip-link.8-Fix-ip-link-delete-description.patch
Patch159:           0160-man-ip-address-ip-link-Document-type-quirk.patch
Patch160:           0161-iproute2-GENEVE-support.patch
Patch161:           0162-iproute2-update-ip-link.8-for-geneve-tunnels.patch
Patch162:           0163-iplink_geneve-add-ttl-configuration-at-link-creation.patch
Patch163:           0164-iplink_geneve-add-tos-configuration-at-link-creation.patch
Patch164:           0165-geneve-add-support-for-IPv6-link-partners.patch
Patch165:           0166-geneve-add-support-for-lwt-tunnel-creation-and-dst-p.patch
Patch166:           0167-geneve-Add-support-for-configuring-UDP-checksums.patch
Patch167:           0168-geneve-add-support-to-set-flow-label.patch
Patch168:           0169-geneve-fix-IPv6-remote-address-reporting.patch
Patch169:           0170-iproute2-utils-change-hexstring_n2a-and-hexstring_a2.patch
Patch170:           0171-iproute2-arpd-use-ll_addr_a2n-and-ll_addr_n2a.patch
Patch171:           0172-lib-ll_addr-improve-ll_addr_n2a-a-bit.patch
Patch172:           0173-utils-make-hexstring_a2n-provide-the-number-of-hex-d.patch
Patch173:           0174-utils-add-get_be-16-32-64-use-them-where-possible.patch
Patch174:           0175-utils-provide-get_hex-to-read-a-hex-digit-from-a-cha.patch
Patch175:           0176-ip-add-MACsec-support.patch
Patch176:           0177-utils-fix-hex-digits-parsing-in-hexstring_a2n.patch
Patch177:           0178-RH-INTERNAL-update-kernel-headers-to-v4.6.0.patch
Patch178:           0179-add-if_macsec-header.patch
Patch179:           0180-configure-Add-check-for-the-doc-tools.patch
Patch180:           0181-configure-Check-for-libmnl.patch
Patch181:           0182-configure-cleanup.patch
Patch182:           0183-include-add-linked-list-implementation-from-kernel.patch
Patch183:           0184-add-devlink-tool.patch
Patch184:           0185-devlink-ignore-build-result.patch
Patch185:           0186-devlink-fix-devlink-port-help-message.patch
Patch186:           0187-list-add-list_for_each_entry_reverse-macro.patch
Patch187:           0188-list-add-list_add_tail-helper.patch
Patch188:           0189-devlink-introduce-pr_out_port_handle-helper.patch
Patch189:           0190-devlink-introduce-helper-to-print-out-nice-names-ifn.patch
Patch190:           0191-devlink-split-dl_argv_parse_put-to-parse-and-put-par.patch
Patch191:           0192-devlink-introduce-dump-filtering-function.patch
Patch192:           0193-devlink-allow-to-parse-both-devlink-and-port-handle-.patch
Patch193:           0194-devlink-implement-shared-buffer-support.patch
Patch194:           0195-devlink-implement-shared-buffer-occupancy-control.patch
Patch195:           0196-devlink-add-manpage-for-shared-buffer.patch
Patch196:           0197-ip-route-restore-route-entries-in-correct-order.patch
Patch197:           0198-iproute-constify-rtattr_cmp.patch
Patch198:           0199-ip-link-Add-group-in-usage-for-ip-link-delete.patch
Patch199:           0200-iplink-List-valid-type-argument-in-ip-link-help-text.patch
Patch200:           0201-iplink-bond_slave-Add-missing-help-functions.patch
Patch201:           0202-man-ip-link-Add-deleting-links-by-group.patch
Patch202:           0203-man-ip-link-Add-short-description-about-group.patch
Patch203:           0204-man-ip-link-Remove-extra-GROUP-explanation.patch
Patch204:           0205-ip-link.8-Extend-type-list-in-synopsis.patch
Patch205:           0206-ip-link.8-Place-ip-link-set-warning-more-prominently.patch
Patch206:           0207-ip-link.8-Add-slave-type-option-descriptions.patch
Patch207:           0208-ip-link-fix-unterminated-string-in-manpage.patch
Patch208:           0209-vxlan-fix-help-and-man-text.patch
Patch209:           0210-ip-link-fix-man-page-warnings.patch
Patch210:           0211-ip-link.8-Fix-font-choices.patch
Patch211:           0212-ip-address.8-Document-autojoin-flag.patch
Patch212:           0213-route-allow-routes-to-be-configured-with-expire-valu.patch
Patch213:           0214-ip-route-timeout-for-routes-has-to-be-set-in-seconds.patch
Patch214:           0215-iproute2-ip-route.8.in-Add-expires-option-for-ip-rou.patch
Patch215:           0216-ipneigh-List-all-nud-states-in-help-output.patch
Patch216:           0217-Document-VF-link-state-control-in-the-ip-link-man-pa.patch
Patch217:           0218-man-ip-link-Document-query_rss-option.patch
Patch218:           0219-Add-support-to-configure-SR-IOV-VF-minimum-and-maxim.patch
Patch219:           0220-ip-check-for-missing-dev-arg-when-doing-VF-rate.patch
Patch220:           0221-ip-link-Remove-unnecessary-device-checking.patch
Patch221:           0222-ip-link-Fix-crash-on-older-kernels-when-show-VF-dev.patch
Patch222:           0223-iplink-Add-missing-variable-initialization.patch
Patch223:           0224-iplink-Check-address-length-via-netlink.patch
Patch224:           0225-Fix-MAC-address-length-check.patch
Patch225:           0226-ip-add-paren-to-silence-warning.patch
Patch226:           0227-doc-man-ip-rule-Remove-incorrect-statement-about-rul.patch
Patch227:           0228-man-ip-link-ip-address-Drop-references-to-ipvlan.patch
Patch228:           0229-man-ip-link-Drop-fou-and-gue-related-documentation.patch
Patch229:           0230-Revert-ip-fix-exit-code-for-rule-failures.patch
Patch230:           0231-Revert-ip-return-correct-exit-code-on-route-failure.patch
Patch231:           0232-Revert-link-dump-filter.patch
Patch232:           0233-Revert-ip-fix-exit-code-for-addrlabel.patch
Patch233:           0234-Revert-fix-ip-force-batch-to-continue-on-errors.patch
Patch234:           0235-Revert-Allow-specifying-bridge-port-STP-state-by-nam.patch
Patch235:           0236-man-macsec-fix-macsec-related-typos.patch
Patch236:           0237-ip-link-address-add-macsec-item-to-TYPE-list.patch
Patch237:           0238-macsec-cipher-and-icvlen-can-be-set-separately.patch
Patch238:           0239-man-ip-link.8-Document-missing-geneve-options.patch
Patch239:           0240-ip-link-add-missing-min-max-_tx_rate-to-help-text.patch
Patch240:           0241-ip-route-restore_handler-should-check-tb-RTA_PREFSRC.patch
License:            GPLv2+ and Public Domain
BuildRequires:      bison
BuildRequires:      flex
BuildRequires:      iptables-devel >= 1.4.5
BuildRequires:      libdb-devel
BuildRequires:      libmnl-devel
BuildRequires:      libselinux-devel
BuildRequires:      linuxdoc-tools
BuildRequires:      pkgconfig
BuildRequires:      psutils
BuildRequires:      tex(cm-super-t1.enc)
BuildRequires:      tex(dvips)
BuildRequires:      tex(ecrm1000.tfm)
BuildRequires:      tex(latex)
BuildRequires:      tex(fullpage.sty)
%if 0%{?fedora}
BuildRequires:      linux-atm-libs-devel
%endif
# For the UsrMove transition period
Conflicts:          filesystem < 3
Provides:           /sbin/ip

%description
The iproute package contains networking utilities (ip and rtmon, for example)
which are designed to use the advanced networking capabilities of the Linux
2.4.x and 2.6.x kernel.

%package doc
Summary:            ip and tc documentation with examples
Group:              Applications/System
License:            GPLv2+

%description doc
The iproute documentation contains howtos and examples of settings.

%package devel
Summary:            iproute development files
Group:              Development/Libraries
License:            GPLv2+
Provides:           iproute-static = %{version}-%{release}

%description devel
The libnetlink static library.

%prep
%setup -q -n %{name}-%{version}-%{baserelease}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1
%patch129 -p1
%patch130 -p1
%patch131 -p1
%patch132 -p1
%patch133 -p1
%patch134 -p1
%patch135 -p1
%patch136 -p1
%patch137 -p1
%patch138 -p1
%patch139 -p1
%patch140 -p1
%patch141 -p1
%patch142 -p1
%patch143 -p1
%patch144 -p1
%patch145 -p1
%patch146 -p1
%patch147 -p1
%patch148 -p1
%patch149 -p1
%patch150 -p1
%patch151 -p1
%patch152 -p1
%patch153 -p1
%patch154 -p1
%patch155 -p1
%patch156 -p1
%patch157 -p1
%patch158 -p1
%patch159 -p1
%patch160 -p1
%patch161 -p1
%patch162 -p1
%patch163 -p1
%patch164 -p1
%patch165 -p1
%patch166 -p1
%patch167 -p1
%patch168 -p1
%patch169 -p1
%patch170 -p1
%patch171 -p1
%patch172 -p1
%patch173 -p1
%patch174 -p1
%patch175 -p1
%patch176 -p1
%patch177 -p1
%patch178 -p1
%patch179 -p1
%patch180 -p1
%patch181 -p1
%patch182 -p1
%patch183 -p1
%patch184 -p1
%patch185 -p1
%patch186 -p1
%patch187 -p1
%patch188 -p1
%patch189 -p1
%patch190 -p1
%patch191 -p1
%patch192 -p1
%patch193 -p1
%patch194 -p1
%patch195 -p1
%patch196 -p1
%patch197 -p1
%patch198 -p1
%patch199 -p1
%patch200 -p1
%patch201 -p1
%patch202 -p1
%patch203 -p1
%patch204 -p1
%patch205 -p1
%patch206 -p1
%patch207 -p1
%patch208 -p1
%patch209 -p1
%patch210 -p1
%patch211 -p1
%patch212 -p1
%patch213 -p1
%patch214 -p1
%patch215 -p1
%patch216 -p1
%patch217 -p1
%patch218 -p1
%patch219 -p1
%patch220 -p1
%patch221 -p1
%patch222 -p1
%patch223 -p1
%patch224 -p1
%patch225 -p1
%patch226 -p1
%patch227 -p1
%patch228 -p1
%patch229 -p1
%patch230 -p1
%patch231 -p1
%patch232 -p1
%patch233 -p1
%patch234 -p1
%patch235 -p1
%patch236 -p1
%patch237 -p1
%patch238 -p1
%patch239 -p1
%patch240 -p1
sed -i 's/iproute-doc/%{name}-%{version}/' man/man8/lnstat.8

%build
export LIBDIR=/%{_libdir}
export IPT_LIB_DIR=/%{_lib}/xtables
export CFLAGS="${CFLAGS:-%optflags}"
./configure
make %{?_smp_mflags}
make -C doc

%install
mkdir -p \
    %{buildroot}%{_includedir} \
    %{buildroot}%{_sbindir} \
    %{buildroot}%{_mandir}/man3 \
    %{buildroot}%{_mandir}/man7 \
    %{buildroot}%{_mandir}/man8 \
    %{buildroot}%{_libdir}/tc \
    %{buildroot}%{_sysconfdir}/iproute2 \
    %{buildroot}%{_sysconfdir}/sysconfig/cbq

for binary in \
    bridge/bridge \
    devlink/devlink \
    examples/cbq.init-%{cbq_version} \
    genl/genl \
    ip/ifcfg \
    ip/ip \
    ip/routef \
    ip/routel \
    ip/rtmon \
    ip/rtpr \
    misc/arpd \
    misc/ifstat \
    misc/lnstat \
    misc/nstat \
    misc/rtacct \
    misc/ss \
    tc/tc
    do install -m755 ${binary} %{buildroot}%{_sbindir}
done
mv %{buildroot}%{_sbindir}/cbq.init-%{cbq_version} %{buildroot}%{_sbindir}/cbq
cd %{buildroot}%{_sbindir}
    ln -s lnstat ctstat
    ln -s lnstat rtstat
cd -

# Libs
install -m644 netem/*.dist %{buildroot}%{_libdir}/tc
%if 0%{?fedora}
install -m755 tc/q_atm.so %{buildroot}%{_libdir}/tc
%endif
install -m755 tc/m_xt.so %{buildroot}%{_libdir}/tc
cd %{buildroot}%{_libdir}/tc
    ln -s m_xt.so m_ipt.so
cd -

# libnetlink
install -m644 include/libnetlink.h %{buildroot}%{_includedir}
install -m644 lib/libnetlink.a %{buildroot}%{_libdir}

# Manpages
iconv -f latin1 -t utf8 man/man8/ss.8 > man/man8/ss.8.utf8 &&
    mv man/man8/ss.8.utf8 man/man8/ss.8
install -m644 man/man3/*.3 %{buildroot}%{_mandir}/man3
install -m644 man/man7/*.7 %{buildroot}%{_mandir}/man7
install -m644 man/man8/*.8 %{buildroot}%{_mandir}/man8
echo '.so man8/tc-cbq.8' > %{buildroot}%{_mandir}/man8/cbq.8

# Config files
install -m644 etc/iproute2/* %{buildroot}%{_sysconfdir}/iproute2
for config in \
    %{SOURCE1} \
    %{SOURCE2}
    do install -m644 ${config} %{buildroot}%{_sysconfdir}/sysconfig/cbq
done

%files
%dir %{_sysconfdir}/iproute2
%doc COPYING
%doc README README.decnet README.iproute2+tc README.distribution README.lnstat
%{_mandir}/man7/*
%{_mandir}/man8/*
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/iproute2/*
%{_sbindir}/*
%dir %{_libdir}/tc/
%{_libdir}/tc/*
%dir %{_sysconfdir}/sysconfig/cbq
%config(noreplace) %{_sysconfdir}/sysconfig/cbq/*

%files doc
%doc COPYING
%doc doc/*.ps
%doc examples

%files devel
%doc COPYING
%{_mandir}/man3/*
%{_libdir}/libnetlink.a
%{_includedir}/libnetlink.h

%changelog
* Thu Aug 25 2016 Phil Sutter <psutter@redhat.com> [3.10.0-74.el7]
- ip route: restore_handler should check tb[RTA_PREFSRC] for local networks (Phil Sutter) [1362728]

* Thu Aug 18 2016 Phil Sutter <psutter@redhat.com> [3.10.0-73.el7]
- ip-link: add missing {min,max}_tx_rate to help text (Phil Sutter) [1340914]
- man: ip-link.8: Document missing geneve options (Phil Sutter) [1339178]
- iproute.spec: Fix for missing cbq.8 man page (Phil Sutter) [1362551]

* Thu Aug 04 2016 Phil Sutter <psutter@redhat.com> [3.10.0-72.el7]
- macsec: cipher and icvlen can be set separately (Davide Caratti) [1354408]
- ip {link,address}: add 'macsec' item to TYPE list (Davide Caratti) [1354702]
- man: macsec: fix macsec related typos (Davide Caratti) [1354702 1354319]
- Revert "Allow specifying bridge port STP state by name rather than number." (Phil Sutter) [1288042]
- Revert "fix ip -force -batch to continue on errors" (Phil Sutter) [1288042]
- Revert "ip: fix exit code for addrlabel" (Phil Sutter) [1288042]
- Revert "link dump filter" (Phil Sutter) [1288042]
- Revert "ip: return correct exit code on route failure" (Phil Sutter) [1288042]
- Revert "ip: fix exit code for rule failures" (Phil Sutter) [1288042]
- man: ip-link: Drop fou and gue related documentation (Phil Sutter) [1013584]
- man: ip-link, ip-address: Drop references to ipvlan (Phil Sutter) [1013584]
- doc, man: ip-rule: Remove incorrect statement about rule 0 (Phil Sutter) [1362561]

* Sat Jul 30 2016 Phil Sutter <psutter@redhat.com> [3.10.0-71.el7]
- ip: add paren to silence warning (Phil Sutter) [1340914]
- Fix MAC address length check (Jakub Sitnicki) [1253767 1271580]
- iplink: Check address length via netlink (Jakub Sitnicki) [1253767 1271580]
- iplink: Add missing variable initialization (Jakub Sitnicki) [1253767 1271580]
- ip link: Fix crash on older kernels when show VF dev (Jakub Sitnicki) [1340914]
- ip link: Remove unnecessary device checking (Jakub Sitnicki) [1340914]
- ip: check for missing dev arg when doing VF rate (Jakub Sitnicki) [1340914]
- Add support to configure SR-IOV VF minimum and maximum Tx rate through ip tool (Jakub Sitnicki) [1340914]

* Fri Jul 22 2016 Phil Sutter <psutter@redhat.com> [3.10.0-70.el7]
- man: ip-link: Document query_rss option (Phil Sutter) [1264146]
- Document VF link state control in the ip-link man page (Phil Sutter) [1264146]
- ipneigh: List all nud states in help output (Phil Sutter) [1276661]
- iproute2: ip-route.8.in: Add expires option for ip route (Phil Sutter) [1357020]
- ip route: timeout for routes has to be set in seconds (Phil Sutter) [1357020]
- route: allow routes to be configured with expire values (Phil Sutter) [1357020]

* Wed Jul 20 2016 Phil Sutter <psutter@redhat.com> [3.10.0-69.el7]
- ip-address.8: Document autojoin flag (Phil Sutter) [1333513]
- ip-link.8: Fix font choices (Phil Sutter) [1269528]
- ip-link: fix man page warnings (Phil Sutter) [1269528]
- vxlan: fix help and man text (Phil Sutter) [1269528]
- ip-link: fix unterminated string in manpage (Phil Sutter) [1269528]
- ip-link.8: Add slave type option descriptions (Phil Sutter) [1269528]
- ip-link.8: Place 'ip link set' warning more prominently (Phil Sutter) [1269528]
- ip-link.8: Extend type list in synopsis (Phil Sutter) [1269528]
- man ip-link: Remove extra GROUP explanation (Phil Sutter) [1269528]
- man ip-link: Add short description about 'group' (Phil Sutter) [1269528]
- man ip-link: Add deleting links by group (Phil Sutter) [1269528]
- iplink: bond_slave: Add missing help functions (Phil Sutter) [1269528]
- iplink: List valid 'type' argument in ip link help text (Phil Sutter) [1269528]
- ip link: Add group in usage() for 'ip link delete' (Phil Sutter) [1269528]
- iproute: constify rtattr_cmp (Phil Sutter) [1348133]
- ip route: restore route entries in correct order (Phil Sutter) [1348133]

* Sat Jul 09 2016 Phil Sutter <psutter@redhat.com> [3.10.0-68.el7]
- devlink: add manpage for shared buffer (Phil Sutter) [1342515]
- devlink: implement shared buffer occupancy control (Phil Sutter) [1342515]
- devlink: implement shared buffer support (Phil Sutter) [1342515]
- devlink: allow to parse both devlink and port handle in the same time (Phil Sutter) [1342515]
- devlink: introduce dump filtering function (Phil Sutter) [1342515]
- devlink: split dl_argv_parse_put to parse and put parts (Phil Sutter) [1342515]
- devlink: introduce helper to print out nice names (ifnames) (Phil Sutter) [1342515]
- devlink: introduce pr_out_port_handle helper (Phil Sutter) [1342515]
- list: add list_add_tail helper (Phil Sutter) [1342515]
- list: add list_for_each_entry_reverse macro (Phil Sutter) [1342515]
- devlink: fix "devlink port" help message (Phil Sutter) [1342515]
- devlink: ignore build result (Phil Sutter) [1342515]
- add devlink tool (Phil Sutter) [1342515]
- include: add linked list implementation from kernel (Phil Sutter) [1342515]
- configure: cleanup (Phil Sutter) [1342515]
- configure: Check for libmnl (Phil Sutter) [1342515]
- configure: Add check for the doc tools (Phil Sutter) [1342515]
- add if_macsec header (Davide Caratti) [1300765]
- RH-INTERNAL: update kernel headers to v4.6.0 (Davide Caratti) [1300765]
- utils: fix hex digits parsing in hexstring_a2n() (Davide Caratti) [1300765]
- ip: add MACsec support (Davide Caratti) [1300765]
- utils: provide get_hex to read a hex digit from a char (Davide Caratti) [1300765]
- utils: add get_be{16, 32, 64}, use them where possible (Davide Caratti) [1300765]
- utils: make hexstring_a2n provide the number of hex digits parsed (Davide Caratti) [1300765]
- lib/ll_addr: improve ll_addr_n2a() a bit (Davide Caratti) [1300765]
- iproute2: arpd: use ll_addr_a2n and ll_addr_n2a (Davide Caratti) [1300765]
- iproute2: utils: change hexstring_n2a and hexstring_a2n to do not work with ":" (Davide Caratti) [1300765]

* Tue Jul 05 2016 Phil Sutter <psutter@redhat.com> [3.10.0-67.el7]
- geneve: fix IPv6 remote address reporting (Phil Sutter) [1339178]
- geneve: add support to set flow label (Phil Sutter) [1339178]
- geneve: Add support for configuring UDP checksums. (Phil Sutter) [1339178]
- geneve: add support for lwt tunnel creation and dst port selection (Phil Sutter) [1339178]
- geneve: add support for IPv6 link partners (Phil Sutter) [1339178]
- iplink_geneve: add tos configuration at link creation (Phil Sutter) [1339178]
- iplink_geneve: add ttl configuration at link creation (Phil Sutter) [1339178]
- iproute2: update ip-link.8 for geneve tunnels (Phil Sutter) [1339178]
- iproute2: GENEVE support (Phil Sutter) [1339178]
- man: ip-address, ip-link: Document 'type' quirk (Phil Sutter) [1341343]
- man: ip-link.8: Fix 'ip link delete' description (Phil Sutter) [1341343]

* Thu Jun 16 2016 Phil Sutter <psutter@redhat.com> [3.10.0-66.el7]
- ip-link: Support printing VF trust setting (Phil Sutter) [1302119]
- iplink: Support VF Trust (Phil Sutter) [1302119]
- add new IFLA_VF_TRUST netlink attribute (Phil Sutter) [1302119]
- ipaddress: Allow listing addresses by type (Phil Sutter) [1341343]
- man ip-link: Small example of 'ip link show master' (Phil Sutter) [1341343]
- ip link: Show devices by type (Phil Sutter) [1341343]
- ip link: Allow to filter devices by master dev (Phil Sutter) [1341343]

* Fri Jun 03 2016 Phil Sutter <psutter@redhat.com> [3.10.0-65.el7]
- man: ip, ip-link: Fix ip option location (Phil Sutter) [1251186]
- ip: enable configuring multicast group autojoin (Phil Sutter) [1333513]
- ss: Fix accidental state filter override (Phil Sutter) [1318005]
- ss: Drop silly assignment (Phil Sutter) [1318005]
- ss: Fix wrong filter behaviour (Phil Sutter) [1318005]

* Wed Mar 30 2016 Phil Sutter <psutter@redhat.com> [3.10.0-64.el7]
- Add missing build dependency to spec file (Phil Sutter) [1275426]

* Wed Mar 30 2016 Phil Sutter <psutter@redhat.com> [3.10.0-63.el7]
- doc/tc-filters.tex: Drop overly subjective paragraphs (Phil Sutter) [1275426]
- doc: Add my article about tc, filters and actions (Phil Sutter) [1275426]
- gitignore: Ignore 'doc' files generated at runtime (Phil Sutter) [1275426]
- tests: Add runtime generated files to .gitignore (Phil Sutter) [1275426]
- man: ship action man pages (Phil Sutter) [1275426]
- man: tc-skbedit.8: Elaborate a bit on TX queues (Phil Sutter) [1275426]
- man: tc-police.8: Emphasize on the two rate control mechanisms (Phil Sutter) [1275426]
- man: tc-mirred.8: Reword man page a bit, add generic mirror example (Phil Sutter) [1275426]
- man: tc-csum.8: Add an example (Phil Sutter) [1275426]
- tc: connmark, pedit: Rename BRANCH to CONTROL (Phil Sutter) [1275426]
- tc: pedit: document branch control in help output (Phil Sutter) [1275426]
- man: tc-u32: Minor syntax fix (Phil Sutter) [1275426]
- man: Add a man page for the xt action (Phil Sutter) [1275426]
- man: Add a man page for the skbedit action (Phil Sutter) [1275426]
- man: Add a man page for the simple action (Phil Sutter) [1275426]
- man: Add a man page for the police action (Phil Sutter) [1275426]
- man: Add a man page for the pedit action (Phil Sutter) [1275426]
- man: Add a man page for the nat action (Phil Sutter) [1275426]
- man: Add a man page for the mirred action (Phil Sutter) [1275426]
- man: Add a man page for the csum action. (Phil Sutter) [1275426]

* Wed Mar 23 2016 Phil Sutter <psutter@redhat.com> [3.10.0-62.el7]
- tc: fix compilation warning on 32bits arch (Phil Sutter) [1315930]
- whitespace cleanup (Phil Sutter) [1315930]
- tc: minor spelling fixes (Phil Sutter) [1315930]
- simple print newline (Phil Sutter) [1315930]
- tc: introduce simple action (Phil Sutter) [1315930]
- man: rtpr: add minimal manpage (Phil Sutter) [1316059]

* Tue Mar 08 2016 Phil Sutter <psutter@redhat.com> [3.10.0-61.el7]
- fix print_ipt: segfault if more then one filter with action -j MARK. (Phil Sutter) [1314403]
- man: ip-link: Beef up VXLAN csum options a bit (Phil Sutter) [1254625]
- libnetlink: Double the dump buffer size (Phil Sutter) [1304840]

* Mon Mar 07 2016 Phil Sutter <psutter@redhat.com> [3.10.0-60.el7]
- man: ip-neighbour.8: Document all known nud states (Phil Sutter) [1276661]
- fix indentation of ip neighbour man page (Phil Sutter) [1276661]
- man: ip-*.8: drop any reference to generic ip options (Phil Sutter) [1251186]
- man8: scrub trailing whitespace (Phil Sutter) [1251186]
- TBF man page fix (tbf is not classless) (Phil Sutter) [1251186]
- man tc-htb: Fix HRB -> HTB typo (Phil Sutter) [1251186]
- man: Spelling fixes (Phil Sutter) [1251186]
- fix spelling of Kuznetsov (Phil Sutter) [1251186]
- man: ip-l2tp.8: Fix BNF syntax (Phil Sutter) [1251186]
- man: ip.8: Add missing flags and token subcommand description (Phil Sutter) [1251186]
- man: ip: add -h[uman-readable] option (Phil Sutter) [1251186]
- man: ip-xfrm.8: Document missing parameters (Phil Sutter) [1251186]
- man: ip-tunnel.8: Document missing 6rd action (Phil Sutter) [1251186]
- add 'vti'/'vti6' tunnel modes to ip-tunnel manual page (Phil Sutter) [1251186]
- man: ip-token.8: Review synopsis section (Phil Sutter) [1251186]
- man: ip-rule.8: Review synopsis section (Phil Sutter) [1251186]
- man: ip-ntable.8: Review synopsis section (Phil Sutter) [1251186]
- man: ip-netns.8: Clarify synopsis a bit (Phil Sutter) [1251186]
- man: ip-neighbour: Fix for missing NUD_STATE description (Phil Sutter) [1251186]
- man: ip-link.8: Fix and improve synopsis (Phil Sutter) [1251186]
- man: ip-link.8: minor font fix (Phil Sutter) [1251186]
- man: ip-address.8: Minor syntax fixes (Phil Sutter) [1251186]
- iprule: add missing nat keyword to help text (Phil Sutter) [1251186]
- iproute: TYPE keyword is not optional, fix help text accordingly (Phil Sutter) [1251186]
- ipntable: Fix typo in help text (Phil Sutter) [1251186]
- ipneigh: add missing proxy keyword to help text (Phil Sutter) [1251186]
- iplink: fix help text syntax (Phil Sutter) [1251186]
- ipaddrlabel: Improve help text precision (Phil Sutter) [1251186]
- ip: align help text with manpage (Phil Sutter) [1251186]
- ipl2tp: Print help even on systems without l2tp support (Phil Sutter) [1251186]
- iprule: Align help text with man page synopsis (Phil Sutter) [1251186]
- iplink: macvtap: fix man page (Phil Sutter) [1013584]
- man: ip-link: document MACVLAN/MACVTAP interface types (Phil Sutter) [1013584]
- man: ip-link: fix a typo (Phil Sutter) [1013584]
- man ip-link: Add missing link types - vti,ipvlan,nlmon (Phil Sutter) [1013584]
- iproute2: ip-link.8.in: Spelling fixes (Phil Sutter) [1013584]
- ip-link: Document IPoIB link type in the man page (Phil Sutter) [1013584]
- iproute: Descriptions of fou and gue options in ip-link man pages (Phil Sutter) [1013584]
- iproute2: ip6gre: update man pages (Phil Sutter) [1013584]
- ip: macvlan: support MACVLAN_FLAG_NOPROMISC flag (Phil Sutter) [1013584]
- ip: link: consolidate macvlan and macvtap (Phil Sutter) [1013584]

* Wed Feb 24 2016 Phil Sutter <psutter@redhat.com> [3.10.0-59.el7]
- iplink: add ageing_time, stp_state and priority for bridge (Phil Sutter) [1270759]
- iplink: shortify printing the usage of link type (Phil Sutter) [1270759]
- iplink: use the short format to print help info (Phil Sutter) [1270759]
- iplink_bridge: add support for priority (Phil Sutter) [1270759]
- iplink_bridge: add support for stp_state (Phil Sutter) [1270759]
- iplink_bridge: add support for ageing_time (Phil Sutter) [1270759]
- add bridge master device support (Phil Sutter) [1270759]
- add bridge_slave device support (Phil Sutter) [1270759]
- iplink: bond_slave: fix ad_actor/partner_oper_port_state output (Phil Sutter) [1269528]
- ip: remove extra newlines at end-of-file (Phil Sutter) [1269528]
- ip link: missing options in bond usage (Phil Sutter) [1269528]
- bond: fix return after invarg (Phil Sutter) [1269528]
- iplink: bonding: add support for IFLA_BOND_TLB_DYNAMIC_LB (Phil Sutter) [1269528]
- bonding: export 3ad actor and partner port state (Phil Sutter) [1269528]
- iplink_bond: add support for ad_actor and port_key options (Phil Sutter) [1269528]
- ip link: Shortify printing the usage of link type (Phil Sutter) [1269528]
- add help command to bonding master (Phil Sutter) [1269528]
- iproute2: allow to change slave options via type_slave (Phil Sutter) [1269528]
- ip: add nlmon as a device type to help message (Phil Sutter) [1269528]
- iplink: can: fix help text and man page (Phil Sutter) [1269528]
- iplink_bond_slave: show mii_status only once (Phil Sutter) [1269528]
- iplink_bond: fix parameter value matching (Phil Sutter) [1269528]
- iplink_bond: fix arp_all_targets parameter name in output (Phil Sutter) [1269528]
- iplink: add support for bonding slave (Phil Sutter) [1269528]
- introduce support for slave info data (Phil Sutter) [1269528]
- iproute2: finish support for bonding attributes (Phil Sutter) [1269528]
- iplink: add support for bonding netlink (Phil Sutter) [1269528]
- iplink: update available type list (Phil Sutter) [1269528]
- xfrm: revise man page and document ip xfrm policy set (Phil Sutter) [1269528]
- xfrm: add command for configuring SPD hash table (Phil Sutter) [1212026]

* Thu Feb 18 2016 Phil Sutter <psutter@redhat.com> [3.10.0-58.el7]
- tc: ship filter man pages and refer to them in tc.8 (Phil Sutter) [1286711]
- tc: add a man page for u32 filter (Phil Sutter) [1286711]
- tc: add a man page for tcindex filter (Phil Sutter) [1286711]
- tc: add a man page for route filter (Phil Sutter) [1286711]
- tc: add a man page for fw filter (Phil Sutter) [1286711]
- tc: add a man page for flow filter (Phil Sutter) [1286711]
- tc: add a man page for cgroup filter (Phil Sutter) [1286711]
- tc: add a man page for basic filter (Phil Sutter) [1286711]
- batch: support quoted strings (Phil Sutter) [1272593]
- man: fix whatis for fq (Phil Sutter) [1261520]
- man: tc: add man page for fq pacer (Phil Sutter) [1261520]

* Thu Feb 18 2016 Phil Sutter <psutter@redhat.com> [3.10.0-57.el7]
- route: Fix printing of locked entries (Phil Sutter) [1291832]
- route: ignore RTAX_HOPLIMIT of value -1 (Phil Sutter) [1291832]
- ip-link: remove warning message (Phil Sutter) [1291832]
- ip: route: add congestion control metric (Phil Sutter) [1291832]
- ip route: enable per-route ecn settings via 'features' option (Phil Sutter) [1291832]
- iproute2: ip-route.8.in: minor fixes (Phil Sutter) [1291832]
- iproute: restrict hoplimit values to be in range [0; 255] (Phil Sutter) [1291832]
- man ss: Fix explanation when no options specified (Phil Sutter) [1291818]
- libnetlink: don't confuse variables in rtnl_talk() (Phil Sutter) [1288042]
- libnetlink: add size argument to rtnl_talk (Phil Sutter) [1288042]
- ip: fix exit code for rule failures (Phil Sutter) [1288042]
- ip: return correct exit code on route failure (Phil Sutter) [1288042]
- link dump filter (Phil Sutter) [1288042]
- ip: fix exit code for addrlabel (Phil Sutter) [1288042]
- fix ip -force -batch to continue on errors (Phil Sutter) [1288042]
- Allow specifying bridge port STP state by name rather than number. (Phil Sutter) [1288042]
- gre: raising the size of the buffer holding nl messages. (Phil Sutter) [1288042]
- neighbor: check return values (Phil Sutter) [1277094]
- ip-address: fix oneline mode for interfaces with VF (Phil Sutter) [1272405]
- ss: add support for segs_in and segs_out (Phil Sutter) [1269114]
- ss: add support for bytes_acked & bytes_received (Phil Sutter) [1269114]
- ss: return -1 if an unrecognized option was given (Phil Sutter) [1265238]
- man: ip-address: document mngtmpaddr and noprefixroute flags (Phil Sutter) [1231898]
- man: ip-address: align synopsis with help output (Phil Sutter) [1231898]
- ip-address.8.in: fix BNF syntax error (Phil Sutter) [1231898]
- ip-address: fix and extend documentation (Phil Sutter) [1231898]
- ip: extend "ip-address" man page to reflect the recent flag extensions (Phil Sutter) [1231898]
- ip: allow ip address show to list addresses with certain flags not being set (Phil Sutter) [1231898]
- bridge fdb: add 'use' option to set NTF_USE flag in fdb add requests (Phil Sutter) [1075692]
- bridge: drop man page fragment (Phil Sutter) [1075692]
- bridge: drop reference to unused option embedded from manpage (Phil Sutter) [1075692]

* Thu Feb 18 2016 Phil Sutter <psutter@redhat.com> [3.10.0-56.el7]
- ipaddress: fix ipaddr_flush for Linux >= 3.1 (Phil Sutter) [1291825]
- ipaddress: simplify ipaddr_flush() (Phil Sutter) [1291825]
- libnetlink: introduce nc_flags (Phil Sutter) [1291825]
- iproute2: Ignore EADDRNOTAVAIL errors during address flush operation (Phil Sutter) [1291825]
- lnstat: fix header displaying mechanism (Phil Sutter) [1263392]
- man: lnstat: rewrite manpage (Phil Sutter) [1269133]

* Wed Feb 17 2016 Phil Sutter <psutter@redhat.com> [3.10.0-55.el7]
- Resolves: #1290860 - Rework list of patches, replace by upstream backports

* Thu Sep 17 2015 Phil Sutter - 3.10.0-54
- Related: #1241486 - backport: tc: fq scheduler - add missing documentation

* Thu Sep 03 2015 Phil Sutter - 3.10.0-53
- Related: #1212026 - [6wind 7.2 Feat]: backport: ipxfrm: unable to configure
  SPD hash table - reverted this backport due to unmet dependencies

* Mon Aug 24 2015 Phil Sutter - 3.10.0-52
- Resolves: #1254095 - bridge: Add master device name to bridge fdb show
- Resolves: #1255316 - tc does not allow to attach pfifo_fast qdisc
- Related: #1251070 - Fix multiple programming errors in iproute package

* Sun Aug 16 2015 Phil Sutter - 3.10.0-51
- Resolves: bz#1251451 - can't change the remote/local address of tunnel
  interface to "any" in ipip mode
- Related: #1213869 - [6wind 7.2 Feat]: backport: iproute2: various netns
  features
- Related: #1215006 - [RFE] backport current version of the ss command
- Resolves: #1251070 - Fix multiple programming errors in iproute package
- Related: #1198456 - backport: dynamic precision, human readable, and IEC
  output to ip stats
- Related: #1210402 - [6wind 7.2 Feat]: backport: vxlan: unable to configure
  UDP checksums
- Related: #1213869 - [6wind 7.2 Feat]: backport: iproute2: various netns
  features

* Fri Aug 07 2015 Phil Sutter - 3.10.0-50
- Resolves: #1244851 - vti tunnel does not work
- Resolves: #1155116 - iproute2: implement "-d" option for "ip mon"

* Thu Aug 06 2015 Phil Sutter - 3.10.0-49
- Resolves: bz#1241486 - backport: tc: fq scheduler
- Related: #1215006 - backport current version of the ss command

* Wed Aug 05 2015 Phil Sutter - 3.10.0-48
- Related: #1215006 - backport current version of the ss command
- Resolves: #1247315 - Fix limitation in iproute/ss regarding dual-stack sockets

* Mon Aug 03 2015 Phil Sutter - 3.10.0-47
- Related: #1215006 - backport current version of the ss command
- Related: #1219280 - backport: iproute2: vti6 support

* Wed Jul 08 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-46
- Related: #1198456 - add missing parts

* Wed Jul 08 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-45
- Related: #1213869 - add support for 'ip -all netns'

* Wed Jul 08 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-44
- Related: #1176180 - put back addrgenmode docs

* Wed Jul 08 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-43
- Related: #1131928 - make netns docs consistent

* Wed Jul 08 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-42
- Resolves: #1169901 - ip rule help output contains action reject, but this
  action does not work

* Tue Jul 07 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-41
- Resolves: #1169874 - ip rule command allows to remove rule with priority 0

* Tue Jul 07 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-40
- Resolves: #1042802 - make 'ip -d monitor' consistent with 'ip -d link'

* Thu Jun 04 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-39
- Resolves: #1228166 - remove redundant libnl-devel build dependency

* Tue Jun 02 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-38
- Resolves: #1131473 - backport: implement -s option for ip a

* Tue Jun 02 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-37
- Resolves: #1213869 - backport: iproute2: unable to manage nsid

* Fri May 29 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-36
- Resolves: #1224970 - backport: ipv6: support noprefixroute and mngtmpaddr

* Thu May 28 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-35
- Related: #1198456 - refactor patchset thoroughly

* Mon May 25 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-34
- Resolves: #1176684 - backport: ip xfrm monitor all does not work

* Mon May 25 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-33
- Resolves: #1219280 - backport: iproute2: vti6 support

* Wed May 20 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-32
- Resolves: #1198489 - backport: "ip route del" without arguments should print
  help

* Thu May 14 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-31
- Resolves: #1218568 - backport: iproute2: query_rss command is missing

* Thu May 14 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-30
- Resolves: #1212026 - backport: ipxfrm: unable to configure SPD hash table

* Wed May 13 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-29
- Resolves: #1210402 - backport: vxlan: unable to configure UDP checksums

* Wed May 13 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-28
- Resolves: #1131928 - backport: introduce option to ip to operate on a
  different namespace

* Wed May 13 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-27
- Resolves: #1198456 - make sure the patch is applied

* Tue Apr 28 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-26
- Resolves: #1198456 - backport changes in link statistics

* Tue Apr 28 2015 Pavel Šimerda <psimerda@redhat.com>
- Resolves: #1139173 - ip -s xfrm state crashes with segfault

* Tue Apr 28 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-24
- Resolves: #1215006 - backport current version of the ss command

* Fri Apr 17 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-23
- Resolves: #1203646 - backport VXLAN-GBP

* Thu Apr 16 2015 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-22
- Resolves: #1176180 - ip -d link show: print addrgenmode

* Fri Oct 24 2014 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-21
- Related: #1119180 - improve addrgen documentation

* Fri Oct 24 2014 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-20
- Related: #1119180 - document addrgen

* Wed Oct 08 2014 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-19
- Resolves: #1081081 - lnstat man page references iproute-doc when it should
  reference iproute-<ver>

* Fri Oct 03 2014 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-18
- Resolves: #1044535 - tc: add cls_bpf frontend

* Fri Oct 03 2014 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-17
- Resolves: #1044535 - backport tc:

* Fri Oct 03 2014 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-16
- Resolves: #1091010 - [RFE] iproute2: Allow Configurable TCP Delayed Ack in
  RHEL

* Fri Oct 03 2014 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-15
- Resolves: #1100271 - ip -6 addrlabel return incorrect error message

* Fri Oct 03 2014 Pavel Šimerda <psimerda@redhat.com> - 3.10.0-14
- Resolves: #1119180 - iproute2: allow to ipv6 set address generation mode

* Tue Feb 25 2014 Petr Šabata <contyk@redhat.com> - 3.10.0-13
- Add VF link state control mechanisms (#1061593)

* Tue Feb 25 2014 Petr Šabata <contyk@redhat.com> - 3.10.0-12
- Add destination port and IPv6 support to VXLAN (#1067437)

* Wed Jan 29 2014 Petr Šabata <contyk@redhat.com> - 3.10.0-11
- Don't hang on rtnl_send() failure (#1040454)
- Add the dstport option to vxlan (#1039855)

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.10.0-10
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.10.0-9
- Mass rebuild 2013-12-27

* Tue Nov 26 2013 Petr Šabata <contyk@redhat.com> - 3.10.0-8
- Document fdb replace and embedded bridge options (#1024697)

* Fri Nov 22 2013 Petr Šabata <contyk@redhat.com> - 3.10.0-7
- Fix the rtt time values (#1032501)

* Fri Nov 08 2013 Petr Šabata <contyk@redhat.com> - 3.10.0-6
- Fix lnstat -i (#1024426)
- Support IPv6 peer addresses (#1017228)
- Add the replace command to bridge fdb (#1024697)
- Document link type vlan (#979326)

* Tue Oct 01 2013 Petr Pisar <ppisar@redhat.com> - 3.10.0-5
- Close file with bridge monitor file (#1011818)

* Tue Sep 24 2013 Petr Pisar <ppisar@redhat.com> - 3.10.0-4
- Document tc -OK option (#977844)
- Document "bridge mdb" and "bridge monitor mdb" (#1009860)

* Wed Sep 18 2013 Marcela Mašláňová <mmaslano@redhat.com> - 3.10.0-3
- Add '-OK' command line option to tc telling it to write an "OK\n" to stdout
- rhbz#977844

* Mon Aug 05 2013 Petr Šabata <contyk@redhat.com> - 3.10.0-2.1
- Add a skeleton manpages for genl and ifstat (#881180)

* Wed Jul 17 2013 Petr Šabata <contyk@redhat.com> - 3.10.0-2
- Fix the XFRM patch

* Wed Jul 17 2013 Petr Šabata <contyk@redhat.com> - 3.10.0-1
- 3.10.0 bump
- Drop the SHAREDIR patch and revert to upstream ways (#966445)
- Fix an XFRM regression with FORTIFY_SOURCE

* Tue Apr 30 2013 Petr Šabata <contyk@redhat.com> - 3.9.0-1
- 3.9.0 bump

* Thu Apr 25 2013 Petr Šabata <contyk@redhat.com> - 3.8.0-4
- ATM is available in Fedora only

* Tue Mar 12 2013 Petr Šabata <contyk@redhat.com> - 3.8.0-3
- Mention the "up" argument in documentation and help outputs (#907468)

* Mon Mar 04 2013 Petr Šabata <contyk@redhat.com> - 3.8.0-2
- Bump for 1.4.18 rebuild

* Tue Feb 26 2013 Petr Šabata <contyk@redhat.com> - 3.8.0-1
- 3.8.0 bump

* Fri Feb 08 2013 Petr Šabata <contyk@redhat.com> - 3.7.0-2
- Don't propogate mounts out of ip (#882047)

* Wed Dec 12 2012 Petr Šabata <contyk@redhat.com> - 3.7.0-1
- 3.7.0 bump

* Mon Nov 19 2012 Petr Šabata <contyk@redhat.com> - 3.6.0-3
- Include section 7 manpages (#876857)
- Fix ancient bogus dates in the changelog (correction based upon commits)
- Explicitly require some TeX fonts no longer present in the base distribution

* Thu Oct 04 2012 Petr Šabata <contyk@redhat.com> - 3.6.0-2
- List all interfaces by default

* Wed Oct 03 2012 Petr Šabata <contyk@redhat.com> - 3.6.0-1
- 3.6.0 bump

* Thu Aug 30 2012 Petr Šabata <contyk@redhat.com> - 3.5.1-2
- Remove the explicit iptables dependency (#852840)

* Tue Aug 14 2012 Petr Šabata <contyk@redhat.com> - 3.5.1-1
- 3.5.1 bugfix release bump
- Rename 'br' to 'bridge'

* Mon Aug 06 2012 Petr Šabata <contyk@redhat.com> - 3.5.0-2
- Install the new bridge utility

* Thu Aug 02 2012 Petr Šabata <contyk@redhat.com> - 3.5.0-1
- 3.5.0 bump
- Move to db5.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 22 2012 Petr Šabata <contyk@redhat.com> - 3.4.0-1
- 3.4.0 bump
- Drop the print route patch (included upstream)

* Mon Apr 30 2012 Petr Šabata <contyk@redhat.com> - 3.3.0-2
- Let's install rtmon too... (#814819)

* Thu Mar 22 2012 Petr Šabata <contyk@redhat.com> - 3.3.0-1
- 3.3.0 bump
- Update source URL

* Mon Feb 27 2012 Petr Šabata <contyk@redhat.com> - 3.2.0-3
- Address dangerous /tmp files security issue (CVE-2012-1088, #797881, #797878)

* Fri Jan 27 2012 Petr Šabata <contyk@redhat.com> - 3.2.0-2
- Simplify the spec a bit thanks to the UsrMove feature

* Fri Jan 06 2012 Petr Šabata <contyk@redhat.com> - 3.2.0-1
- 3.2.0 bump
- Removing a useless, now conflicting patch (initcwnd already decumented)

* Thu Nov 24 2011 Petr Šabata <contyk@redhat.com> - 3.1.0-1
- 3.1.0 bump
- Point URL and Source to the new location on kernel.org
- Remove now obsolete defattr
- Dropping various patches now included upstream
- Dropping iproute2-2.6.25-segfault.patch; I fail to understand the reason for
  this hack

* Tue Nov 15 2011 Petr Šabata <contyk@redhat.com> - 2.6.39-6
- ss -ul should display UDP CLOSED sockets (#691100)

* Thu Oct 06 2011 Petr Sabata <contyk@redhat.com> - 2.6.39-5
- Fix ss, lnstat and arpd usage and manpages

* Wed Sep 07 2011 Petr Sabata <contyk@redhat.com> - 2.6.39-4
- lnstat should dump (-d) to stdout instead of stderr (#736332)

* Tue Jul 26 2011 Petr Sabata <contyk@redhat.com> - 2.6.39-3
- Rebuild for xtables7

* Tue Jul 12 2011 Petr Sabata <contyk@redhat.com> - 2.6.39-2
- Rebuild for xtables6

* Thu Jun 30 2011 Petr Sabata <contyk@redhat.com> - 2.6.39-1
- 2.6.39 bump

* Wed Apr 27 2011 Petr Sabata <psabata@redhat.com> - 2.6.38.1-4
- Link [cr]tstat to lnstat

* Wed Apr 27 2011 Petr Sabata <psabata@redhat.com> - 2.6.38.1-3
- Install ctstat, rtstat and routef manpage symlinks
- Install m_xt & m_ipt tc modules
- Creating devel and virtual static subpackages with libnetlink

* Thu Apr 21 2011 Petr Sabata <psabata@redhat.com> - 2.6.38.1-2
- General cleanup
- Use global instead of define
- Buildroot removal
- Correcting URL and Source links
- Install genl, ifstat, routef, routel and rtpr (rhbz#697319)

* Fri Mar 18 2011 Petr Sabata <psabata@redhat.com> - 2.6.38.1-1
- 2.6.38.1 bump

* Wed Mar 16 2011 Petr Sabata <psabata@redhat.com> - 2.6.38-1
- 2.6.38 bump

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Petr Sabata <psabata@redhat.com> - 2.6.37-2
- man-pages.patch update, ip(8) TYPE whitespace

* Mon Jan 10 2011 Petr Sabata <psabata@redhat.com> - 2.6.37-1
- 2.6.37 upstream release
- ss(8) improvements patch removed (included upstream)

* Wed Dec 08 2010 Petr Sabata <psabata@redhat.com> - 2.6.35-10
- fix a typo in ss(8) improvements patch, rhbz#661267

* Tue Nov 30 2010 Petr Sabata <psabata@redhat.com> - 2.6.35-9
- ss(8) improvements patch by jpopelka; should be included in 2.6.36

* Tue Nov 09 2010 Petr Sabata <psabata@redhat.com> - 2.6.35-8
- rhbz#641599, use the versioned path, man-pages.patch update, prep update

* Tue Oct 12 2010 Petr Sabata <psabata@redhat.com> - 2.6.35-7
- Do not segfault if peer name is omitted when creating a peer veth link, rhbz#642322

* Mon Oct 11 2010 Petr Sabata <psabata@redhat.com> - 2.6.35-6
- Man-pages update, rhbz#641599

* Wed Sep 29 2010 jkeating - 2.6.35-5
- Rebuilt for gcc bug 634757

* Tue Sep 21 2010 Petr Sabata <psabata@redhat.com> - 2.6.35-4
- Modified man-pages.patch to fix cbq manpage, rhbz#635877

* Tue Sep 21 2010 Petr Sabata <psabata@redhat.com> - 2.6.35-3
- Don't print routes with negative metric fix, rhbz#628739

* Wed Aug 18 2010 Petr Sabata <psabata@redhat.com> - 2.6.35-2
- 'ip route get' fix, iproute2-2.6.35-print-route.patch
- rhbz#622782

* Thu Aug 05 2010 Petr Sabata <psabata@redhat.com> - 2.6.35-1
- 2.6.35 version bump
- iproute2-tc-priority.patch removed (included in upstream now)

* Thu Jul 08 2010 Petr Sabata <psabata@redhat.com> - 2.6.34-5
- Licensing guidelines compliance fix

* Wed Jul 07 2010 Petr Sabata <psabata@redhat.com> - 2.6.34-4
- Requires: iptables >= 1.4.5, BuildRequires: iptables-devel >= 1.4.5

* Thu Jul 01 2010 Petr Sabata <psabata@redhat.com> - 2.6.34-3
- Build now runs ./configure to regenerate Makefile for ipt/xt detection

* Mon Jun 21 2010 Petr Sabata <psabata@redhat.com> - 2.6.34-2
- iproute-tc-priority.patch, rhbz#586112

* Mon Jun 21 2010 Petr Sabata <psabata@redhat.com> - 2.6.34-1
- 2.6.34 version bump

* Tue Apr 20 2010 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.33-2
- 578729 6rd tunnel correctly 3979ef91de9ed17d21672aaaefd6c228485135a2
- change BR texlive to tex according to guidelines

* Thu Feb 25 2010 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.33-1
- update

* Tue Jan 26 2010 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.32-2
- add macvlan aka VESA support d63a9b2b1e4e3eab0d0577d0a0f412d50be1e0a7
- kernel headers 2.6.33 ab322673298bd0b8927cdd9d11f3d36af5941b93
  are needed for macvlan features and probably for other added later.
- fix number of release which contains 2.6.32 kernel headers and features
  but it was released as 2.6.31

* Mon Jan  4 2010 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.31-1
- update to 2.6.31

* Fri Nov 27 2009 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.29-5.1.20091106gita7a9ddbb
- 539232 patch cbq initscript

* Fri Nov 27 2009 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.29-5.0.20091106gita7a9ddbb
- snapshot with kernel headers for 2.6.32

* Fri Oct  9 2009 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.29-5.0.20091009gitdaf49fd6
- new official version isn't available but it's needed -> switch to git snapshots

* Thu Sep 24 2009 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.29-5
- create missing man pages

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 23 2009 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.29-3
- new iptables (xtables) bring problems to tc, when ipt is used. 
  rhbz#497344 still broken. tc_modules.patch brings correct paths to
  xtables, but that doesn't fix whole issue.
- 497355 ip should allow creation of an IPsec SA with 'proto any' 
  and specified sport and dport as selectors

* Tue Apr 14 2009 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.29-2
- c3651bf4763d7247e3edd4e20526a85de459041b ip6tunnel: Fix no default 
 display of ip4ip6 tunnels
- e48f73d6a5e90d2f883e15ccedf4f53d26bb6e74 missing arpd directory

* Wed Mar 25 2009 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.29-1
- update to 2.6.29
- remove DDR patch which became part of sourc
- add patch with correct headers 1957a322c9932e1a1d2ca1fd37ce4b335ceb7113

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb  4 2009 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.28-2
- 483484 install distribution files into /usr/share and also fixed
 install paths in spec
- add the latest change from git which add DRR support
 c86f34942a0ce9f8203c0c38f9fe9604f96be706

* Mon Jan 19 2009 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.28-1
- previous two patches were included into 2.6.28 release.
- update

* Mon Jan 12 2009 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.27-2
- 475130 - Negative preferred lifetimes of IPv6 prefixes/addresses
  displayed incorrectly
- 472878 - “ip maddr show” in IB interface causes a stack corruption
- both patches will be probably in iproute v2.6.28

* Thu Dec 4 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.6.27-1
- aead support was included into upstream version
- patch for moving libs is now deprecated
- update to 2.6.27

* Tue Aug 12 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.6.26-1
- update to 2.6.26
- clean patches

* Tue Jul 22 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.6.25-5
- fix iproute2-2.6.25-segfault.patch

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.6.25-4
- rebuild for new db4-4.7

* Thu Jul  3 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.6.25-3
- 449933 instead of failing strncpy use copying byte after byte

* Wed May 14 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.6.25-2
- allow replay setting, solve also 444724

* Mon Apr 21 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.6.25-1
- update
- remove patch for backward compatibility
- add patch for AEAD compatibility

* Thu Feb 21 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.6.23-4
- add creating ps file again. Fix was done in texlive

* Wed Feb  6 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.6.23-3
- rebuild without tetex files. It isn't working in rawhide yet. Added
  new source for ps files. 
- #431179 backward compatibility for previous iproute versions

* Mon Jan 21 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.6.23-2
- rebuild with fix tetex and linuxdoc-tools -> manual pdf
- clean unnecessary patches
- add into spec *.so objects, new BR linux-atm-libs-devel

* Wed Oct 31 2007 Marcela Maslanova <mmaslano@redhat.com> - 2.6.23-1
- new version from upstrem 2.3.23

* Tue Oct 23 2007 Marcela Maslanova <mmaslano@redhat.com> - 2.6.22-5
- move files from /usr/lib/tc to /usr/share/tc
- remove listing files twice

* Fri Aug 31 2007 Marcela Maslanova <mmaslano@redhat.com> - 2.6.22-3
- package review #225903

* Mon Aug 27 2007 Jeremy Katz <katzj@redhat.com> - 2.6.22-2
- rebuild for new db4

* Wed Jul 11 2007 Radek Vokál <rvokal@redhat.com> - 2.6.22-1
- upgrade to 2.6.22

* Mon Mar 19 2007 Radek Vokál <rvokal@redhat.com> - 2.6.20-2
- fix broken tc-pfifo man page (#232891)

* Thu Mar 15 2007 Radek Vokál <rvokal@redhat.com> - 2.6.20-1
- upgrade to 2.6.20

* Fri Dec 15 2006 Radek Vokál <rvokal@redhat.com> - 2.6.19-1
- upgrade to 2.6.19

* Mon Dec 11 2006 Radek Vokál <rvokal@redhat.com> - 2.6.18-5
- fix snapshot version

* Fri Dec  1 2006 Radek Vokál <rvokal@redhat.com> - 2.6.18-4
- spec file cleanup
- one more rebuilt against db4

* Thu Nov 16 2006 Radek Vokál <rvokal@redhat.com> - 2.6.18-3
- fix defective manpage for tc-pfifo (#215399)

* Mon Nov 13 2006 Radek Vokál <rvokal@redhat.com> - 2.6.18-2
- rebuilt against new db4

* Tue Oct  3 2006 Radek Vokal <rvokal@redhat.com> - 2.6.18-1
- upgrade to upstream 2.6.18
- initcwnd patch merged
- bug fix for xfrm monitor
- alignment fixes for cris
- documentation corrections
        
* Mon Oct  2 2006 Radek Vokal <rvokal@redhat.com> - 2.6.16-7
- fix ip.8 man page, add initcwnd option

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 2.6.16-6
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 Radek Vokal <rvokal@redhat.com> - 2.6.16-5
- fix crash when resolving ip address

* Mon Aug 21 2006 Radek Vokál <rvokal@redhat.com> - 2.6.16-4
- add LOWER_UP and DORMANT flags (#202199)
- use dist tag

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.6.16-3.1
- rebuild

* Mon Jun 26 2006 Radek Vokál <rvokal@redhat.com> - 2.6.16-3
- improve handling of initcwnd value (#179719)

* Sun May 28 2006 Radek Vokál <rvokal@redhat.com> - 2.6.16-2
- fix BuildRequires: flex (#193403)

* Sun Mar 26 2006 Radek Vokál <rvokal@redhat.com> - 2.6.16-1
- upgrade to 2.6.16-060323
- don't hardcode /usr/lib in tc (#186607)

* Wed Feb 22 2006 Radek Vokál <rvokal@redhat.com> - 2.6.15-2
- own /usr/lib/tc (#181953)
- obsoletes shapecfg (#182284)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.6.15-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.6.15-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 17 2006 Radek Vokal <rvokal@redhat.com> 2.6.15-1
- upgrade to 2.6.15-060110

* Mon Dec 12 2005 Radek Vokal <rvokal@redhat.com> 2.6.14-11
- rebuilt

* Fri Dec 09 2005 Radek Vokal <rvokal@redhat.com> 2.6.14-10
- remove backup of config files (#175302)

* Fri Nov 11 2005 Radek Vokal <rvokal@redhat.com> 2.6.14-9
- use tc manpages and cbq.init from source tarball (#172851)

* Thu Nov 10 2005 Radek Vokal <rvokal@redhat.com> 2.6.14-8
- new upstream source 

* Mon Oct 31 2005 Radek Vokal <rvokal@redhat.com> 2.6.14-7
- add warning to ip tunnel add command (#128107)

* Fri Oct 07 2005 Bill Nottingham <notting@redhat.com> 2.6.14-6
- update from upstream (appears to fix #170111)

* Fri Oct 07 2005 Radek Vokal <rvokal@redhat.com> 2.6.14-5
- update from upstream
- fixed host_len size for memcpy (#168903) <Matt_Domsch@dell.com>

* Fri Sep 23 2005 Radek Vokal <rvokal@redhat.com> 2.6.14-4
- add RPM_OPT_FLAGS

* Mon Sep 19 2005 Radek Vokal <rvokal@redhat.com> 2.6.14-3
- forget to apply the patch :( 

* Mon Sep 19 2005 Radek Vokal <rvokal@redhat.com> 2.6.14-2
- make ip help work again (#168449)

* Wed Sep 14 2005 Radek Vokal <rvokal@redhat.com> 2.6.14-1
- upgrade to ss050901 for 2.6.14 kernel headers

* Fri Aug 26 2005 Radek Vokal <rvokal@redhat.com> 2.6.13-3
- added /sbin/cbq script and sample configuration files (#166301)

* Fri Aug 19 2005 Radek Vokal <rvokal@redhat.com> 2.6.13-2
- upgrade to iproute2-050816

* Thu Aug 11 2005 Radek Vokal <rvokal@redhat.com> 2.6.13-1
- update to snapshot for 2.6.13+ kernel

* Tue May 24 2005 Radek Vokal <rvokal@redhat.com> 2.6.11-2
- removed useless initvar patch (#150798)
- new upstream source 

* Tue Mar 15 2005 Radek Vokal <rvokal@redhat.com> 2.6.11-1
- update to iproute-2.6.11

* Fri Mar 04 2005 Radek Vokal <rvokal@redhat.com> 2.6.10-2
- gcc4 rebuilt

* Wed Feb 16 2005 Radek Vokal <rvokal@redhat.com> 2.6.10-1
- update to iproute-2.6.10

* Thu Dec 23 2004 Radek Vokal <rvokal@redhat.com> 2.6.9-6
- added arpd into sbin

* Mon Nov 29 2004 Radek Vokal <rvokal@redhat.com> 2.6.9-5
- debug info removed from makefile and from spec (#140891)

* Tue Nov 16 2004 Radek Vokal <rvokal@redhat.com> 2.6.9-4
- source file updated from snapshot version
- endian patch adding <endian.h> 

* Sat Sep 18 2004 Joshua Blanton <jblanton@cs.ohiou.edu> 2.6.9-3
- added installation of netem module for tc

* Mon Sep 06 2004 Radek Vokal <rvokal@redhat.com> 2.6.9-2
- fixed possible buffer owerflow, path by Steve Grubb <linux_4ever@yahoo.com>

* Wed Sep 01 2004 Radek Vokal <rvokal@redhat.com> 2.6.9-1
- updated to iproute-2.6.9, spec file change, patches cleared

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 26 2004 Phil Knirsch <pknirsch@redhat.com> 2.4.7-16
- Took tons of manpages from debian, much more complete (#123952).

* Thu May 06 2004 Phil Knirsch <pknirsch@redhat.com> 2.4.7-15
- rebuilt

* Thu May 06 2004 Phil Knirsch <pknirsch@redhat.com> 2.4.7-13.2
- Built security errata version for FC1.

* Wed Apr 21 2004 Phil Knirsch <pknirsch@redhat.com> 2.4.7-14
- Fixed -f option for ss (#118355).
- Small description fix (#110997).
- Added initialization of some vars (#74961). 
- Added patch to initialize "default" rule as well (#60693).

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Nov 05 2003 Phil Knirsch <pknirsch@redhat.com> 2.4.7-12
- Security errata for netlink (CAN-2003-0856).

* Thu Oct 23 2003 Phil Knirsch <pknirsch@redhat.com>
- Updated to latest version. Used by other distros, so seems stable. ;-)
- Quite a few patches needed updating in that turn.
- Added ss (#107363) and several other new nifty tools.

* Tue Jun 17 2003 Phil Knirsch <pknirsch@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Jan 16 2003 Phil Knirsch <pknirsch@redhat.com> 2.4.7-7
- Added htb3-tc patch from http://luxik.cdi.cz/~devik/qos/htb/ (#75486).

* Fri Oct 11 2002 Bill Nottingham <notting@redhat.com> 2.4.7-6
- remove flags patch at author's request

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 19 2002 Phil Knirsch <pknirsch@redhat.com> 2.4.7-4
- Don't forcibly strip binaries

* Mon May 27 2002 Phil Knirsch <pknirsch@redhat.com> 2.4.7-3
- Fixed missing diffserv and atm support in config (#57278).
- Fixed inconsistent numeric base problem for command line (#65473).

* Tue May 14 2002 Phil Knirsch <pknirsch@redhat.com> 2.4.7-2
- Added patch to fix crosscompiling by Adrian Linkins.

* Fri Mar 15 2002 Phil Knirsch <pknirsch@redhat.com> 2.4.7-1
- Update to latest stable release 2.4.7-now-ss010824.
- Added simple man page for ip.

* Wed Aug  8 2001 Bill Nottingham <notting@redhat.com>
- allow setting of allmulti & promisc flags (#48669)

* Mon Jul 02 2001 Than Ngo <than@redhat.com>
- fix build problem in beehive if kernel-sources is not installed

* Fri May 25 2001 Helge Deller <hdeller@redhat.de>
- updated to iproute2-2.2.4-now-ss001007.tar.gz 
- bzip2 source tar file
- "License" replaces "Copyright"
- added "BuildPrereq: tetex-latex tetex-dvips psutils"
- rebuilt for 7.2

* Tue May  1 2001 Bill Nottingham <notting@redhat.com>
- use the system headers - the included ones are broken
- ETH_P_ECHO went away

* Sat Jan  6 2001 Jeff Johnson <jbj@redhat.com>
- test for specific KERNEL_INCLUDE directories.

* Thu Oct 12 2000 Than Ngo <than@redhat.com>
- rebuild for 7.1

* Thu Oct 12 2000 Than Ngo <than@redhat.com>
- add default configuration files for iproute (Bug #10549, #18887)

* Tue Jul 25 2000 Jakub Jelinek <jakub@redhat.com>
- fix include-glibc/ to cope with glibc 2.2 new resolver headers

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Than Ngo <than@redhat.de>
- rebuilt in the new build environment
- use RPM macros
- handle RPM_OPT_FLAGS

* Sat Jun 03 2000 Than Ngo <than@redhat.de>
- fix iproute to build with new glibc

* Fri May 26 2000 Ngo Than <than@redhat.de>
- update to 2.2.4-now-ss000305
- add configuration files

* Mon Sep 13 1999 Bill Nottingham <notting@redhat.com>
- strip binaries

* Mon Aug 16 1999 Cristian Gafton <gafton@redhat.com>
- first build
