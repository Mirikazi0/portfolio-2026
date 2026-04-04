document.addEventListener('DOMContentLoaded', () => {
    if (window.matchMedia('(pointer: fine)').matches) {
        const cursor = document.getElementById('custom-cursor');
        if (!cursor) return;
        
        document.addEventListener('mousemove', (e) => {
            cursor.style.transform = `translate3d(${e.clientX}px, ${e.clientY}px, 0) translate(-50%, -50%)`;
        });

        // Add hover effect for preview images globally
        const previewImages = document.querySelectorAll('.case-study-image, .card-image, .carousel-card');
        previewImages.forEach(img => {
            img.addEventListener('mouseenter', () => {
                cursor.classList.add('view-mode');
            });
            img.addEventListener('mouseleave', () => {
                cursor.classList.remove('view-mode');
            });
        });
    }
});
