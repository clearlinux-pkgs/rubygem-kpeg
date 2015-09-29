#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-kpeg
Version  : 1.0.0
Release  : 6
URL      : https://rubygems.org/downloads/kpeg-1.0.0.gem
Source0  : https://rubygems.org/downloads/kpeg-1.0.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: rubygem-kpeg-bin
BuildRequires : ruby
BuildRequires : rubygem-hoe
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-test-unit

%description
= kpeg
home :: https://github.com/evanphx/kpeg
bugs :: https://github.com/evanphx/kpeg/issues

%package bin
Summary: bin components for the rubygem-kpeg package.
Group: Binaries

%description bin
bin components for the rubygem-kpeg package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n kpeg-1.0.0
gem spec %{SOURCE0} -l --ruby > rubygem-kpeg.gemspec

%build
gem build rubygem-kpeg.gemspec

%install
gem_dir=$(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .${gem_dir} \
--bindir .%{_bindir} \
kpeg-1.0.0.gem

mkdir -p %{buildroot}${gem_dir}
cp -pa .${gem_dir}/* \
%{buildroot}${gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
rake test


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/kpeg-1.0.0.gem
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/Hoe/Kpeg/cdesc-Kpeg.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/Hoe/Kpeg/define_kpeg_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/Hoe/Kpeg/initialize_kpeg-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/Hoe/Kpeg/kpeg_flags-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/Hoe/Kpeg/kpeg_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/Hoe/cdesc-Hoe.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Action/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Action/action-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Action/cdesc-Action.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Action/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Action/match-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Action/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/AndPredicate/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/AndPredicate/cdesc-AndPredicate.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/AndPredicate/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/AndPredicate/match-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/AndPredicate/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/AndPredicate/op-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Bounds/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Bounds/cdesc-Bounds.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Bounds/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Bounds/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Bounds/op-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CharRange/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CharRange/cdesc-CharRange.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CharRange/fin-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CharRange/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CharRange/match-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CharRange/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CharRange/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CharRange/string-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Choice/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Choice/%7c-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Choice/cdesc-Choice.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Choice/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Choice/match-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Choice/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Choice/ops-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CodeGenerator/cdesc-CodeGenerator.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CodeGenerator/handle_ast-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CodeGenerator/indentify-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CodeGenerator/make-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CodeGenerator/method_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CodeGenerator/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CodeGenerator/output-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CodeGenerator/output_ast-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CodeGenerator/output_footer-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CodeGenerator/output_grammar-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CodeGenerator/output_header-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CodeGenerator/output_op-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CodeGenerator/parse-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CodeGenerator/reset_saves-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CodeGenerator/save-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CodeGenerator/standalone-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CodeGenerator/standalone_region-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Collect/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Collect/cdesc-Collect.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Collect/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Collect/match-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Collect/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Collect/op-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/MemoEntry/ans-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/MemoEntry/cdesc-MemoEntry.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/MemoEntry/left_rec-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/MemoEntry/move%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/MemoEntry/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/MemoEntry/pos-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/MemoEntry/result-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/MemoEntry/set-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/ParseError/cdesc-ParseError.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/RuleInfo/cdesc-RuleInfo.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/RuleInfo/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/RuleInfo/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/RuleInfo/rendered-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/apply-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/apply_with_args-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/cdesc-CompiledParser.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/external_invoke-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/failed_rule-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/failing_rule_offset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/failure_caret-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/failure_character-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/failure_info-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/failure_oneline-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/get_byte-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/get_text-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/grow_lr-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/match_string-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/parse-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/pos-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/raise_error-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/result-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/rule_info-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/scan-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/set_failed_rule-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/set_string-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/setup_foreign_grammar-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/setup_parser-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/show_error-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/show_pos-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/CompiledParser/string-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Dot/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Dot/cdesc-Dot.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Dot/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Dot/match-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/ForeignInvokeRule/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/ForeignInvokeRule/arguments-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/ForeignInvokeRule/cdesc-ForeignInvokeRule.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/ForeignInvokeRule/grammar_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/ForeignInvokeRule/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/ForeignInvokeRule/match-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/ForeignInvokeRule/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/ForeignInvokeRule/rule_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/FormatParser/MemoEntry/cdesc-MemoEntry.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/FormatParser/ParseError/cdesc-ParseError.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/FormatParser/RuleInfo/cdesc-RuleInfo.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/FormatParser/cdesc-FormatParser.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/FormatParser/g-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/FormatParser/grammar-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/FormatParser/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/%5b%5d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/%5b%5d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/action-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/add_directive-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/add_foreign_grammar-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/add_setup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/andp-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/any-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/bounds-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/cdesc-Grammar.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/collect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/directives-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/dot-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/find-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/foreign_grammars-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/foreign_invoke-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/invoke-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/kleene-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/lit-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/many-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/maybe-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/method_missing-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/multiple-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/notp-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/range-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/ref-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/reg-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/resolve-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/root-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/rule_order-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/rules-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/seq-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/set-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/set_variable-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/setup_actions-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/str-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/t-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Grammar/variables-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/GrammarRenderer/cdesc-GrammarRenderer.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/GrammarRenderer/escape-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/GrammarRenderer/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/GrammarRenderer/parens%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/GrammarRenderer/render-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/GrammarRenderer/render_op-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/InvokeRule/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/InvokeRule/arguments-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/InvokeRule/cdesc-InvokeRule.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/InvokeRule/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/InvokeRule/match-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/InvokeRule/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/InvokeRule/rule_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/LiteralRegexp/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/LiteralRegexp/cdesc-LiteralRegexp.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/LiteralRegexp/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/LiteralRegexp/match-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/LiteralRegexp/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/LiteralRegexp/regexp-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/LiteralRegexp/string-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/LiteralString/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/LiteralString/cdesc-LiteralString.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/LiteralString/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/LiteralString/match-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/LiteralString/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/LiteralString/string-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Match/cdesc-Match.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/MatchComposition/cdesc-MatchComposition.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/MatchComposition/explain-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/MatchComposition/matches-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/MatchComposition/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/MatchComposition/op-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/MatchComposition/total_string-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/MatchComposition/value-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/MatchString/cdesc-MatchString.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/MatchString/explain-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/MatchString/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/MatchString/op-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/MatchString/string-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/MatchString/total_string-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/MatchString/value-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Multiple/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Multiple/cdesc-Multiple.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Multiple/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Multiple/match-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Multiple/max-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Multiple/min-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Multiple/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Multiple/op-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Multiple/save_values%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Multiple/save_values-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/NotPredicate/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/NotPredicate/cdesc-NotPredicate.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/NotPredicate/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/NotPredicate/match-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/NotPredicate/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/NotPredicate/op-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Operator/%7c-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Operator/action-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Operator/cdesc-Operator.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Operator/detect_tags-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Operator/inspect_type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Operator/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Operator/prune_values-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Operator/set_action-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/LeftRecursive/cdesc-LeftRecursive.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/LeftRecursive/detected-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/LeftRecursive/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/MemoEntry/ans-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/MemoEntry/cdesc-MemoEntry.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/MemoEntry/inc%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/MemoEntry/move%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/MemoEntry/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/MemoEntry/pos-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/MemoEntry/uses-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/apply-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/cdesc-Parser.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/expectation-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/expected_string-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/fail-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/failed%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/failing_offset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/failing_op-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/grammar-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/grow_lr-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/invoke-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/memoizations-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/parse-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Parser/switch_grammar-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Position/cdesc-Position.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Position/current_column-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Position/current_line-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Position/lines-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Rule/arguments-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Rule/cdesc-Rule.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Rule/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Rule/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Rule/op-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/RuleReference/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/RuleReference/arguments-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/RuleReference/cdesc-RuleReference.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/RuleReference/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/RuleReference/match-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/RuleReference/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/RuleReference/rule_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Sequence/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Sequence/cdesc-Sequence.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Sequence/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Sequence/match-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Sequence/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Sequence/ops-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/StringEscape/MemoEntry/cdesc-MemoEntry.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/StringEscape/ParseError/cdesc-ParseError.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/StringEscape/RuleInfo/cdesc-RuleInfo.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/StringEscape/cdesc-StringEscape.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/StringEscape/text-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Tag/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Tag/cdesc-Tag.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Tag/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Tag/match-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Tag/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Tag/op-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/Tag/tag_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/cdesc-KPeg.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/compile-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/grammar-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/load-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/load_grammar-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/KPeg/match-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/examples/phone_number/page-README_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/examples/upper/page-README_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/lib/kpeg/page-format_parser_kpeg.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/lib/kpeg/page-string_escape_kpeg.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/page-History_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/page-Manifest_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/kpeg-1.0.0/ri/page-README_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/.autotest
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/.gemtest
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/.travis.yml
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/History.txt
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/Manifest.txt
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/README.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/bin/kpeg
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/examples/calculator/calculator.kpeg
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/examples/calculator/calculator.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/examples/foreign_reference/literals.kpeg
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/examples/foreign_reference/matcher.kpeg
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/examples/foreign_reference/matcher.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/examples/lua_string/driver.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/examples/lua_string/lua_string.kpeg
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/examples/lua_string/lua_string.kpeg.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/examples/phone_number/README.md
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/examples/phone_number/phone_number.kpeg
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/examples/phone_number/phone_number.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/examples/upper/README.md
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/examples/upper/upper.kpeg
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/examples/upper/upper.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/kpeg.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/lib/hoe/kpeg.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/lib/kpeg.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/lib/kpeg/code_generator.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/lib/kpeg/compiled_parser.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/lib/kpeg/format_parser.kpeg
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/lib/kpeg/format_parser.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/lib/kpeg/grammar.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/lib/kpeg/grammar_renderer.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/lib/kpeg/match.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/lib/kpeg/parser.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/lib/kpeg/position.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/lib/kpeg/string_escape.kpeg
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/lib/kpeg/string_escape.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/test/inputs/comments.kpeg
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/test/test_kpeg.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/test/test_kpeg_code_generator.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/test/test_kpeg_compiled_parser.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/test/test_kpeg_format.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/test/test_kpeg_format_parser_round_trip.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/test/test_kpeg_grammar.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/test/test_kpeg_grammar_renderer.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/test/test_kpeg_string_escape.rb
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/vim/syntax_kpeg/ftdetect/kpeg.vim
/usr/lib64/ruby/gems/2.2.0/gems/kpeg-1.0.0/vim/syntax_kpeg/syntax/kpeg.vim
/usr/lib64/ruby/gems/2.2.0/specifications/kpeg-1.0.0.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/kpeg
