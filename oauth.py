


<!DOCTYPE html>
<html>
  <head>
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
        <title>oauth.py at master from mikeknapp/AppEngine-OAuth-Library - GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />

    
    

    <meta content="authenticity_token" name="csrf-param" />
<meta content="d60ad866c231758375007f21923afb4a843120c0" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/stylesheets/bundles/github-9bef515c140b863f61df966f44e62caaa19ccae1.css" media="screen" rel="stylesheet" type="text/css" />
    

    <script src="https://a248.e.akamai.net/assets.github.com/javascripts/bundles/jquery-0afaa9d8025004af7fc6f2a561837057d3f21298.js" type="text/javascript"></script>
    <script src="https://a248.e.akamai.net/assets.github.com/javascripts/bundles/github-c3520f89f16a33cc97a93889496732ddc0d6c49b.js" type="text/javascript"></script>
    

      <link rel='permalink' href='/mikeknapp/AppEngine-OAuth-Library/blob/269b2b0ed882fa38d185c795d8ba46a04f10f5f3/oauth.py'>
    

    <meta name="description" content="AppEngine-OAuth-Library - An OAuth library for interacting with Twitter, MySpace, LinkedIn and Yahoo on AppEngine" />
  <link href="https://github.com/mikeknapp/AppEngine-OAuth-Library/commits/master.atom" rel="alternate" title="Recent Commits to AppEngine-OAuth-Library:master" type="application/atom+xml" />

  </head>


  <body class="logged_in page-blob  env-production ">
    


    

    <div id="main">
      <div id="header" class="true">
          <a class="logo" href="https://github.com/">
            <img alt="github" class="default svg" height="45" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov6.svg" />
            <img alt="github" class="default png" height="45" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov6.png" />
            <!--[if (gt IE 8)|!(IE)]><!-->
            <img alt="github" class="hover svg" height="45" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov6-hover.svg" />
            <img alt="github" class="hover png" height="45" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov6-hover.png" />
            <!--<![endif]-->
          </a>

          


    <div class="userbox">
      <div class="avatarname">
        <a href="https://github.com/gtracy"><img height="20" src="https://secure.gravatar.com/avatar/a9afc685773640f78877da7efec6e752?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" width="20" /></a>
        <a href="https://github.com/gtracy" class="name">gtracy</a>

      </div>
      <ul class="usernav">
        <li><a href="https://github.com/">Dashboard</a></li>
        <li>
          <a href="https://github.com/inbox">Inbox</a>
          <a href="https://github.com/inbox" class="unread_count ">0</a>
        </li>
        <li><a href="https://github.com/account">Account Settings</a></li>
        <li><a href="/logout">Log Out</a></li>
      </ul>
    </div><!-- /.userbox -->


        <div class="topsearch">
<form action="/search" id="top_search_form" method="get">      <a href="/search" class="advanced-search tooltipped downwards" title="Advanced Search">Advanced Search</a>
      <div class="search placeholder-field js-placeholder-field">
        <label class="placeholder" for="global-search-field">Search…</label>
        <input type="text" class="search my_repos_autocompleter" id="global-search-field" name="q" results="5" /> <input type="submit" value="Search" class="button" />
      </div>
      <input type="hidden" name="type" value="Everything" />
      <input type="hidden" name="repo" value="" />
      <input type="hidden" name="langOverride" value="" />
      <input type="hidden" name="start_value" value="1" />
</form>    <ul class="nav">
        <li class="explore"><a href="https://github.com/explore">Explore GitHub</a></li>
        <li><a href="https://gist.github.com">Gist</a></li>
        <li><a href="/blog">Blog</a></li>
      <li><a href="http://help.github.com">Help</a></li>
    </ul>
</div>

      </div>

      
            <div class="site">
      <div class="pagehead repohead vis-public   instapaper_ignore readability-menu">


      <div class="title-actions-bar">
        <h1>
          <a href="/mikeknapp">mikeknapp</a> /
          <strong><a href="/mikeknapp/AppEngine-OAuth-Library" class="js-current-repository">AppEngine-OAuth-Library</a></strong>
        </h1>
        



            <ul class="pagehead-actions">

        <li class="js-toggler-container watch-button-container on">
          <a href="/mikeknapp/AppEngine-OAuth-Library/toggle_watch" class="minibutton btn-watch watch-button js-toggler-target" data-method="post" data-remote="true"><span><span class="icon"></span>Watch</span></a>
          <a href="/mikeknapp/AppEngine-OAuth-Library/toggle_watch" class="minibutton btn-watch unwatch-button js-toggler-target" data-method="post" data-remote="true"><span><span class="icon"></span>Unwatch</span></a>
        </li>
              <li><a href="#fork_box" class="minibutton btn-fork " rel="facebox"><span><span class="icon"></span>Fork</span></a></li>

            <div id="fork_box" style="display:none">
              <h2>Where do you want to fork this to?</h2>
                <div class="full-button">
<form action="/mikeknapp/AppEngine-OAuth-Library/fork" method="post"><div style="margin:0;padding:0"><input name="authenticity_token" type="hidden" value="d60ad866c231758375007f21923afb4a843120c0" /></div>                    <button class="classy"><span>Fork to gtracy</span></button>
</form>                </div>
                <div class="rule"></div>
                  <div class="full-button">
<form action="/mikeknapp/AppEngine-OAuth-Library/fork" method="post"><div style="margin:0;padding:0"><input name="authenticity_token" type="hidden" value="d60ad866c231758375007f21923afb4a843120c0" /></div>                      <input id="organization" name="organization" type="hidden" value="twiliomadness" />
                      <button class="classy"><span>Fork to twiliomadness (organization)</span></button>
</form>                  </div>
                <div class="rule"></div>
                  <div class="full-button">
<form action="/mikeknapp/AppEngine-OAuth-Library/fork" method="post"><div style="margin:0;padding:0"><input name="authenticity_token" type="hidden" value="d60ad866c231758375007f21923afb4a843120c0" /></div>                      <input id="organization" name="organization" type="hidden" value="Asthmapolis" />
                      <button class="classy"><span>Fork to Asthmapolis (organization)</span></button>
</form>                  </div>
            </div>

      <li class="repostats">
        <ul class="repo-stats">
          <li class="watchers watching">
            <a href="/mikeknapp/AppEngine-OAuth-Library/watchers" title="Watchers — You&#39;re Watching" class="tooltipped downwards">
              180
            </a>
          </li>
          <li class="forks">
            <a href="/mikeknapp/AppEngine-OAuth-Library/network" title="Forks" class="tooltipped downwards">
              29
            </a>
          </li>
        </ul>
      </li>
    </ul>

      </div>

        

  <ul class="tabs">
    <li><a href="/mikeknapp/AppEngine-OAuth-Library" class="selected" highlight="repo_sourcerepo_downloadsrepo_commitsrepo_tagsrepo_branches">Code</a></li>
    <li><a href="/mikeknapp/AppEngine-OAuth-Library/network" highlight="repo_networkrepo_fork_queue">Network</a>
    <li><a href="/mikeknapp/AppEngine-OAuth-Library/pulls" highlight="repo_pulls">Pull Requests <span class='counter'>0</span></a></li>

      <li><a href="/mikeknapp/AppEngine-OAuth-Library/issues" highlight="repo_issues">Issues <span class='counter'>0</span></a></li>


    <li><a href="/mikeknapp/AppEngine-OAuth-Library/graphs" highlight="repo_graphsrepo_contributors">Stats &amp; Graphs</a></li>

  </ul>

  
<div class="frame frame-center tree-finder" style="display:none"
      data-tree-list-url="/mikeknapp/AppEngine-OAuth-Library/tree-list/269b2b0ed882fa38d185c795d8ba46a04f10f5f3"
      data-blob-url-prefix="/mikeknapp/AppEngine-OAuth-Library/blob/269b2b0ed882fa38d185c795d8ba46a04f10f5f3"
    >

  <div class="breadcrumb">
    <b><a href="/mikeknapp/AppEngine-OAuth-Library">AppEngine-OAuth-Library</a></b> /
    <input class="tree-finder-input" type="text" name="query" autocomplete="off" spellcheck="false">
  </div>

    <div class="octotip">
      <p>
        <a href="/mikeknapp/AppEngine-OAuth-Library/dismiss-tree-finder-help" class="dismiss js-dismiss-tree-list-help" title="Hide this notice forever">Dismiss</a>
        <strong>Octotip:</strong> You've activated the <em>file finder</em>
        by pressing <span class="kbd">t</span> Start typing to filter the
        file list. Use <span class="kbd badmono">↑</span> and
        <span class="kbd badmono">↓</span> to navigate,
        <span class="kbd">enter</span> to view files.
      </p>
    </div>

  <table class="tree-browser" cellpadding="0" cellspacing="0">
    <tr class="js-header"><th>&nbsp;</th><th>name</th></tr>
    <tr class="js-no-results no-results" style="display: none">
      <th colspan="2">No matching files</th>
    </tr>
    <tbody class="js-results-list">
    </tbody>
  </table>
</div>

<div id="jump-to-line" style="display:none">
  <h2>Jump to Line</h2>
  <form>
    <input class="textfield" type="text">
    <div class="full-button">
      <button type="submit" class="classy">
        <span>Go</span>
      </button>
    </div>
  </form>
</div>


<div class="subnav-bar">

  <ul class="actions">
    
      <li class="switcher">

        <div class="context-menu-container js-menu-container">
          <span class="text">Current branch:</span>
          <a href="#"
             class="minibutton bigger switcher context-menu-button js-menu-target js-commitish-button btn-branch repo-tree"
             data-master-branch="master"
             data-ref="master">
            <span><span class="icon"></span>master</span>
          </a>

          <div class="context-pane commitish-context js-menu-content">
            <a href="javascript:;" class="close js-menu-close"></a>
            <div class="title">Switch Branches/Tags</div>
            <div class="body pane-selector commitish-selector js-filterable-commitishes">
              <div class="filterbar">
                <div class="placeholder-field js-placeholder-field">
                  <label class="placeholder" for="context-commitish-filter-field" data-placeholder-mode="sticky">Filter branches/tags</label>
                  <input type="text" id="context-commitish-filter-field" class="commitish-filter" />
                </div>

                <ul class="tabs">
                  <li><a href="#" data-filter="branches" class="selected">Branches</a></li>
                  <li><a href="#" data-filter="tags">Tags</a></li>
                </ul>
              </div>

                <div class="commitish-item branch-commitish selector-item">
                  <h4>
                      <a href="/mikeknapp/AppEngine-OAuth-Library/blob/master/oauth.py" data-name="master">master</a>
                  </h4>
                </div>


              <div class="no-results" style="display:none">Nothing to show</div>
            </div>
          </div><!-- /.commitish-context-context -->
        </div>

      </li>
  </ul>

  <ul class="subnav">
    <li><a href="/mikeknapp/AppEngine-OAuth-Library" class="selected" highlight="repo_source">Files</a></li>
    <li><a href="/mikeknapp/AppEngine-OAuth-Library/commits/master" highlight="repo_commits">Commits</a></li>
    <li><a href="/mikeknapp/AppEngine-OAuth-Library/branches" class="" highlight="repo_branches">Branches <span class="counter">1</span></a></li>
    <li><a href="/mikeknapp/AppEngine-OAuth-Library/tags" class="blank" highlight="repo_tags">Tags <span class="counter">0</span></a></li>
    <li><a href="/mikeknapp/AppEngine-OAuth-Library/downloads" class="blank" highlight="repo_downloads">Downloads <span class="counter">0</span></a></li>
  </ul>

</div>

  
  
  


        

      </div><!-- /.pagehead -->

      




  
  <p class="last-commit">Latest commit to the <strong>master</strong> branch</p>

<div class="commit commit-tease js-details-container">
  <p class="commit-title ">
      <a href="/mikeknapp/AppEngine-OAuth-Library"><a href="/mikeknapp/AppEngine-OAuth-Library/commit/269b2b0ed882fa38d185c795d8ba46a04f10f5f3" class="message">Merge pull request </a><a href="https://github.com/mikeknapp/AppEngine-OAuth-Library/issues/7" title="Unnecessary call?" class="issue-link">#7</a><a href="/mikeknapp/AppEngine-OAuth-Library/commit/269b2b0ed882fa38d185c795d8ba46a04f10f5f3" class="message"> from setomits/master</a></a>
      <a href="javascript:;" class="minibutton expander-minibutton js-details-target"><span>…</span></a>
  </p>
    <div class="commit-desc"><pre>Unnecessary call?</pre></div>
  <div class="commit-meta">
    <a href="/mikeknapp/AppEngine-OAuth-Library/commit/269b2b0ed882fa38d185c795d8ba46a04f10f5f3" class="sha-block">commit <span class="sha">269b2b0ed8</span></a>

    <div class="authorship">
      <img class="gravatar" height="20" src="https://secure.gravatar.com/avatar/2f9c7c55818ff2e2b99464373f8ffb5c?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" width="20" />
      <span class="author-name"><a href="/mikeknapp">mikeknapp</a></span>
      authored <time class="js-relative-date" datetime="2011-05-22T21:30:43-07:00" title="2011-05-22 21:30:43">May 22, 2011</time>

    </div>
  </div>
</div>


  <div id="slider">

    <div class="breadcrumb" data-path="oauth.py/">
      <b><a href="/mikeknapp/AppEngine-OAuth-Library/tree/269b2b0ed882fa38d185c795d8ba46a04f10f5f3" class="js-rewrite-sha">AppEngine-OAuth-Library</a></b> / oauth.py       <span style="display:none" id="clippy_3429" class="clippy-text">oauth.py</span>
      
      <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
              width="110"
              height="14"
              class="clippy"
              id="clippy" >
      <param name="movie" value="https://a248.e.akamai.net/assets.github.com/flash/clippy.swf?v5"/>
      <param name="allowScriptAccess" value="always" />
      <param name="quality" value="high" />
      <param name="scale" value="noscale" />
      <param NAME="FlashVars" value="id=clippy_3429&amp;copied=copied!&amp;copyto=copy to clipboard">
      <param name="bgcolor" value="#FFFFFF">
      <param name="wmode" value="opaque">
      <embed src="https://a248.e.akamai.net/assets.github.com/flash/clippy.swf?v5"
             width="110"
             height="14"
             name="clippy"
             quality="high"
             allowScriptAccess="always"
             type="application/x-shockwave-flash"
             pluginspage="http://www.macromedia.com/go/getflashplayer"
             FlashVars="id=clippy_3429&amp;copied=copied!&amp;copyto=copy to clipboard"
             bgcolor="#FFFFFF"
             wmode="opaque"
      />
      </object>
      

    </div>

    <div class="frames">
      <div class="frame frame-center" data-path="oauth.py/" data-permalink-url="/mikeknapp/AppEngine-OAuth-Library/blob/269b2b0ed882fa38d185c795d8ba46a04f10f5f3/oauth.py" data-title="oauth.py at master from mikeknapp/AppEngine-OAuth-Library - GitHub" data-type="blob">
          <ul class="big-actions">
            <li><a class="file-edit-link minibutton js-rewrite-sha" href="/mikeknapp/AppEngine-OAuth-Library/edit/269b2b0ed882fa38d185c795d8ba46a04f10f5f3/oauth.py" data-method="post"><span>Edit this file</span></a></li>
          </ul>

        <div id="files">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><img alt="Txt" height="16" src="https://a248.e.akamai.net/assets.github.com/images/icons/txt.png" width="16" /></span>
                <span class="mode" title="File Mode">100755</span>
                  <span>634 lines (463 sloc)</span>
                <span>18.995 kb</span>
              </div>
              <ul class="actions">
                <li><a href="/mikeknapp/AppEngine-OAuth-Library/raw/master/oauth.py" id="raw-url">raw</a></li>
                  <li><a href="/mikeknapp/AppEngine-OAuth-Library/blame/master/oauth.py">blame</a></li>
                <li><a href="/mikeknapp/AppEngine-OAuth-Library/commits/master/oauth.py">history</a></li>
              </ul>
            </div>
              <div class="data type-python">
      <table cellpadding="0" cellspacing="0" class="lines">
        <tr>
          <td>
            <pre class="line_numbers"><span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
<span id="L302" rel="#L302">302</span>
<span id="L303" rel="#L303">303</span>
<span id="L304" rel="#L304">304</span>
<span id="L305" rel="#L305">305</span>
<span id="L306" rel="#L306">306</span>
<span id="L307" rel="#L307">307</span>
<span id="L308" rel="#L308">308</span>
<span id="L309" rel="#L309">309</span>
<span id="L310" rel="#L310">310</span>
<span id="L311" rel="#L311">311</span>
<span id="L312" rel="#L312">312</span>
<span id="L313" rel="#L313">313</span>
<span id="L314" rel="#L314">314</span>
<span id="L315" rel="#L315">315</span>
<span id="L316" rel="#L316">316</span>
<span id="L317" rel="#L317">317</span>
<span id="L318" rel="#L318">318</span>
<span id="L319" rel="#L319">319</span>
<span id="L320" rel="#L320">320</span>
<span id="L321" rel="#L321">321</span>
<span id="L322" rel="#L322">322</span>
<span id="L323" rel="#L323">323</span>
<span id="L324" rel="#L324">324</span>
<span id="L325" rel="#L325">325</span>
<span id="L326" rel="#L326">326</span>
<span id="L327" rel="#L327">327</span>
<span id="L328" rel="#L328">328</span>
<span id="L329" rel="#L329">329</span>
<span id="L330" rel="#L330">330</span>
<span id="L331" rel="#L331">331</span>
<span id="L332" rel="#L332">332</span>
<span id="L333" rel="#L333">333</span>
<span id="L334" rel="#L334">334</span>
<span id="L335" rel="#L335">335</span>
<span id="L336" rel="#L336">336</span>
<span id="L337" rel="#L337">337</span>
<span id="L338" rel="#L338">338</span>
<span id="L339" rel="#L339">339</span>
<span id="L340" rel="#L340">340</span>
<span id="L341" rel="#L341">341</span>
<span id="L342" rel="#L342">342</span>
<span id="L343" rel="#L343">343</span>
<span id="L344" rel="#L344">344</span>
<span id="L345" rel="#L345">345</span>
<span id="L346" rel="#L346">346</span>
<span id="L347" rel="#L347">347</span>
<span id="L348" rel="#L348">348</span>
<span id="L349" rel="#L349">349</span>
<span id="L350" rel="#L350">350</span>
<span id="L351" rel="#L351">351</span>
<span id="L352" rel="#L352">352</span>
<span id="L353" rel="#L353">353</span>
<span id="L354" rel="#L354">354</span>
<span id="L355" rel="#L355">355</span>
<span id="L356" rel="#L356">356</span>
<span id="L357" rel="#L357">357</span>
<span id="L358" rel="#L358">358</span>
<span id="L359" rel="#L359">359</span>
<span id="L360" rel="#L360">360</span>
<span id="L361" rel="#L361">361</span>
<span id="L362" rel="#L362">362</span>
<span id="L363" rel="#L363">363</span>
<span id="L364" rel="#L364">364</span>
<span id="L365" rel="#L365">365</span>
<span id="L366" rel="#L366">366</span>
<span id="L367" rel="#L367">367</span>
<span id="L368" rel="#L368">368</span>
<span id="L369" rel="#L369">369</span>
<span id="L370" rel="#L370">370</span>
<span id="L371" rel="#L371">371</span>
<span id="L372" rel="#L372">372</span>
<span id="L373" rel="#L373">373</span>
<span id="L374" rel="#L374">374</span>
<span id="L375" rel="#L375">375</span>
<span id="L376" rel="#L376">376</span>
<span id="L377" rel="#L377">377</span>
<span id="L378" rel="#L378">378</span>
<span id="L379" rel="#L379">379</span>
<span id="L380" rel="#L380">380</span>
<span id="L381" rel="#L381">381</span>
<span id="L382" rel="#L382">382</span>
<span id="L383" rel="#L383">383</span>
<span id="L384" rel="#L384">384</span>
<span id="L385" rel="#L385">385</span>
<span id="L386" rel="#L386">386</span>
<span id="L387" rel="#L387">387</span>
<span id="L388" rel="#L388">388</span>
<span id="L389" rel="#L389">389</span>
<span id="L390" rel="#L390">390</span>
<span id="L391" rel="#L391">391</span>
<span id="L392" rel="#L392">392</span>
<span id="L393" rel="#L393">393</span>
<span id="L394" rel="#L394">394</span>
<span id="L395" rel="#L395">395</span>
<span id="L396" rel="#L396">396</span>
<span id="L397" rel="#L397">397</span>
<span id="L398" rel="#L398">398</span>
<span id="L399" rel="#L399">399</span>
<span id="L400" rel="#L400">400</span>
<span id="L401" rel="#L401">401</span>
<span id="L402" rel="#L402">402</span>
<span id="L403" rel="#L403">403</span>
<span id="L404" rel="#L404">404</span>
<span id="L405" rel="#L405">405</span>
<span id="L406" rel="#L406">406</span>
<span id="L407" rel="#L407">407</span>
<span id="L408" rel="#L408">408</span>
<span id="L409" rel="#L409">409</span>
<span id="L410" rel="#L410">410</span>
<span id="L411" rel="#L411">411</span>
<span id="L412" rel="#L412">412</span>
<span id="L413" rel="#L413">413</span>
<span id="L414" rel="#L414">414</span>
<span id="L415" rel="#L415">415</span>
<span id="L416" rel="#L416">416</span>
<span id="L417" rel="#L417">417</span>
<span id="L418" rel="#L418">418</span>
<span id="L419" rel="#L419">419</span>
<span id="L420" rel="#L420">420</span>
<span id="L421" rel="#L421">421</span>
<span id="L422" rel="#L422">422</span>
<span id="L423" rel="#L423">423</span>
<span id="L424" rel="#L424">424</span>
<span id="L425" rel="#L425">425</span>
<span id="L426" rel="#L426">426</span>
<span id="L427" rel="#L427">427</span>
<span id="L428" rel="#L428">428</span>
<span id="L429" rel="#L429">429</span>
<span id="L430" rel="#L430">430</span>
<span id="L431" rel="#L431">431</span>
<span id="L432" rel="#L432">432</span>
<span id="L433" rel="#L433">433</span>
<span id="L434" rel="#L434">434</span>
<span id="L435" rel="#L435">435</span>
<span id="L436" rel="#L436">436</span>
<span id="L437" rel="#L437">437</span>
<span id="L438" rel="#L438">438</span>
<span id="L439" rel="#L439">439</span>
<span id="L440" rel="#L440">440</span>
<span id="L441" rel="#L441">441</span>
<span id="L442" rel="#L442">442</span>
<span id="L443" rel="#L443">443</span>
<span id="L444" rel="#L444">444</span>
<span id="L445" rel="#L445">445</span>
<span id="L446" rel="#L446">446</span>
<span id="L447" rel="#L447">447</span>
<span id="L448" rel="#L448">448</span>
<span id="L449" rel="#L449">449</span>
<span id="L450" rel="#L450">450</span>
<span id="L451" rel="#L451">451</span>
<span id="L452" rel="#L452">452</span>
<span id="L453" rel="#L453">453</span>
<span id="L454" rel="#L454">454</span>
<span id="L455" rel="#L455">455</span>
<span id="L456" rel="#L456">456</span>
<span id="L457" rel="#L457">457</span>
<span id="L458" rel="#L458">458</span>
<span id="L459" rel="#L459">459</span>
<span id="L460" rel="#L460">460</span>
<span id="L461" rel="#L461">461</span>
<span id="L462" rel="#L462">462</span>
<span id="L463" rel="#L463">463</span>
<span id="L464" rel="#L464">464</span>
<span id="L465" rel="#L465">465</span>
<span id="L466" rel="#L466">466</span>
<span id="L467" rel="#L467">467</span>
<span id="L468" rel="#L468">468</span>
<span id="L469" rel="#L469">469</span>
<span id="L470" rel="#L470">470</span>
<span id="L471" rel="#L471">471</span>
<span id="L472" rel="#L472">472</span>
<span id="L473" rel="#L473">473</span>
<span id="L474" rel="#L474">474</span>
<span id="L475" rel="#L475">475</span>
<span id="L476" rel="#L476">476</span>
<span id="L477" rel="#L477">477</span>
<span id="L478" rel="#L478">478</span>
<span id="L479" rel="#L479">479</span>
<span id="L480" rel="#L480">480</span>
<span id="L481" rel="#L481">481</span>
<span id="L482" rel="#L482">482</span>
<span id="L483" rel="#L483">483</span>
<span id="L484" rel="#L484">484</span>
<span id="L485" rel="#L485">485</span>
<span id="L486" rel="#L486">486</span>
<span id="L487" rel="#L487">487</span>
<span id="L488" rel="#L488">488</span>
<span id="L489" rel="#L489">489</span>
<span id="L490" rel="#L490">490</span>
<span id="L491" rel="#L491">491</span>
<span id="L492" rel="#L492">492</span>
<span id="L493" rel="#L493">493</span>
<span id="L494" rel="#L494">494</span>
<span id="L495" rel="#L495">495</span>
<span id="L496" rel="#L496">496</span>
<span id="L497" rel="#L497">497</span>
<span id="L498" rel="#L498">498</span>
<span id="L499" rel="#L499">499</span>
<span id="L500" rel="#L500">500</span>
<span id="L501" rel="#L501">501</span>
<span id="L502" rel="#L502">502</span>
<span id="L503" rel="#L503">503</span>
<span id="L504" rel="#L504">504</span>
<span id="L505" rel="#L505">505</span>
<span id="L506" rel="#L506">506</span>
<span id="L507" rel="#L507">507</span>
<span id="L508" rel="#L508">508</span>
<span id="L509" rel="#L509">509</span>
<span id="L510" rel="#L510">510</span>
<span id="L511" rel="#L511">511</span>
<span id="L512" rel="#L512">512</span>
<span id="L513" rel="#L513">513</span>
<span id="L514" rel="#L514">514</span>
<span id="L515" rel="#L515">515</span>
<span id="L516" rel="#L516">516</span>
<span id="L517" rel="#L517">517</span>
<span id="L518" rel="#L518">518</span>
<span id="L519" rel="#L519">519</span>
<span id="L520" rel="#L520">520</span>
<span id="L521" rel="#L521">521</span>
<span id="L522" rel="#L522">522</span>
<span id="L523" rel="#L523">523</span>
<span id="L524" rel="#L524">524</span>
<span id="L525" rel="#L525">525</span>
<span id="L526" rel="#L526">526</span>
<span id="L527" rel="#L527">527</span>
<span id="L528" rel="#L528">528</span>
<span id="L529" rel="#L529">529</span>
<span id="L530" rel="#L530">530</span>
<span id="L531" rel="#L531">531</span>
<span id="L532" rel="#L532">532</span>
<span id="L533" rel="#L533">533</span>
<span id="L534" rel="#L534">534</span>
<span id="L535" rel="#L535">535</span>
<span id="L536" rel="#L536">536</span>
<span id="L537" rel="#L537">537</span>
<span id="L538" rel="#L538">538</span>
<span id="L539" rel="#L539">539</span>
<span id="L540" rel="#L540">540</span>
<span id="L541" rel="#L541">541</span>
<span id="L542" rel="#L542">542</span>
<span id="L543" rel="#L543">543</span>
<span id="L544" rel="#L544">544</span>
<span id="L545" rel="#L545">545</span>
<span id="L546" rel="#L546">546</span>
<span id="L547" rel="#L547">547</span>
<span id="L548" rel="#L548">548</span>
<span id="L549" rel="#L549">549</span>
<span id="L550" rel="#L550">550</span>
<span id="L551" rel="#L551">551</span>
<span id="L552" rel="#L552">552</span>
<span id="L553" rel="#L553">553</span>
<span id="L554" rel="#L554">554</span>
<span id="L555" rel="#L555">555</span>
<span id="L556" rel="#L556">556</span>
<span id="L557" rel="#L557">557</span>
<span id="L558" rel="#L558">558</span>
<span id="L559" rel="#L559">559</span>
<span id="L560" rel="#L560">560</span>
<span id="L561" rel="#L561">561</span>
<span id="L562" rel="#L562">562</span>
<span id="L563" rel="#L563">563</span>
<span id="L564" rel="#L564">564</span>
<span id="L565" rel="#L565">565</span>
<span id="L566" rel="#L566">566</span>
<span id="L567" rel="#L567">567</span>
<span id="L568" rel="#L568">568</span>
<span id="L569" rel="#L569">569</span>
<span id="L570" rel="#L570">570</span>
<span id="L571" rel="#L571">571</span>
<span id="L572" rel="#L572">572</span>
<span id="L573" rel="#L573">573</span>
<span id="L574" rel="#L574">574</span>
<span id="L575" rel="#L575">575</span>
<span id="L576" rel="#L576">576</span>
<span id="L577" rel="#L577">577</span>
<span id="L578" rel="#L578">578</span>
<span id="L579" rel="#L579">579</span>
<span id="L580" rel="#L580">580</span>
<span id="L581" rel="#L581">581</span>
<span id="L582" rel="#L582">582</span>
<span id="L583" rel="#L583">583</span>
<span id="L584" rel="#L584">584</span>
<span id="L585" rel="#L585">585</span>
<span id="L586" rel="#L586">586</span>
<span id="L587" rel="#L587">587</span>
<span id="L588" rel="#L588">588</span>
<span id="L589" rel="#L589">589</span>
<span id="L590" rel="#L590">590</span>
<span id="L591" rel="#L591">591</span>
<span id="L592" rel="#L592">592</span>
<span id="L593" rel="#L593">593</span>
<span id="L594" rel="#L594">594</span>
<span id="L595" rel="#L595">595</span>
<span id="L596" rel="#L596">596</span>
<span id="L597" rel="#L597">597</span>
<span id="L598" rel="#L598">598</span>
<span id="L599" rel="#L599">599</span>
<span id="L600" rel="#L600">600</span>
<span id="L601" rel="#L601">601</span>
<span id="L602" rel="#L602">602</span>
<span id="L603" rel="#L603">603</span>
<span id="L604" rel="#L604">604</span>
<span id="L605" rel="#L605">605</span>
<span id="L606" rel="#L606">606</span>
<span id="L607" rel="#L607">607</span>
<span id="L608" rel="#L608">608</span>
<span id="L609" rel="#L609">609</span>
<span id="L610" rel="#L610">610</span>
<span id="L611" rel="#L611">611</span>
<span id="L612" rel="#L612">612</span>
<span id="L613" rel="#L613">613</span>
<span id="L614" rel="#L614">614</span>
<span id="L615" rel="#L615">615</span>
<span id="L616" rel="#L616">616</span>
<span id="L617" rel="#L617">617</span>
<span id="L618" rel="#L618">618</span>
<span id="L619" rel="#L619">619</span>
<span id="L620" rel="#L620">620</span>
<span id="L621" rel="#L621">621</span>
<span id="L622" rel="#L622">622</span>
<span id="L623" rel="#L623">623</span>
<span id="L624" rel="#L624">624</span>
<span id="L625" rel="#L625">625</span>
<span id="L626" rel="#L626">626</span>
<span id="L627" rel="#L627">627</span>
<span id="L628" rel="#L628">628</span>
<span id="L629" rel="#L629">629</span>
<span id="L630" rel="#L630">630</span>
<span id="L631" rel="#L631">631</span>
<span id="L632" rel="#L632">632</span>
<span id="L633" rel="#L633">633</span>
<span id="L634" rel="#L634">634</span>
</pre>
          </td>
          <td width="100%">
                <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/env python</span></div><div class='line' id='LC2'><br/></div><div class='line' id='LC3'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC4'><span class="sd">A simple OAuth implementation for authenticating users with third party</span></div><div class='line' id='LC5'><span class="sd">websites.</span></div><div class='line' id='LC6'><br/></div><div class='line' id='LC7'><span class="sd">A typical use case inside an AppEngine controller would be:</span></div><div class='line' id='LC8'><br/></div><div class='line' id='LC9'><span class="sd">1) Create the OAuth client. In this case we&#39;ll use the Twitter client,</span></div><div class='line' id='LC10'><span class="sd">  but you could write other clients to connect to different services.</span></div><div class='line' id='LC11'><br/></div><div class='line' id='LC12'><span class="sd">  import oauth</span></div><div class='line' id='LC13'><br/></div><div class='line' id='LC14'><span class="sd">  consumer_key = &quot;LKlkj83kaio2fjiudjd9...etc&quot;</span></div><div class='line' id='LC15'><span class="sd">  consumer_secret = &quot;58kdujslkfojkjsjsdk...etc&quot;</span></div><div class='line' id='LC16'><span class="sd">  callback_url = &quot;http://www.myurl.com/callback/twitter&quot;</span></div><div class='line' id='LC17'><br/></div><div class='line' id='LC18'><span class="sd">  client = oauth.TwitterClient(consumer_key, consumer_secret, callback_url)</span></div><div class='line' id='LC19'><br/></div><div class='line' id='LC20'><span class="sd">2) Send the user to Twitter in order to login:</span></div><div class='line' id='LC21'><br/></div><div class='line' id='LC22'><span class="sd">  self.redirect(client.get_authorization_url())</span></div><div class='line' id='LC23'><br/></div><div class='line' id='LC24'><span class="sd">3) Once the user has arrived back at your callback URL, you&#39;ll want to</span></div><div class='line' id='LC25'><span class="sd">  get the authenticated user information.</span></div><div class='line' id='LC26'><br/></div><div class='line' id='LC27'><span class="sd">  auth_token = self.request.get(&quot;oauth_token&quot;)</span></div><div class='line' id='LC28'><span class="sd">  auth_verifier = self.request.get(&quot;oauth_verifier&quot;)</span></div><div class='line' id='LC29'><span class="sd">  user_info = client.get_user_info(auth_token, auth_verifier=auth_verifier)</span></div><div class='line' id='LC30'><br/></div><div class='line' id='LC31'><span class="sd">  The &quot;user_info&quot; variable should then contain a dictionary of various</span></div><div class='line' id='LC32'><span class="sd">  user information (id, picture url, etc). What you do with that data is up</span></div><div class='line' id='LC33'><span class="sd">  to you.</span></div><div class='line' id='LC34'><br/></div><div class='line' id='LC35'><span class="sd">  That&#39;s it!</span></div><div class='line' id='LC36'><br/></div><div class='line' id='LC37'><span class="sd">4) If you need to, you can also call other other API URLs using</span></div><div class='line' id='LC38'><span class="sd">  client.make_request() as long as you supply a valid API URL and an access</span></div><div class='line' id='LC39'><span class="sd">  token and secret. Note, you may need to set method=urlfetch.POST.</span></div><div class='line' id='LC40'><br/></div><div class='line' id='LC41'><span class="sd">@author: Mike Knapp</span></div><div class='line' id='LC42'><span class="sd">@copyright: Unrestricted. Feel free to use modify however you see fit. Please</span></div><div class='line' id='LC43'><span class="sd">note however this software is unsupported. Please don&#39;t email me about it. :)</span></div><div class='line' id='LC44'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC45'><br/></div><div class='line' id='LC46'><span class="kn">from</span> <span class="nn">google.appengine.api</span> <span class="kn">import</span> <span class="n">memcache</span></div><div class='line' id='LC47'><span class="kn">from</span> <span class="nn">google.appengine.api</span> <span class="kn">import</span> <span class="n">urlfetch</span></div><div class='line' id='LC48'><span class="kn">from</span> <span class="nn">google.appengine.ext</span> <span class="kn">import</span> <span class="n">db</span></div><div class='line' id='LC49'><br/></div><div class='line' id='LC50'><span class="kn">from</span> <span class="nn">cgi</span> <span class="kn">import</span> <span class="n">parse_qs</span></div><div class='line' id='LC51'><span class="kn">from</span> <span class="nn">django.utils</span> <span class="kn">import</span> <span class="n">simplejson</span> <span class="k">as</span> <span class="n">json</span></div><div class='line' id='LC52'><span class="kn">from</span> <span class="nn">hashlib</span> <span class="kn">import</span> <span class="n">sha1</span></div><div class='line' id='LC53'><span class="kn">from</span> <span class="nn">hmac</span> <span class="kn">import</span> <span class="n">new</span> <span class="k">as</span> <span class="n">hmac</span></div><div class='line' id='LC54'><span class="kn">from</span> <span class="nn">random</span> <span class="kn">import</span> <span class="n">getrandbits</span></div><div class='line' id='LC55'><span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">time</span></div><div class='line' id='LC56'><span class="kn">from</span> <span class="nn">urllib</span> <span class="kn">import</span> <span class="n">urlencode</span></div><div class='line' id='LC57'><span class="kn">from</span> <span class="nn">urllib</span> <span class="kn">import</span> <span class="n">quote</span> <span class="k">as</span> <span class="n">urlquote</span></div><div class='line' id='LC58'><span class="kn">from</span> <span class="nn">urllib</span> <span class="kn">import</span> <span class="n">unquote</span> <span class="k">as</span> <span class="n">urlunquote</span></div><div class='line' id='LC59'><br/></div><div class='line' id='LC60'><span class="kn">import</span> <span class="nn">logging</span></div><div class='line' id='LC61'><br/></div><div class='line' id='LC62'><br/></div><div class='line' id='LC63'><span class="n">TWITTER</span> <span class="o">=</span> <span class="s">&quot;twitter&quot;</span></div><div class='line' id='LC64'><span class="n">YAHOO</span> <span class="o">=</span> <span class="s">&quot;yahoo&quot;</span></div><div class='line' id='LC65'><span class="n">MYSPACE</span> <span class="o">=</span> <span class="s">&quot;myspace&quot;</span></div><div class='line' id='LC66'><span class="n">DROPBOX</span> <span class="o">=</span> <span class="s">&quot;dropbox&quot;</span></div><div class='line' id='LC67'><span class="n">LINKEDIN</span> <span class="o">=</span> <span class="s">&quot;linkedin&quot;</span></div><div class='line' id='LC68'><span class="n">YAMMER</span> <span class="o">=</span> <span class="s">&quot;yammer&quot;</span></div><div class='line' id='LC69'><br/></div><div class='line' id='LC70'><br/></div><div class='line' id='LC71'><span class="k">class</span> <span class="nc">OAuthException</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span></div><div class='line' id='LC72'>&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC73'><br/></div><div class='line' id='LC74'><br/></div><div class='line' id='LC75'><span class="k">def</span> <span class="nf">get_oauth_client</span><span class="p">(</span><span class="n">service</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">secret</span><span class="p">,</span> <span class="n">callback_url</span><span class="p">):</span></div><div class='line' id='LC76'>&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Get OAuth Client.</span></div><div class='line' id='LC77'><br/></div><div class='line' id='LC78'><span class="sd">  A factory that will return the appropriate OAuth client.</span></div><div class='line' id='LC79'><span class="sd">  &quot;&quot;&quot;</span></div><div class='line' id='LC80'><br/></div><div class='line' id='LC81'>&nbsp;&nbsp;<span class="k">if</span> <span class="n">service</span> <span class="o">==</span> <span class="n">TWITTER</span><span class="p">:</span></div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">TwitterClient</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">secret</span><span class="p">,</span> <span class="n">callback_url</span><span class="p">)</span></div><div class='line' id='LC83'>&nbsp;&nbsp;<span class="k">elif</span> <span class="n">service</span> <span class="o">==</span> <span class="n">YAHOO</span><span class="p">:</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">YahooClient</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">secret</span><span class="p">,</span> <span class="n">callback_url</span><span class="p">)</span></div><div class='line' id='LC85'>&nbsp;&nbsp;<span class="k">elif</span> <span class="n">service</span> <span class="o">==</span> <span class="n">MYSPACE</span><span class="p">:</span></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">MySpaceClient</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">secret</span><span class="p">,</span> <span class="n">callback_url</span><span class="p">)</span></div><div class='line' id='LC87'>&nbsp;&nbsp;<span class="k">elif</span> <span class="n">service</span> <span class="o">==</span> <span class="n">DROPBOX</span><span class="p">:</span></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">DropboxClient</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">secret</span><span class="p">,</span> <span class="n">callback_url</span><span class="p">)</span></div><div class='line' id='LC89'>&nbsp;&nbsp;<span class="k">elif</span> <span class="n">service</span> <span class="o">==</span> <span class="n">LINKEDIN</span><span class="p">:</span></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">LinkedInClient</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">secret</span><span class="p">,</span> <span class="n">callback_url</span><span class="p">)</span></div><div class='line' id='LC91'>&nbsp;&nbsp;<span class="k">elif</span> <span class="n">service</span> <span class="o">==</span> <span class="n">YAMMER</span><span class="p">:</span></div><div class='line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">YammerClient</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">secret</span><span class="p">,</span> <span class="n">callback_url</span><span class="p">)</span></div><div class='line' id='LC93'>&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">Exception</span><span class="p">,</span> <span class="s">&quot;Unknown OAuth service </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">service</span></div><div class='line' id='LC95'><br/></div><div class='line' id='LC96'><br/></div><div class='line' id='LC97'><span class="k">class</span> <span class="nc">AuthToken</span><span class="p">(</span><span class="n">db</span><span class="o">.</span><span class="n">Model</span><span class="p">):</span></div><div class='line' id='LC98'>&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Auth Token.</span></div><div class='line' id='LC99'><br/></div><div class='line' id='LC100'><span class="sd">  A temporary auth token that we will use to authenticate a user with a</span></div><div class='line' id='LC101'><span class="sd">  third party website. (We need to store the data while the user visits</span></div><div class='line' id='LC102'><span class="sd">  the third party website to authenticate themselves.)</span></div><div class='line' id='LC103'><br/></div><div class='line' id='LC104'><span class="sd">  TODO: Implement a cron to clean out old tokens periodically.</span></div><div class='line' id='LC105'><span class="sd">  &quot;&quot;&quot;</span></div><div class='line' id='LC106'><br/></div><div class='line' id='LC107'>&nbsp;&nbsp;<span class="n">service</span> <span class="o">=</span> <span class="n">db</span><span class="o">.</span><span class="n">StringProperty</span><span class="p">(</span><span class="n">required</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC108'>&nbsp;&nbsp;<span class="n">token</span> <span class="o">=</span> <span class="n">db</span><span class="o">.</span><span class="n">StringProperty</span><span class="p">(</span><span class="n">required</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC109'>&nbsp;&nbsp;<span class="n">secret</span> <span class="o">=</span> <span class="n">db</span><span class="o">.</span><span class="n">StringProperty</span><span class="p">(</span><span class="n">required</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC110'>&nbsp;&nbsp;<span class="n">created</span> <span class="o">=</span> <span class="n">db</span><span class="o">.</span><span class="n">DateTimeProperty</span><span class="p">(</span><span class="n">auto_now_add</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC111'><br/></div><div class='line' id='LC112'><br/></div><div class='line' id='LC113'><span class="k">class</span> <span class="nc">OAuthClient</span><span class="p">():</span></div><div class='line' id='LC114'><br/></div><div class='line' id='LC115'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">service_name</span><span class="p">,</span> <span class="n">consumer_key</span><span class="p">,</span> <span class="n">consumer_secret</span><span class="p">,</span> <span class="n">request_url</span><span class="p">,</span></div><div class='line' id='LC116'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">access_url</span><span class="p">,</span> <span class="n">callback_url</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; Constructor.&quot;&quot;&quot;</span></div><div class='line' id='LC118'><br/></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">service_name</span> <span class="o">=</span> <span class="n">service_name</span></div><div class='line' id='LC120'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">consumer_key</span> <span class="o">=</span> <span class="n">consumer_key</span></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">consumer_secret</span> <span class="o">=</span> <span class="n">consumer_secret</span></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">request_url</span> <span class="o">=</span> <span class="n">request_url</span></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">access_url</span> <span class="o">=</span> <span class="n">access_url</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">callback_url</span> <span class="o">=</span> <span class="n">callback_url</span></div><div class='line' id='LC125'><br/></div><div class='line' id='LC126'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">prepare_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">,</span> <span class="n">token</span><span class="o">=</span><span class="s">&quot;&quot;</span><span class="p">,</span> <span class="n">secret</span><span class="o">=</span><span class="s">&quot;&quot;</span><span class="p">,</span> <span class="n">additional_params</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">method</span><span class="o">=</span><span class="n">urlfetch</span><span class="o">.</span><span class="n">GET</span><span class="p">,</span> <span class="n">t</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">nonce</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Prepare Request.</span></div><div class='line' id='LC129'><br/></div><div class='line' id='LC130'><span class="sd">    Prepares an authenticated request to any OAuth protected resource.</span></div><div class='line' id='LC131'><br/></div><div class='line' id='LC132'><span class="sd">    Returns the payload of the request.</span></div><div class='line' id='LC133'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC134'><br/></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">encode</span><span class="p">(</span><span class="n">text</span><span class="p">):</span></div><div class='line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">urlquote</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">text</span><span class="p">),</span> <span class="s">&quot;~&quot;</span><span class="p">)</span></div><div class='line' id='LC137'><br/></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">params</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;oauth_consumer_key&quot;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">consumer_key</span><span class="p">,</span></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;oauth_signature_method&quot;</span><span class="p">:</span> <span class="s">&quot;HMAC-SHA1&quot;</span><span class="p">,</span></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;oauth_timestamp&quot;</span><span class="p">:</span> <span class="n">t</span> <span class="k">if</span> <span class="n">t</span> <span class="k">else</span> <span class="nb">str</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">time</span><span class="p">())),</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;oauth_nonce&quot;</span><span class="p">:</span> <span class="n">nonce</span> <span class="k">if</span> <span class="n">nonce</span> <span class="k">else</span> <span class="nb">str</span><span class="p">(</span><span class="n">getrandbits</span><span class="p">(</span><span class="mi">64</span><span class="p">)),</span></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;oauth_version&quot;</span><span class="p">:</span> <span class="s">&quot;1.0&quot;</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC145'><br/></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">token</span><span class="p">:</span></div><div class='line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">params</span><span class="p">[</span><span class="s">&quot;oauth_token&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">token</span></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_url</span><span class="p">:</span></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">params</span><span class="p">[</span><span class="s">&quot;oauth_callback&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_url</span></div><div class='line' id='LC150'><br/></div><div class='line' id='LC151'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">additional_params</span><span class="p">:</span></div><div class='line' id='LC152'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">params</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">additional_params</span><span class="p">)</span></div><div class='line' id='LC153'><br/></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">k</span><span class="p">,</span><span class="n">v</span> <span class="ow">in</span> <span class="n">params</span><span class="o">.</span><span class="n">items</span><span class="p">():</span></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">v</span><span class="p">,</span> <span class="nb">unicode</span><span class="p">):</span></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">params</span><span class="p">[</span><span class="n">k</span><span class="p">]</span> <span class="o">=</span> <span class="n">v</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s">&#39;utf8&#39;</span><span class="p">)</span></div><div class='line' id='LC157'><br/></div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Join all of the params together.</span></div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">params_str</span> <span class="o">=</span> <span class="s">&quot;&amp;&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="s">&quot;</span><span class="si">%s</span><span class="s">=</span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">encode</span><span class="p">(</span><span class="n">k</span><span class="p">),</span> <span class="n">encode</span><span class="p">(</span><span class="n">params</span><span class="p">[</span><span class="n">k</span><span class="p">]))</span></div><div class='line' id='LC160'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">k</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">params</span><span class="p">)])</span></div><div class='line' id='LC161'><br/></div><div class='line' id='LC162'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Join the entire message together per the OAuth specification.</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">message</span> <span class="o">=</span> <span class="s">&quot;&amp;&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="s">&quot;GET&quot;</span> <span class="k">if</span> <span class="n">method</span> <span class="o">==</span> <span class="n">urlfetch</span><span class="o">.</span><span class="n">GET</span> <span class="k">else</span> <span class="s">&quot;POST&quot;</span><span class="p">,</span></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">encode</span><span class="p">(</span><span class="n">url</span><span class="p">),</span> <span class="n">encode</span><span class="p">(</span><span class="n">params_str</span><span class="p">)])</span></div><div class='line' id='LC165'><br/></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Create a HMAC-SHA1 signature of the message.</span></div><div class='line' id='LC167'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">key</span> <span class="o">=</span> <span class="s">&quot;</span><span class="si">%s</span><span class="s">&amp;</span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">consumer_secret</span><span class="p">,</span> <span class="n">secret</span><span class="p">)</span> <span class="c"># Note compulsory &quot;&amp;&quot;.</span></div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">signature</span> <span class="o">=</span> <span class="n">hmac</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">message</span><span class="p">,</span> <span class="n">sha1</span><span class="p">)</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">digest_base64</span> <span class="o">=</span> <span class="n">signature</span><span class="o">.</span><span class="n">digest</span><span class="p">()</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s">&quot;base64&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC170'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">params</span><span class="p">[</span><span class="s">&quot;oauth_signature&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">digest_base64</span></div><div class='line' id='LC171'><br/></div><div class='line' id='LC172'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Construct the request payload and return it</span></div><div class='line' id='LC173'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">urlencode</span><span class="p">(</span><span class="n">params</span><span class="p">)</span></div><div class='line' id='LC174'><br/></div><div class='line' id='LC175'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">make_async_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">,</span> <span class="n">token</span><span class="o">=</span><span class="s">&quot;&quot;</span><span class="p">,</span> <span class="n">secret</span><span class="o">=</span><span class="s">&quot;&quot;</span><span class="p">,</span> <span class="n">additional_params</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></div><div class='line' id='LC176'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">protected</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="n">urlfetch</span><span class="o">.</span><span class="n">GET</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="p">{}):</span></div><div class='line' id='LC177'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Make Request.</span></div><div class='line' id='LC178'><br/></div><div class='line' id='LC179'><span class="sd">    Make an authenticated request to any OAuth protected resource.</span></div><div class='line' id='LC180'><br/></div><div class='line' id='LC181'><span class="sd">    If protected is equal to True, the Authorization: OAuth header will be set.</span></div><div class='line' id='LC182'><br/></div><div class='line' id='LC183'><span class="sd">    A urlfetch response object is returned.</span></div><div class='line' id='LC184'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC185'><br/></div><div class='line' id='LC186'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">payload</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">prepare_request</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">token</span><span class="p">,</span> <span class="n">secret</span><span class="p">,</span> <span class="n">additional_params</span><span class="p">,</span></div><div class='line' id='LC187'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">method</span><span class="p">)</span></div><div class='line' id='LC188'><br/></div><div class='line' id='LC189'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">method</span> <span class="o">==</span> <span class="n">urlfetch</span><span class="o">.</span><span class="n">GET</span><span class="p">:</span></div><div class='line' id='LC190'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">url</span> <span class="o">=</span> <span class="s">&quot;</span><span class="si">%s</span><span class="s">?</span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">payload</span><span class="p">)</span></div><div class='line' id='LC191'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">payload</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC192'><br/></div><div class='line' id='LC193'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">protected</span><span class="p">:</span></div><div class='line' id='LC194'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">headers</span><span class="p">[</span><span class="s">&quot;Authorization&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="s">&quot;OAuth&quot;</span></div><div class='line' id='LC195'><br/></div><div class='line' id='LC196'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rpc</span> <span class="o">=</span> <span class="n">urlfetch</span><span class="o">.</span><span class="n">create_rpc</span><span class="p">(</span><span class="n">deadline</span><span class="o">=</span><span class="mf">10.0</span><span class="p">)</span></div><div class='line' id='LC197'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">urlfetch</span><span class="o">.</span><span class="n">make_fetch_call</span><span class="p">(</span><span class="n">rpc</span><span class="p">,</span> <span class="n">url</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="n">method</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span></div><div class='line' id='LC198'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">payload</span><span class="o">=</span><span class="n">payload</span><span class="p">)</span></div><div class='line' id='LC199'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">rpc</span></div><div class='line' id='LC200'><br/></div><div class='line' id='LC201'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">make_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">,</span> <span class="n">token</span><span class="o">=</span><span class="s">&quot;&quot;</span><span class="p">,</span> <span class="n">secret</span><span class="o">=</span><span class="s">&quot;&quot;</span><span class="p">,</span> <span class="n">additional_params</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></div><div class='line' id='LC202'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">protected</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="n">urlfetch</span><span class="o">.</span><span class="n">GET</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="p">{}):</span></div><div class='line' id='LC203'><br/></div><div class='line' id='LC204'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">make_async_request</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">token</span><span class="p">,</span> <span class="n">secret</span><span class="p">,</span> <span class="n">additional_params</span><span class="p">,</span></div><div class='line' id='LC205'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">protected</span><span class="p">,</span> <span class="n">method</span><span class="p">,</span> <span class="n">headers</span><span class="p">)</span><span class="o">.</span><span class="n">get_result</span><span class="p">()</span></div><div class='line' id='LC206'><br/></div><div class='line' id='LC207'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_authorization_url</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC208'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Get Authorization URL.</span></div><div class='line' id='LC209'><br/></div><div class='line' id='LC210'><span class="sd">    Returns a service specific URL which contains an auth token. The user</span></div><div class='line' id='LC211'><span class="sd">    should be redirected to this URL so that they can give consent to be</span></div><div class='line' id='LC212'><span class="sd">    logged in.</span></div><div class='line' id='LC213'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC214'><br/></div><div class='line' id='LC215'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">,</span> <span class="s">&quot;Must be implemented by a subclass&quot;</span></div><div class='line' id='LC216'><br/></div><div class='line' id='LC217'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_user_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">auth_token</span><span class="p">,</span> <span class="n">auth_verifier</span><span class="o">=</span><span class="s">&quot;&quot;</span><span class="p">):</span></div><div class='line' id='LC218'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Get User Info.</span></div><div class='line' id='LC219'><br/></div><div class='line' id='LC220'><span class="sd">    Exchanges the auth token for an access token and returns a dictionary</span></div><div class='line' id='LC221'><span class="sd">    of information about the authenticated user.</span></div><div class='line' id='LC222'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC223'><br/></div><div class='line' id='LC224'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">auth_token</span> <span class="o">=</span> <span class="n">urlunquote</span><span class="p">(</span><span class="n">auth_token</span><span class="p">)</span></div><div class='line' id='LC225'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">auth_verifier</span> <span class="o">=</span> <span class="n">urlunquote</span><span class="p">(</span><span class="n">auth_verifier</span><span class="p">)</span></div><div class='line' id='LC226'><br/></div><div class='line' id='LC227'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">auth_secret</span> <span class="o">=</span> <span class="n">memcache</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_memcache_auth_key</span><span class="p">(</span><span class="n">auth_token</span><span class="p">))</span></div><div class='line' id='LC228'><br/></div><div class='line' id='LC229'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">auth_secret</span><span class="p">:</span></div><div class='line' id='LC230'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span> <span class="o">=</span> <span class="n">AuthToken</span><span class="o">.</span><span class="n">gql</span><span class="p">(</span><span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC231'><span class="s">        WHERE</span></div><div class='line' id='LC232'><span class="s">          service = :1 AND</span></div><div class='line' id='LC233'><span class="s">          token = :2</span></div><div class='line' id='LC234'><span class="s">        LIMIT</span></div><div class='line' id='LC235'><span class="s">          1</span></div><div class='line' id='LC236'><span class="s">      &quot;&quot;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">service_name</span><span class="p">,</span> <span class="n">auth_token</span><span class="p">)</span><span class="o">.</span><span class="n">get</span><span class="p">()</span></div><div class='line' id='LC237'><br/></div><div class='line' id='LC238'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">result</span><span class="p">:</span></div><div class='line' id='LC239'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logging</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&quot;The auth token </span><span class="si">%s</span><span class="s"> was not found in our db&quot;</span> <span class="o">%</span> <span class="n">auth_token</span><span class="p">)</span></div><div class='line' id='LC240'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">Exception</span><span class="p">,</span> <span class="s">&quot;Could not find Auth Token in database&quot;</span></div><div class='line' id='LC241'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC242'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">auth_secret</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">secret</span></div><div class='line' id='LC243'><br/></div><div class='line' id='LC244'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">make_request</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">access_url</span><span class="p">,</span></div><div class='line' id='LC245'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">token</span><span class="o">=</span><span class="n">auth_token</span><span class="p">,</span></div><div class='line' id='LC246'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">secret</span><span class="o">=</span><span class="n">auth_secret</span><span class="p">,</span></div><div class='line' id='LC247'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">additional_params</span><span class="o">=</span><span class="p">{</span><span class="s">&quot;oauth_verifier&quot;</span><span class="p">:</span></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">auth_verifier</span><span class="p">})</span></div><div class='line' id='LC249'><br/></div><div class='line' id='LC250'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Extract the access token/secret from the response.</span></div><div class='line' id='LC251'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extract_credentials</span><span class="p">(</span><span class="n">response</span><span class="p">)</span></div><div class='line' id='LC252'><br/></div><div class='line' id='LC253'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Try to collect some information about this user from the service.</span></div><div class='line' id='LC254'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_lookup_user_info</span><span class="p">(</span><span class="n">result</span><span class="p">[</span><span class="s">&quot;token&quot;</span><span class="p">],</span> <span class="n">result</span><span class="p">[</span><span class="s">&quot;secret&quot;</span><span class="p">])</span></div><div class='line' id='LC255'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">result</span><span class="p">)</span></div><div class='line' id='LC256'><br/></div><div class='line' id='LC257'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">user_info</span></div><div class='line' id='LC258'><br/></div><div class='line' id='LC259'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_get_auth_token</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC260'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Get Authorization Token.</span></div><div class='line' id='LC261'><br/></div><div class='line' id='LC262'><span class="sd">    Actually gets the authorization token and secret from the service. The</span></div><div class='line' id='LC263'><span class="sd">    token and secret are stored in our database, and the auth token is</span></div><div class='line' id='LC264'><span class="sd">    returned.</span></div><div class='line' id='LC265'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC266'><br/></div><div class='line' id='LC267'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">make_request</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">request_url</span><span class="p">)</span></div><div class='line' id='LC268'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extract_credentials</span><span class="p">(</span><span class="n">response</span><span class="p">)</span></div><div class='line' id='LC269'><br/></div><div class='line' id='LC270'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">auth_token</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s">&quot;token&quot;</span><span class="p">]</span></div><div class='line' id='LC271'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">auth_secret</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s">&quot;secret&quot;</span><span class="p">]</span></div><div class='line' id='LC272'><br/></div><div class='line' id='LC273'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Save the auth token and secret in our database.</span></div><div class='line' id='LC274'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">auth</span> <span class="o">=</span> <span class="n">AuthToken</span><span class="p">(</span><span class="n">service</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">service_name</span><span class="p">,</span></div><div class='line' id='LC275'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">token</span><span class="o">=</span><span class="n">auth_token</span><span class="p">,</span></div><div class='line' id='LC276'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">secret</span><span class="o">=</span><span class="n">auth_secret</span><span class="p">)</span></div><div class='line' id='LC277'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">auth</span><span class="o">.</span><span class="n">put</span><span class="p">()</span></div><div class='line' id='LC278'><br/></div><div class='line' id='LC279'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Add the secret to memcache as well.</span></div><div class='line' id='LC280'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">memcache</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_memcache_auth_key</span><span class="p">(</span><span class="n">auth_token</span><span class="p">),</span> <span class="n">auth_secret</span><span class="p">,</span></div><div class='line' id='LC281'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">time</span><span class="o">=</span><span class="mi">20</span><span class="o">*</span><span class="mi">60</span><span class="p">)</span></div><div class='line' id='LC282'><br/></div><div class='line' id='LC283'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">auth_token</span></div><div class='line' id='LC284'><br/></div><div class='line' id='LC285'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_get_memcache_auth_key</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">auth_token</span><span class="p">):</span></div><div class='line' id='LC286'><br/></div><div class='line' id='LC287'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&quot;oauth_</span><span class="si">%s</span><span class="s">_</span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service_name</span><span class="p">,</span> <span class="n">auth_token</span><span class="p">)</span></div><div class='line' id='LC288'><br/></div><div class='line' id='LC289'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_extract_credentials</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result</span><span class="p">):</span></div><div class='line' id='LC290'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Extract Credentials.</span></div><div class='line' id='LC291'><br/></div><div class='line' id='LC292'><span class="sd">    Returns an dictionary containing the token and secret (if present).</span></div><div class='line' id='LC293'><span class="sd">    Throws an Exception otherwise.</span></div><div class='line' id='LC294'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC295'><br/></div><div class='line' id='LC296'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">token</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC297'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">secret</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC298'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parsed_results</span> <span class="o">=</span> <span class="n">parse_qs</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">content</span><span class="p">)</span></div><div class='line' id='LC299'><br/></div><div class='line' id='LC300'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&quot;oauth_token&quot;</span> <span class="ow">in</span> <span class="n">parsed_results</span><span class="p">:</span></div><div class='line' id='LC301'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">token</span> <span class="o">=</span> <span class="n">parsed_results</span><span class="p">[</span><span class="s">&quot;oauth_token&quot;</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC302'><br/></div><div class='line' id='LC303'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&quot;oauth_token_secret&quot;</span> <span class="ow">in</span> <span class="n">parsed_results</span><span class="p">:</span></div><div class='line' id='LC304'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">secret</span> <span class="o">=</span> <span class="n">parsed_results</span><span class="p">[</span><span class="s">&quot;oauth_token_secret&quot;</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC305'><br/></div><div class='line' id='LC306'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="n">token</span> <span class="ow">and</span> <span class="n">secret</span><span class="p">)</span> <span class="ow">or</span> <span class="n">result</span><span class="o">.</span><span class="n">status_code</span> <span class="o">!=</span> <span class="mi">200</span><span class="p">:</span></div><div class='line' id='LC307'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logging</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&quot;Could not extract token/secret: </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">result</span><span class="o">.</span><span class="n">content</span><span class="p">)</span></div><div class='line' id='LC308'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">OAuthException</span><span class="p">(</span><span class="s">&quot;Problem talking to the service&quot;</span><span class="p">)</span></div><div class='line' id='LC309'><br/></div><div class='line' id='LC310'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">{</span></div><div class='line' id='LC311'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;service&quot;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">service_name</span><span class="p">,</span></div><div class='line' id='LC312'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;token&quot;</span><span class="p">:</span> <span class="n">token</span><span class="p">,</span></div><div class='line' id='LC313'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;secret&quot;</span><span class="p">:</span> <span class="n">secret</span></div><div class='line' id='LC314'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC315'><br/></div><div class='line' id='LC316'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_lookup_user_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">access_token</span><span class="p">,</span> <span class="n">access_secret</span><span class="p">):</span></div><div class='line' id='LC317'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Lookup User Info.</span></div><div class='line' id='LC318'><br/></div><div class='line' id='LC319'><span class="sd">    Complies a dictionary describing the user. The user should be</span></div><div class='line' id='LC320'><span class="sd">    authenticated at this point. Each different client should override</span></div><div class='line' id='LC321'><span class="sd">    this method.</span></div><div class='line' id='LC322'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC323'><br/></div><div class='line' id='LC324'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">,</span> <span class="s">&quot;Must be implemented by a subclass&quot;</span></div><div class='line' id='LC325'><br/></div><div class='line' id='LC326'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_get_default_user_info</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC327'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Get Default User Info.</span></div><div class='line' id='LC328'><br/></div><div class='line' id='LC329'><span class="sd">    Returns a blank array that can be used to populate generalized user</span></div><div class='line' id='LC330'><span class="sd">    information.</span></div><div class='line' id='LC331'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC332'><br/></div><div class='line' id='LC333'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">{</span></div><div class='line' id='LC334'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;id&quot;</span><span class="p">:</span> <span class="s">&quot;&quot;</span><span class="p">,</span></div><div class='line' id='LC335'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;username&quot;</span><span class="p">:</span> <span class="s">&quot;&quot;</span><span class="p">,</span></div><div class='line' id='LC336'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;name&quot;</span><span class="p">:</span> <span class="s">&quot;&quot;</span><span class="p">,</span></div><div class='line' id='LC337'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;picture&quot;</span><span class="p">:</span> <span class="s">&quot;&quot;</span></div><div class='line' id='LC338'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC339'><br/></div><div class='line' id='LC340'><br/></div><div class='line' id='LC341'><span class="k">class</span> <span class="nc">TwitterClient</span><span class="p">(</span><span class="n">OAuthClient</span><span class="p">):</span></div><div class='line' id='LC342'>&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Twitter Client.</span></div><div class='line' id='LC343'><br/></div><div class='line' id='LC344'><span class="sd">  A client for talking to the Twitter API using OAuth as the</span></div><div class='line' id='LC345'><span class="sd">  authentication model.</span></div><div class='line' id='LC346'><span class="sd">  &quot;&quot;&quot;</span></div><div class='line' id='LC347'><br/></div><div class='line' id='LC348'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">consumer_key</span><span class="p">,</span> <span class="n">consumer_secret</span><span class="p">,</span> <span class="n">callback_url</span><span class="p">):</span></div><div class='line' id='LC349'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Constructor.&quot;&quot;&quot;</span></div><div class='line' id='LC350'><br/></div><div class='line' id='LC351'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">OAuthClient</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span></div><div class='line' id='LC352'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">TWITTER</span><span class="p">,</span></div><div class='line' id='LC353'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">consumer_key</span><span class="p">,</span></div><div class='line' id='LC354'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">consumer_secret</span><span class="p">,</span></div><div class='line' id='LC355'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;http://api.twitter.com/oauth/request_token&quot;</span><span class="p">,</span></div><div class='line' id='LC356'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;http://api.twitter.com/oauth/access_token&quot;</span><span class="p">,</span></div><div class='line' id='LC357'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">callback_url</span><span class="p">)</span></div><div class='line' id='LC358'><br/></div><div class='line' id='LC359'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_authorization_url</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC360'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Get Authorization URL.&quot;&quot;&quot;</span></div><div class='line' id='LC361'><br/></div><div class='line' id='LC362'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_auth_token</span><span class="p">()</span></div><div class='line' id='LC363'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&quot;http://api.twitter.com/oauth/authorize?oauth_token=</span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">token</span></div><div class='line' id='LC364'><br/></div><div class='line' id='LC365'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_authenticate_url</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC366'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Get Authentication URL.&quot;&quot;&quot;</span></div><div class='line' id='LC367'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_auth_token</span><span class="p">()</span></div><div class='line' id='LC368'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&quot;http://api.twitter.com/oauth/authenticate?oauth_token=</span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">token</span></div><div class='line' id='LC369'><br/></div><div class='line' id='LC370'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_lookup_user_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">access_token</span><span class="p">,</span> <span class="n">access_secret</span><span class="p">):</span></div><div class='line' id='LC371'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Lookup User Info.</span></div><div class='line' id='LC372'><br/></div><div class='line' id='LC373'><span class="sd">    Lookup the user on Twitter.</span></div><div class='line' id='LC374'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC375'><br/></div><div class='line' id='LC376'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">make_request</span><span class="p">(</span></div><div class='line' id='LC377'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;http://api.twitter.com/account/verify_credentials.json&quot;</span><span class="p">,</span></div><div class='line' id='LC378'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">token</span><span class="o">=</span><span class="n">access_token</span><span class="p">,</span> <span class="n">secret</span><span class="o">=</span><span class="n">access_secret</span><span class="p">,</span> <span class="n">protected</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC379'><br/></div><div class='line' id='LC380'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">)</span></div><div class='line' id='LC381'><br/></div><div class='line' id='LC382'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_default_user_info</span><span class="p">()</span></div><div class='line' id='LC383'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;id&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;id&quot;</span><span class="p">]</span></div><div class='line' id='LC384'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;username&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;screen_name&quot;</span><span class="p">]</span></div><div class='line' id='LC385'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;name&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;name&quot;</span><span class="p">]</span></div><div class='line' id='LC386'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;picture&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;profile_image_url&quot;</span><span class="p">]</span></div><div class='line' id='LC387'><br/></div><div class='line' id='LC388'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">user_info</span></div><div class='line' id='LC389'><br/></div><div class='line' id='LC390'><br/></div><div class='line' id='LC391'><span class="k">class</span> <span class="nc">MySpaceClient</span><span class="p">(</span><span class="n">OAuthClient</span><span class="p">):</span></div><div class='line' id='LC392'>&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;MySpace Client.</span></div><div class='line' id='LC393'><br/></div><div class='line' id='LC394'><span class="sd">  A client for talking to the MySpace API using OAuth as the</span></div><div class='line' id='LC395'><span class="sd">  authentication model.</span></div><div class='line' id='LC396'><span class="sd">  &quot;&quot;&quot;</span></div><div class='line' id='LC397'><br/></div><div class='line' id='LC398'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">consumer_key</span><span class="p">,</span> <span class="n">consumer_secret</span><span class="p">,</span> <span class="n">callback_url</span><span class="p">):</span></div><div class='line' id='LC399'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Constructor.&quot;&quot;&quot;</span></div><div class='line' id='LC400'><br/></div><div class='line' id='LC401'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">OAuthClient</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span></div><div class='line' id='LC402'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">MYSPACE</span><span class="p">,</span></div><div class='line' id='LC403'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">consumer_key</span><span class="p">,</span></div><div class='line' id='LC404'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">consumer_secret</span><span class="p">,</span></div><div class='line' id='LC405'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;http://api.myspace.com/request_token&quot;</span><span class="p">,</span></div><div class='line' id='LC406'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;http://api.myspace.com/access_token&quot;</span><span class="p">,</span></div><div class='line' id='LC407'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">callback_url</span><span class="p">)</span></div><div class='line' id='LC408'><br/></div><div class='line' id='LC409'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_authorization_url</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC410'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Get Authorization URL.&quot;&quot;&quot;</span></div><div class='line' id='LC411'><br/></div><div class='line' id='LC412'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_auth_token</span><span class="p">()</span></div><div class='line' id='LC413'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">(</span><span class="s">&quot;http://api.myspace.com/authorize?oauth_token=</span><span class="si">%s</span><span class="s">&quot;</span></div><div class='line' id='LC414'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp;oauth_callback=</span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">token</span><span class="p">,</span> <span class="n">urlquote</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">callback_url</span><span class="p">)))</span></div><div class='line' id='LC415'><br/></div><div class='line' id='LC416'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_lookup_user_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">access_token</span><span class="p">,</span> <span class="n">access_secret</span><span class="p">):</span></div><div class='line' id='LC417'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Lookup User Info.</span></div><div class='line' id='LC418'><br/></div><div class='line' id='LC419'><span class="sd">    Lookup the user on MySpace.</span></div><div class='line' id='LC420'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC421'><br/></div><div class='line' id='LC422'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">make_request</span><span class="p">(</span><span class="s">&quot;http://api.myspace.com/v1/user.json&quot;</span><span class="p">,</span></div><div class='line' id='LC423'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">token</span><span class="o">=</span><span class="n">access_token</span><span class="p">,</span> <span class="n">secret</span><span class="o">=</span><span class="n">access_secret</span><span class="p">,</span> <span class="n">protected</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC424'><br/></div><div class='line' id='LC425'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">)</span></div><div class='line' id='LC426'><br/></div><div class='line' id='LC427'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_default_user_info</span><span class="p">()</span></div><div class='line' id='LC428'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;id&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;userId&quot;</span><span class="p">]</span></div><div class='line' id='LC429'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">username</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;webUri&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;http://www.myspace.com/&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">)</span></div><div class='line' id='LC430'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;username&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">username</span></div><div class='line' id='LC431'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;name&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;name&quot;</span><span class="p">]</span></div><div class='line' id='LC432'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;picture&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;image&quot;</span><span class="p">]</span></div><div class='line' id='LC433'><br/></div><div class='line' id='LC434'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">user_info</span></div><div class='line' id='LC435'><br/></div><div class='line' id='LC436'><br/></div><div class='line' id='LC437'><span class="k">class</span> <span class="nc">YahooClient</span><span class="p">(</span><span class="n">OAuthClient</span><span class="p">):</span></div><div class='line' id='LC438'>&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Yahoo! Client.</span></div><div class='line' id='LC439'><br/></div><div class='line' id='LC440'><span class="sd">  A client for talking to the Yahoo! API using OAuth as the</span></div><div class='line' id='LC441'><span class="sd">  authentication model.</span></div><div class='line' id='LC442'><span class="sd">  &quot;&quot;&quot;</span></div><div class='line' id='LC443'><br/></div><div class='line' id='LC444'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">consumer_key</span><span class="p">,</span> <span class="n">consumer_secret</span><span class="p">,</span> <span class="n">callback_url</span><span class="p">):</span></div><div class='line' id='LC445'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Constructor.&quot;&quot;&quot;</span></div><div class='line' id='LC446'><br/></div><div class='line' id='LC447'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">OAuthClient</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span></div><div class='line' id='LC448'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">YAHOO</span><span class="p">,</span></div><div class='line' id='LC449'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">consumer_key</span><span class="p">,</span></div><div class='line' id='LC450'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">consumer_secret</span><span class="p">,</span></div><div class='line' id='LC451'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;https://api.login.yahoo.com/oauth/v2/get_request_token&quot;</span><span class="p">,</span></div><div class='line' id='LC452'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;https://api.login.yahoo.com/oauth/v2/get_token&quot;</span><span class="p">,</span></div><div class='line' id='LC453'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">callback_url</span><span class="p">)</span></div><div class='line' id='LC454'><br/></div><div class='line' id='LC455'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_authorization_url</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC456'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Get Authorization URL.&quot;&quot;&quot;</span></div><div class='line' id='LC457'><br/></div><div class='line' id='LC458'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_auth_token</span><span class="p">()</span></div><div class='line' id='LC459'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">(</span><span class="s">&quot;https://api.login.yahoo.com/oauth/v2/request_auth?oauth_token=</span><span class="si">%s</span><span class="s">&quot;</span></div><div class='line' id='LC460'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="o">%</span> <span class="n">token</span><span class="p">)</span></div><div class='line' id='LC461'><br/></div><div class='line' id='LC462'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_lookup_user_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">access_token</span><span class="p">,</span> <span class="n">access_secret</span><span class="p">):</span></div><div class='line' id='LC463'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Lookup User Info.</span></div><div class='line' id='LC464'><br/></div><div class='line' id='LC465'><span class="sd">    Lookup the user on Yahoo!</span></div><div class='line' id='LC466'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC467'><br/></div><div class='line' id='LC468'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_default_user_info</span><span class="p">()</span></div><div class='line' id='LC469'><br/></div><div class='line' id='LC470'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># 1) Obtain the user&#39;s GUID.</span></div><div class='line' id='LC471'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">make_request</span><span class="p">(</span></div><div class='line' id='LC472'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;http://social.yahooapis.com/v1/me/guid&quot;</span><span class="p">,</span> <span class="n">token</span><span class="o">=</span><span class="n">access_token</span><span class="p">,</span></div><div class='line' id='LC473'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">secret</span><span class="o">=</span><span class="n">access_secret</span><span class="p">,</span> <span class="n">additional_params</span><span class="o">=</span><span class="p">{</span><span class="s">&quot;format&quot;</span><span class="p">:</span> <span class="s">&quot;json&quot;</span><span class="p">},</span></div><div class='line' id='LC474'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">protected</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC475'><br/></div><div class='line' id='LC476'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">)[</span><span class="s">&quot;guid&quot;</span><span class="p">]</span></div><div class='line' id='LC477'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">guid</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;value&quot;</span><span class="p">]</span></div><div class='line' id='LC478'><br/></div><div class='line' id='LC479'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># 2) Inspect the user&#39;s profile.</span></div><div class='line' id='LC480'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">make_request</span><span class="p">(</span></div><div class='line' id='LC481'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;http://social.yahooapis.com/v1/user/</span><span class="si">%s</span><span class="s">/profile/usercard&quot;</span> <span class="o">%</span> <span class="n">guid</span><span class="p">,</span></div><div class='line' id='LC482'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">token</span><span class="o">=</span><span class="n">access_token</span><span class="p">,</span> <span class="n">secret</span><span class="o">=</span><span class="n">access_secret</span><span class="p">,</span></div><div class='line' id='LC483'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">additional_params</span><span class="o">=</span><span class="p">{</span><span class="s">&quot;format&quot;</span><span class="p">:</span> <span class="s">&quot;json&quot;</span><span class="p">},</span> <span class="n">protected</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC484'><br/></div><div class='line' id='LC485'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">)[</span><span class="s">&quot;profile&quot;</span><span class="p">]</span></div><div class='line' id='LC486'><br/></div><div class='line' id='LC487'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;id&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">guid</span></div><div class='line' id='LC488'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;username&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;nickname&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span></div><div class='line' id='LC489'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;name&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;nickname&quot;</span><span class="p">]</span></div><div class='line' id='LC490'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;picture&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;image&quot;</span><span class="p">][</span><span class="s">&quot;imageUrl&quot;</span><span class="p">]</span></div><div class='line' id='LC491'><br/></div><div class='line' id='LC492'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">user_info</span></div><div class='line' id='LC493'><br/></div><div class='line' id='LC494'><br/></div><div class='line' id='LC495'><span class="k">class</span> <span class="nc">DropboxClient</span><span class="p">(</span><span class="n">OAuthClient</span><span class="p">):</span></div><div class='line' id='LC496'>&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Dropbox Client.</span></div><div class='line' id='LC497'><br/></div><div class='line' id='LC498'><span class="sd">  A client for talking to the Dropbox API using OAuth as the authentication</span></div><div class='line' id='LC499'><span class="sd">  model.</span></div><div class='line' id='LC500'><span class="sd">  &quot;&quot;&quot;</span></div><div class='line' id='LC501'><br/></div><div class='line' id='LC502'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">consumer_key</span><span class="p">,</span> <span class="n">consumer_secret</span><span class="p">,</span> <span class="n">callback_url</span><span class="p">):</span></div><div class='line' id='LC503'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Constructor.&quot;&quot;&quot;</span></div><div class='line' id='LC504'><br/></div><div class='line' id='LC505'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">OAuthClient</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span></div><div class='line' id='LC506'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">DROPBOX</span><span class="p">,</span></div><div class='line' id='LC507'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">consumer_key</span><span class="p">,</span></div><div class='line' id='LC508'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">consumer_secret</span><span class="p">,</span></div><div class='line' id='LC509'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;https://api.dropbox.com/0/oauth/request_token&quot;</span><span class="p">,</span></div><div class='line' id='LC510'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;https://api.dropbox.com/0/oauth/access_token&quot;</span><span class="p">,</span></div><div class='line' id='LC511'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">callback_url</span><span class="p">)</span></div><div class='line' id='LC512'><br/></div><div class='line' id='LC513'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_authorization_url</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC514'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Get Authorization URL.&quot;&quot;&quot;</span></div><div class='line' id='LC515'><br/></div><div class='line' id='LC516'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_auth_token</span><span class="p">()</span></div><div class='line' id='LC517'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">(</span><span class="s">&quot;http://www.dropbox.com/0/oauth/authorize?&quot;</span></div><div class='line' id='LC518'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;oauth_token=</span><span class="si">%s</span><span class="s">&amp;oauth_callback=</span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">token</span><span class="p">,</span></div><div class='line' id='LC519'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">urlquote</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">callback_url</span><span class="p">)))</span></div><div class='line' id='LC520'><br/></div><div class='line' id='LC521'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_lookup_user_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">access_token</span><span class="p">,</span> <span class="n">access_secret</span><span class="p">):</span></div><div class='line' id='LC522'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Lookup User Info.</span></div><div class='line' id='LC523'><br/></div><div class='line' id='LC524'><span class="sd">    Lookup the user on Dropbox.</span></div><div class='line' id='LC525'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC526'><br/></div><div class='line' id='LC527'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">make_request</span><span class="p">(</span><span class="s">&quot;http://api.dropbox.com/0/account/info&quot;</span><span class="p">,</span></div><div class='line' id='LC528'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">token</span><span class="o">=</span><span class="n">access_token</span><span class="p">,</span> <span class="n">secret</span><span class="o">=</span><span class="n">access_secret</span><span class="p">,</span></div><div class='line' id='LC529'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">protected</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC530'><br/></div><div class='line' id='LC531'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">)</span></div><div class='line' id='LC532'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_default_user_info</span><span class="p">()</span></div><div class='line' id='LC533'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;id&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;uid&quot;</span><span class="p">]</span></div><div class='line' id='LC534'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;name&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;display_name&quot;</span><span class="p">]</span></div><div class='line' id='LC535'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;country&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;country&quot;</span><span class="p">]</span></div><div class='line' id='LC536'><br/></div><div class='line' id='LC537'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">user_info</span></div><div class='line' id='LC538'><br/></div><div class='line' id='LC539'><br/></div><div class='line' id='LC540'><span class="k">class</span> <span class="nc">LinkedInClient</span><span class="p">(</span><span class="n">OAuthClient</span><span class="p">):</span></div><div class='line' id='LC541'>&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;LinkedIn Client.</span></div><div class='line' id='LC542'><br/></div><div class='line' id='LC543'><span class="sd">  A client for talking to the LinkedIn API using OAuth as the</span></div><div class='line' id='LC544'><span class="sd">  authentication model.</span></div><div class='line' id='LC545'><span class="sd">  &quot;&quot;&quot;</span></div><div class='line' id='LC546'><br/></div><div class='line' id='LC547'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">consumer_key</span><span class="p">,</span> <span class="n">consumer_secret</span><span class="p">,</span> <span class="n">callback_url</span><span class="p">):</span></div><div class='line' id='LC548'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Constructor.&quot;&quot;&quot;</span></div><div class='line' id='LC549'><br/></div><div class='line' id='LC550'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">OAuthClient</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span></div><div class='line' id='LC551'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LINKEDIN</span><span class="p">,</span></div><div class='line' id='LC552'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">consumer_key</span><span class="p">,</span></div><div class='line' id='LC553'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">consumer_secret</span><span class="p">,</span></div><div class='line' id='LC554'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;https://api.linkedin.com/uas/oauth/requestToken&quot;</span><span class="p">,</span></div><div class='line' id='LC555'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;https://api.linkedin.com/uas/oauth/accessToken&quot;</span><span class="p">,</span></div><div class='line' id='LC556'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">callback_url</span><span class="p">)</span></div><div class='line' id='LC557'><br/></div><div class='line' id='LC558'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_authorization_url</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC559'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Get Authorization URL.&quot;&quot;&quot;</span></div><div class='line' id='LC560'><br/></div><div class='line' id='LC561'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_auth_token</span><span class="p">()</span></div><div class='line' id='LC562'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">(</span><span class="s">&quot;https://www.linkedin.com/uas/oauth/authenticate?oauth_token=</span><span class="si">%s</span><span class="s">&quot;</span></div><div class='line' id='LC563'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp;oauth_callback=</span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">token</span><span class="p">,</span> <span class="n">urlquote</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">callback_url</span><span class="p">)))</span></div><div class='line' id='LC564'><br/></div><div class='line' id='LC565'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_lookup_user_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">access_token</span><span class="p">,</span> <span class="n">access_secret</span><span class="p">):</span></div><div class='line' id='LC566'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Lookup User Info.</span></div><div class='line' id='LC567'><br/></div><div class='line' id='LC568'><span class="sd">    Lookup the user on LinkedIn</span></div><div class='line' id='LC569'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC570'><br/></div><div class='line' id='LC571'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_default_user_info</span><span class="p">()</span></div><div class='line' id='LC572'><br/></div><div class='line' id='LC573'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Grab the user&#39;s profile from LinkedIn.</span></div><div class='line' id='LC574'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">make_request</span><span class="p">(</span><span class="s">&quot;http://api.linkedin.com/v1/people/~:&quot;</span></div><div class='line' id='LC575'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;(picture-url,id,first-name,last-name)&quot;</span><span class="p">,</span></div><div class='line' id='LC576'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">token</span><span class="o">=</span><span class="n">access_token</span><span class="p">,</span></div><div class='line' id='LC577'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">secret</span><span class="o">=</span><span class="n">access_secret</span><span class="p">,</span></div><div class='line' id='LC578'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">protected</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span></div><div class='line' id='LC579'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">headers</span><span class="o">=</span><span class="p">{</span><span class="s">&quot;x-li-format&quot;</span><span class="p">:</span><span class="s">&quot;json&quot;</span><span class="p">})</span></div><div class='line' id='LC580'><br/></div><div class='line' id='LC581'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">)</span></div><div class='line' id='LC582'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;id&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;id&quot;</span><span class="p">]</span></div><div class='line' id='LC583'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;picture&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;pictureUrl&quot;</span><span class="p">]</span></div><div class='line' id='LC584'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;name&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;firstName&quot;</span><span class="p">]</span> <span class="o">+</span> <span class="s">&quot; &quot;</span> <span class="o">+</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;lastName&quot;</span><span class="p">]</span></div><div class='line' id='LC585'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">user_info</span></div><div class='line' id='LC586'><br/></div><div class='line' id='LC587'><br/></div><div class='line' id='LC588'><span class="k">class</span> <span class="nc">YammerClient</span><span class="p">(</span><span class="n">OAuthClient</span><span class="p">):</span></div><div class='line' id='LC589'>&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Yammer Client.</span></div><div class='line' id='LC590'><br/></div><div class='line' id='LC591'><span class="sd">  A client for talking to the Yammer API using OAuth as the</span></div><div class='line' id='LC592'><span class="sd">  authentication model.</span></div><div class='line' id='LC593'><span class="sd">  &quot;&quot;&quot;</span></div><div class='line' id='LC594'><br/></div><div class='line' id='LC595'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">consumer_key</span><span class="p">,</span> <span class="n">consumer_secret</span><span class="p">,</span> <span class="n">callback_url</span><span class="p">):</span></div><div class='line' id='LC596'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Constructor.&quot;&quot;&quot;</span></div><div class='line' id='LC597'><br/></div><div class='line' id='LC598'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">OAuthClient</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span></div><div class='line' id='LC599'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">YAMMER</span><span class="p">,</span></div><div class='line' id='LC600'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">consumer_key</span><span class="p">,</span></div><div class='line' id='LC601'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">consumer_secret</span><span class="p">,</span></div><div class='line' id='LC602'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;https://www.yammer.com/oauth/request_token&quot;</span><span class="p">,</span></div><div class='line' id='LC603'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;https://www.yammer.com/oauth/access_token&quot;</span><span class="p">,</span></div><div class='line' id='LC604'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">callback_url</span><span class="p">)</span></div><div class='line' id='LC605'><br/></div><div class='line' id='LC606'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_authorization_url</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC607'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Get Authorization URL.&quot;&quot;&quot;</span></div><div class='line' id='LC608'><br/></div><div class='line' id='LC609'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_auth_token</span><span class="p">()</span></div><div class='line' id='LC610'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">(</span><span class="s">&quot;https://www.yammer.com/oauth/authorize?oauth_token=</span><span class="si">%s</span><span class="s">&quot;</span></div><div class='line' id='LC611'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&amp;oauth_callback=</span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">token</span><span class="p">,</span> <span class="n">urlquote</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">callback_url</span><span class="p">)))</span></div><div class='line' id='LC612'><br/></div><div class='line' id='LC613'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_lookup_user_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">access_token</span><span class="p">,</span> <span class="n">access_secret</span><span class="p">):</span></div><div class='line' id='LC614'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Lookup User Info.</span></div><div class='line' id='LC615'><br/></div><div class='line' id='LC616'><span class="sd">    Lookup the user on Yammer</span></div><div class='line' id='LC617'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC618'><br/></div><div class='line' id='LC619'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_default_user_info</span><span class="p">()</span></div><div class='line' id='LC620'><br/></div><div class='line' id='LC621'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Grab the user&#39;s profile from Yammer.</span></div><div class='line' id='LC622'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">make_request</span><span class="p">(</span><span class="s">&quot;https://www.yammer.com/api/v1/users/current.json&quot;</span><span class="p">,</span></div><div class='line' id='LC623'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">token</span><span class="o">=</span><span class="n">access_token</span><span class="p">,</span></div><div class='line' id='LC624'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">secret</span><span class="o">=</span><span class="n">access_secret</span><span class="p">,</span></div><div class='line' id='LC625'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">protected</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span></div><div class='line' id='LC626'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">headers</span><span class="o">=</span><span class="p">{</span><span class="s">&quot;x-li-format&quot;</span><span class="p">:</span><span class="s">&quot;json&quot;</span><span class="p">})</span></div><div class='line' id='LC627'><br/></div><div class='line' id='LC628'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">)</span></div><div class='line' id='LC629'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_default_user_info</span><span class="p">()</span></div><div class='line' id='LC630'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;id&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;name&quot;</span><span class="p">]</span></div><div class='line' id='LC631'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;picture&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;mugshot_url&quot;</span><span class="p">]</span></div><div class='line' id='LC632'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_info</span><span class="p">[</span><span class="s">&quot;name&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">&quot;full_name&quot;</span><span class="p">]</span></div><div class='line' id='LC633'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">user_info</span></div><div class='line' id='LC634'><br/></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>
      </div>
    </div>

  </div>

<div class="frame frame-loading" style="display:none;" data-tree-list-url="/mikeknapp/AppEngine-OAuth-Library/tree-list/269b2b0ed882fa38d185c795d8ba46a04f10f5f3" data-blob-url-prefix="/mikeknapp/AppEngine-OAuth-Library/blob/269b2b0ed882fa38d185c795d8ba46a04f10f5f3">
  <img src="https://a248.e.akamai.net/assets.github.com/images/modules/ajax/big_spinner_336699.gif" height="32" width="32">
</div>

    </div>

    </div>

    <!-- footer -->
    <div id="footer" >
      
  <div class="upper_footer">
     <div class="site" class="clearfix">

       <!--[if IE]><h4 id="blacktocat_ie">GitHub Links</h4><![endif]-->
       <![if !IE]><h4 id="blacktocat">GitHub Links</h4><![endif]>

       <ul class="footer_nav">
         <h4>GitHub</h4>
         <li><a href="https://github.com/about">About</a></li>
         <li><a href="https://github.com/blog">Blog</a></li>
         <li><a href="https://github.com/features">Features</a></li>
         <li><a href="https://github.com/contact">Contact &amp; Support</a></li>
         <li><a href="https://github.com/training">Training</a></li>
         <li><a href="http://status.github.com/">Site Status</a></li>
       </ul>

       <ul class="footer_nav">
         <h4>Tools</h4>
         <li><a href="http://mac.github.com/">GitHub for Mac</a></li>
         <li><a href="http://mobile.github.com/">Issues for iPhone</a></li>
         <li><a href="https://gist.github.com">Gist: Code Snippets</a></li>
         <li><a href="http://enterprise.github.com/">GitHub Enterprise</a></li>
         <li><a href="http://jobs.github.com/">Job Board</a></li>
       </ul>

       <ul class="footer_nav">
         <h4>Extras</h4>
         <li><a href="http://shop.github.com/">GitHub Shop</a></li>
         <li><a href="http://octodex.github.com/">The Octodex</a></li>
       </ul>

       <ul class="footer_nav">
         <h4>Documentation</h4>
         <li><a href="http://help.github.com/">GitHub Help</a></li>
         <li><a href="http://developer.github.com/">Developer API</a></li>
         <li><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></li>
         <li><a href="http://pages.github.com/">GitHub Pages</a></li>
       </ul>

     </div><!-- /.site -->
  </div><!-- /.upper_footer -->

<div class="lower_footer">
  <div class="site" class="clearfix">
    <!--[if IE]><div id="legal_ie"><![endif]-->
    <![if !IE]><div id="legal"><![endif]>
      <ul>
          <li><a href="https://github.com/site/terms">Terms of Service</a></li>
          <li><a href="https://github.com/site/privacy">Privacy</a></li>
          <li><a href="https://github.com/security">Security</a></li>
      </ul>

      <p>&copy; 2011 <span id="_rrt" title="0.46892s from fe9.rs.github.com">GitHub</span> Inc. All rights reserved.</p>
    </div><!-- /#legal or /#legal_ie-->

      <div class="sponsor">
        <a href="http://www.rackspace.com" class="logo">
          <img alt="Dedicated Server" height="36" src="https://a248.e.akamai.net/assets.github.com/images/modules/footer/rackspace_logo.png?v2" width="38" />
        </a>
        Powered by the <a href="http://www.rackspace.com ">Dedicated
        Servers</a> and<br/> <a href="http://www.rackspacecloud.com">Cloud
        Computing</a> of Rackspace Hosting<span>&reg;</span>
      </div>
  </div><!-- /.site -->
</div><!-- /.lower_footer -->

    </div><!-- /#footer -->

    

<div id="keyboard_shortcuts_pane" class="instapaper_ignore readability-extra" style="display:none">
  <h2>Keyboard Shortcuts <small><a href="#" class="js-see-all-keyboard-shortcuts">(see all)</a></small></h2>

  <div class="columns threecols">
    <div class="column first">
      <h3>Site wide shortcuts</h3>
      <dl class="keyboard-mappings">
        <dt>s</dt>
        <dd>Focus site search</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>?</dt>
        <dd>Bring up this help dialog</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column middle" style=&#39;display:none&#39;>
      <h3>Commit list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selection down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selection up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>c <em>or</em> o <em>or</em> enter</dt>
        <dd>Open commit</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>y</dt>
        <dd>Expand URL to its canonical form</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column last" style=&#39;display:none&#39;>
      <h3>Pull request list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selection down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selection up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>o <em>or</em> enter</dt>
        <dd>Open issue</dd>
      </dl>
    </div><!-- /.columns.last -->

  </div><!-- /.columns.equacols -->

  <div style=&#39;display:none&#39;>
    <div class="rule"></div>

    <h3>Issues</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selection down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selection up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>x</dt>
          <dd>Toggle selection</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column middle">
        <dl class="keyboard-mappings">
          <dt>I</dt>
          <dd>Mark selection as read</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>U</dt>
          <dd>Mark selection as unread</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>e</dt>
          <dd>Close selection</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>y</dt>
          <dd>Remove selection from view</dd>
        </dl>
      </div><!-- /.column.middle -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>c</dt>
          <dd>Create issue</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Create label</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>i</dt>
          <dd>Back to inbox</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>u</dt>
          <dd>Back to issues</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>/</dt>
          <dd>Focus issues search</dd>
        </dl>
      </div>
    </div>
  </div>

  <div style=&#39;display:none&#39;>
    <div class="rule"></div>

    <h3>Issues Dashboard</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selection down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selection up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
      </div><!-- /.column.first -->
    </div>
  </div>

  <div style=&#39;display:none&#39;>
    <div class="rule"></div>

    <h3>Network Graph</h3>
    <div class="columns equacols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt><span class="badmono">←</span> <em>or</em> h</dt>
          <dd>Scroll left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">→</span> <em>or</em> l</dt>
          <dd>Scroll right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↑</span> <em>or</em> k</dt>
          <dd>Scroll up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↓</span> <em>or</em> j</dt>
          <dd>Scroll down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Toggle visibility of head labels</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">←</span> <em>or</em> shift h</dt>
          <dd>Scroll all the way left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">→</span> <em>or</em> shift l</dt>
          <dd>Scroll all the way right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↑</span> <em>or</em> shift k</dt>
          <dd>Scroll all the way up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↓</span> <em>or</em> shift j</dt>
          <dd>Scroll all the way down</dd>
        </dl>
      </div><!-- /.column.last -->
    </div>
  </div>

  <div >
    <div class="rule"></div>
    <div class="columns threecols">
      <div class="column first" >
        <h3>Source Code Browsing</h3>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Activates the file finder</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Jump to line</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>w</dt>
          <dd>Switch branch/tag</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>y</dt>
          <dd>Expand URL to its canonical form</dd>
        </dl>
      </div>
    </div>
  </div>
</div>

    <div id="markdown-help" class="instapaper_ignore readability-extra">
  <h2>Markdown Cheat Sheet</h2>

  <div class="cheatsheet-content">

  <div class="mod">
    <div class="col">
      <h3>Format Text</h3>
      <p>Headers</p>
      <pre>
# This is an &lt;h1&gt; tag
## This is an &lt;h2&gt; tag
###### This is an &lt;h6&gt; tag</pre>
     <p>Text styles</p>
     <pre>
*This text will be italic*
_This will also be italic_
**This text will be bold**
__This will also be bold__

*You **can** combine them*
</pre>
    </div>
    <div class="col">
      <h3>Lists</h3>
      <p>Unordered</p>
      <pre>
* Item 1
* Item 2
  * Item 2a
  * Item 2b</pre>
     <p>Ordered</p>
     <pre>
1. Item 1
2. Item 2
3. Item 3
   * Item 3a
   * Item 3b</pre>
    </div>
    <div class="col">
      <h3>Miscellaneous</h3>
      <p>Images</p>
      <pre>
![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)
</pre>
     <p>Links</p>
     <pre>
http://github.com - automatic!
[GitHub](http://github.com)</pre>
<p>Blockquotes</p>
     <pre>
As Kanye West said:
> We're living the future so
> the present is our past.
</pre>
    </div>
  </div>
  <div class="rule"></div>

  <h3>Code Examples in Markdown</h3>
  <div class="col">
      <p>Syntax highlighting with <a href="http://github.github.com/github-flavored-markdown/" title="GitHub Flavored Markdown" target="_blank">GFM</a></p>
      <pre>
```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```</pre>
    </div>
    <div class="col">
      <p>Or, indent your code 4 spaces</p>
      <pre>
Here is a Python code example
without syntax highlighting:

    def foo:
      if not bar:
        return true</pre>
    </div>
    <div class="col">
      <p>Inline code for comments</p>
      <pre>
I think you should use an
`&lt;addr&gt;` element here instead.</pre>
    </div>
  </div>

  </div>
</div>

    <div class="context-overlay"></div>

    <div class="ajax-error-message">
      <p><span class="icon"></span> Something went wrong with that request. Please try again. <a href="javascript:;" class="ajax-error-dismiss">Dismiss</a></p>
    </div>

    
    
    
  </body>
</html>

