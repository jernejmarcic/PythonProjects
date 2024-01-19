document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('dark-mode-toggle');

    // Check if user has a preferred theme
    initializeTheme();

    toggle.addEventListener('change', function() {
        if (this.checked) {
            // Apply Dark Theme
            applyTheme('dark');
        } else {
            // Apply Light Theme
            applyTheme('light');
        }
    });
});

function applyTheme(theme) {
    const body = document.body;

    if (theme === 'dark') {
        body.classList.add('dark-theme');
        body.classList.remove('light-theme');
    } else {
        body.classList.add('light-theme');
        body.classList.remove('dark-theme');
    }
}

function initializeTheme() {
    const toggle = document.getElementById('dark-mode-toggle');
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (prefersDark) {
        applyTheme('dark');
        toggle.checked = true;
    } else {
        applyTheme('light');
        toggle.checked = false;
    }
}

function editNote(noteId, noteTitle, noteContent) {
    // Set the note ID
    document.getElementById('note-id').value = noteId;

    // Set the note title
    document.getElementById('title').value = noteTitle;

    // Set the note content in TinyMCE
    tinymce.get('note').setContent(noteContent);
}




function toggleSidebar() {
    var sidebar = document.getElementById('sidebar');
    if (sidebar.style.left === '-250px' || sidebar.style.left === '') {
        sidebar.style.left = '0';
    } else {
        sidebar.style.left = '-250px';
    }
}

document.addEventListener('DOMContentLoaded', function() {
  var sidebar = document.getElementById('sidebar');
  var toggleBtn = document.querySelector('.sidebar .toggle-btn');

  // Toggle sidebar
  toggleBtn.addEventListener('click', function() {
    if (sidebar.style.left === '-250px') {
      sidebar.style.left = '0';
    } else {
      sidebar.style.left = '-250px';
    }
  });

  // Keyboard shortcut (Tab key) to toggle sidebar
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Tab') {
      e.preventDefault(); // Prevent default tab behavior
      toggleBtn.click(); // Trigger the sidebar toggle
    }
  });
});

const sidebar = document.querySelector('.sidebar');
const resizeHandle = document.querySelector('.sidebar-resize-handle');

resizeHandle.addEventListener('mousedown', function(e) {
  document.addEventListener('mousemove', resizeSidebar);
  document.addEventListener('mouseup', stopResizing);
});



document.addEventListener('DOMContentLoaded', (event) => {
    
function resizeSidebar(e) {
  const newWidth = e.clientX - sidebar.getBoundingClientRect().left;
  console.log(newWidth); // Just log the width for testing
  if (newWidth > 100) { // Minimum width
    sidebar.style.width = newWidth + 'px';
  }
}

function stopResizing() {
  document.removeEventListener('mousemove', resizeSidebar);
}
});

